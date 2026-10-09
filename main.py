"""Small command-line interface for the visual-only workflows."""
import argparse
import json
from pathlib import Path
from visual_search.common import Client, deduplicate, read_csv, save_json, utc_now
from visual_search.files import download_pdfs, import_wos, screen_records, write_screening
from visual_search.providers import VENUES, collect_pages, conference_lists, conference_records, database_page
from visual_search.scope import QUERIES

SOURCES = ('openalex', 'conferences', 'semantic-scholar', 'crossref')
RELEASE = Path(__file__).resolve().parent


def new_output(path):
    """Require a fresh output directory; never replace sources or previous runs."""
    output = path.resolve()
    protected = (RELEASE / 'visual_search', RELEASE / 'tests')
    if output == RELEASE or output in RELEASE.parents or any(output == p or p in output.parents for p in protected):
        raise ValueError('Choose a separate run directory')
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ValueError('Output must be an empty or new directory')
    output.mkdir(parents=True, exist_ok=True)
    return output


def search(client, output, sources, venues):
    log = {'started_utc': utc_now(), 'date_restrictions': None, 'queries': list(QUERIES),
           'sources': sources, 'venues': list(venues), 'searches': [], 'complete': False}
    records = []
    with (output / 'retrieved.jsonl').open('w', encoding='utf-8') as saved:
        def emit(rows):
            for row in rows:
                if not row.get('title'):
                    raise ValueError('Provider returned a record without a title')
                records.append(row)
                saved.write(json.dumps(row, ensure_ascii=False) + '\n')
            saved.flush()

        def job(description, action):
            status = dict(description, complete=False)
            log['searches'].append(status)
            save_json(output / 'search_log.json', log)
            try:
                action(status)
            except Exception as exc:
                status.update(complete=False, error=str(exc))
            save_json(output / 'search_log.json', log)
            print(description, 'complete' if status['complete'] else 'INCOMPLETE', flush=True)

        try:
            for source in sources:
                if source == 'conferences':
                    lists = []
                    def discover(status):
                        lists.extend(conference_lists(client, venues))
                        status.update(complete=True, lists=lists)
                    job({'source': source, 'step': 'discover_available_lists'}, discover)
                    for listing in lists:
                        def fetch_conference(status, listing=listing):
                            count = 0
                            for row in conference_records(client, listing):
                                emit([row])
                                count += 1
                            status.update(complete=True, retrieved=count)
                        job({'source': source, **listing}, fetch_conference)
                else:
                    for query in QUERIES:
                        job({'source': source, 'query': query},
                            lambda status, source=source, query=query: collect_pages(
                                lambda cursor: database_page(client, source, query, cursor), emit, status))
            log['complete'] = all(s['complete'] for s in log['searches'])
        finally:
            # Even interrupted or failed retrieval leaves inspectable partial results.
            log['finished_utc'] = utc_now()
            save_json(output / 'search_log.json', log)
            write_screening(output, screen_records(deduplicate(records)))
    return log['complete']


def parser():
    root = argparse.ArgumentParser(description='Visual-counterfactual literature search and automatic screening.')
    commands = root.add_subparsers(dest='command', required=True)
    discovery = commands.add_parser('search', help='Search all available dates; follow all result pages.')
    discovery.add_argument('--sources', nargs='+', choices=SOURCES, default=['openalex', 'conferences'])
    discovery.add_argument('--venues', nargs='+', choices=VENUES, default=list(VENUES))
    screening = commands.add_parser('screen', help='Screen an existing metadata CSV; optionally consult PDFs.')
    screening.add_argument('--input', required=True, type=Path)
    screening.add_argument('--pdf-dir', type=Path)
    download = commands.add_parser('download', help='Download all available candidate/review PDFs, without a count cap.')
    download.add_argument('--input', required=True, type=Path)
    imports = commands.add_parser('import-wos', help='Import and visually screen supplied full-record exports.')
    imports.add_argument('--input-dir', required=True, type=Path)
    for command in (discovery, screening, download, imports):
        command.add_argument('--output', required=True, type=Path, help='New or empty run directory.')
    return root


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        output = new_output(args.output)
        if args.command == 'search':
            success = search(Client(), output, list(dict.fromkeys(args.sources)), args.venues)
        elif args.command == 'download':
            success = download_pdfs(Client(), read_csv(args.input), output)
        else:
            rows = import_wos(args.input_dir) if args.command == 'import-wos' else read_csv(args.input)
            if any(not row.get('title') for row in rows):
                raise ValueError('Every input record must have a title')
            records = screen_records(deduplicate(rows), getattr(args, 'pdf_dir', None))
            write_screening(output, records)
            success = not any(r['pdf_evidence_status'] == 'extraction_failed' for r in records)
        print('Finished.' if success else 'Finished with incomplete retrieval or processing; inspect output logs.')
        return 0 if success else 1
    except (ValueError, OSError, ImportError, RuntimeError) as exc:
        print('Error:', str(exc))
        return 1
    except KeyboardInterrupt:
        print('Interrupted. Saved results are partial.')
        return 130

if __name__ == '__main__':
    raise SystemExit(main())
