"""Optional PDF retrieval, PDF-assisted screening, and supplied-export import."""
from pathlib import Path
from .common import clean, normalized_doi, read_csv, record_id, write_csv
from .scope import screen


def screen_records(records, pdf_dir=None):
    result = []
    for original in records:
        row = dict(original)
        row['record_id'] = record_id(row)
        text, pdf_status = '', 'not_requested'
        if pdf_dir:
            from pypdf import PdfReader
            path = Path(pdf_dir) / (row['record_id'] + '.pdf')
            pdf_status = 'missing'
            if path.exists():
                try:
                    text = '\n'.join(page.extract_text() or '' for page in PdfReader(path).pages)
                    pdf_status = 'extracted' if text.strip() else 'no_extractable_text'
                except Exception:
                    pdf_status = 'extraction_failed'
        row.update(screen(row, text))
        if row.get('conference_status') == 'acceptance_unverified' and row['screening_decision'] == 'candidate':
            row.update(screening_decision='manual_review', screening_reason='conference_acceptance_unverified')
        row['pdf_evidence_status'] = pdf_status
        result.append(row)
    return result


def write_screening(output, records):
    write_csv(output / 'screening.csv', records)
    write_csv(output / 'candidates.csv', [r for r in records if r['screening_decision'] == 'candidate'])
    write_csv(output / 'manual_review.csv', [r for r in records if r['screening_decision'] == 'manual_review'])


def download_pdfs(client, records, output):
    """Attempt every candidate/review PDF URL; no numerical download cap."""
    folder = output / 'pdfs'
    folder.mkdir()
    log = []
    for row in records:
        decision = row.get('screening_decision') or screen(row)['screening_decision']
        if decision not in ('candidate', 'manual_review'):
            continue
        entry = {'record_id': record_id(row), 'title': row.get('title', ''),
                 'pdf_url': row.get('pdf_url', ''), 'status': 'no_pdf_url', 'error': ''}
        if entry['pdf_url']:
            try:
                content = client.get_bytes(entry['pdf_url'])
                if not content.lstrip().startswith(b'%PDF-'):
                    raise ValueError('Response is not a PDF')
                (folder / (entry['record_id'] + '.pdf')).write_bytes(content)
                entry['status'] = 'downloaded'
            except Exception as exc:
                entry.update(status='failed', error=str(exc))
        log.append(entry)
        write_csv(output / 'downloads.csv', log)
    if not log:
        write_csv(output / 'downloads.csv', log)
    return not any(row['status'] == 'failed' for row in log)


def import_wos(folder):
    """Read complete field-tagged full-record exports supplied by the reader."""
    paths = sorted(Path(folder).glob('*.txt'))
    if not paths:
        raise ValueError('No .txt export files found')
    rows = []
    for path in paths:
        data = path.read_bytes()
        try:
            text = data.decode('utf-8-sig')
        except UnicodeDecodeError:
            text = data.decode('cp1252')
        if not text.rstrip().endswith('EF'):
            raise ValueError('Incomplete export: ' + path.name)
        item, tag = {}, None
        for line in text.splitlines():
            if line == 'ER':
                field = lambda key: clean(item.get(key, []))
                if not field('UT') or not field('TI'):
                    raise ValueError('Export record lacks accession or title: ' + path.name)
                doi = normalized_doi(field('DI'))
                rows.append(dict(source='web-of-science', source_record_id=field('UT'),
                    title=field('TI'), abstract=field('AB'), authors=field('AF') or field('AU'),
                    year=field('PY'), publication_date='', venue=field('SO'), publication_type=field('DT'),
                    doi=doi, url='https://doi.org/' + doi if doi else '', pdf_url='',
                    query='supplied export: ' + path.name))
                item, tag = {}, None
            elif re_tag(line):
                tag = line[:2]
                item.setdefault(tag, []).append(line[3:])
            elif line.startswith('   ') and tag:
                item[tag].append(line[3:])
    return rows


def re_tag(line):
    return len(line) >= 3 and line[:2].isupper() and line[2] == ' '
