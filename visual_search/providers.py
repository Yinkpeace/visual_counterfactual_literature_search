"""Provider adapters. Date restrictions and total-result caps are not applied."""
import re
from .common import clean, normalized_doi

# Transport batch sizes, not retrieval limits. Cursors are followed to exhaustion.
OPENALEX_PAGE_SIZE = 100
CROSSREF_PAGE_SIZE = 1000
VENUES = ('aaai', 'aistats', 'corl', 'cvpr', 'eccv', 'iccv', 'iclr', 'icml',
          'icra', 'ijcai', 'iros', 'kdd', 'nips', 'rss', 'uai')


def decode_abstract(index):
    words = [(position, word) for word, positions in (index or {}).items() for position in positions]
    return ' '.join(word for _, word in sorted(words))


def normalize(source, item):
    """Convert each provider's public metadata to the same small schema."""
    if source == 'openalex':
        location = item.get('primary_location') or {}
        venue = location.get('source') or {}
        pdfs = [x.get('pdf_url') for x in item.get('locations') or [] if x]
        data = dict(
            source_record_id=item.get('id'), title=item.get('display_name'),
            abstract=decode_abstract(item.get('abstract_inverted_index')),
            authors=[(a.get('author') or {}).get('display_name') for a in item.get('authorships') or []],
            year=item.get('publication_year'), publication_date=item.get('publication_date'),
            venue=venue.get('display_name'), publication_type=item.get('type'), doi=item.get('doi'),
            url=item.get('doi') or item.get('id'), pdf_url=next((p for p in pdfs if p), ''),
        )
    elif source == 'semantic-scholar':
        data = dict(
            source_record_id=item.get('paperId'), title=item.get('title'), abstract=item.get('abstract'),
            authors=item.get('authors'), year=item.get('year'), publication_date=item.get('publicationDate'),
            venue=item.get('venue'), publication_type=item.get('publicationTypes'),
            doi=(item.get('externalIds') or {}).get('DOI'), url=item.get('url'),
            pdf_url=(item.get('openAccessPdf') or {}).get('url'),
        )
    else:
        date = (item.get('published') or {}).get('date-parts') or [[]]
        date = date[0]
        links = [x.get('URL') for x in item.get('link') or [] if x.get('content-type') == 'application/pdf']
        data = dict(
            source_record_id=item.get('DOI'), title=item.get('title'), abstract=item.get('abstract'),
            authors=[' '.join(filter(None, [a.get('given'), a.get('family')])) for a in item.get('author') or []],
            year=date[0] if date else '', publication_date='-'.join(str(x).zfill(2) for x in date),
            venue=item.get('container-title'), publication_type=item.get('type'), doi=item.get('DOI'),
            url=item.get('URL'), pdf_url=next((p for p in links if p), ''),
        )
    row = {key: clean(value) for key, value in data.items()}
    row['doi'] = normalized_doi(row['doi'])
    row['source'] = source
    return row


def database_page(client, source, query, cursor):
    """Return (records, next cursor, reported total); None marks exhaustion."""
    if source == 'openalex':
        payload = client.get_json('https://api.openalex.org/works',
            {'search': query, 'per_page': OPENALEX_PAGE_SIZE, 'cursor': cursor or '*'})
        items = payload['results']
        next_cursor = payload['meta']['next_cursor']
        total = payload['meta'].get('count')
    elif source == 'semantic-scholar':
        params = {'query': query, 'fields': 'title,abstract,authors,year,publicationDate,venue,publicationTypes,externalIds,url,openAccessPdf'}
        if cursor:
            params['token'] = cursor
        payload = client.get_json('https://api.semanticscholar.org/graph/v1/paper/search/bulk', params)
        items, next_cursor, total = payload['data'], payload.get('token'), payload.get('total')
    elif source == 'crossref':
        payload = client.get_json('https://api.crossref.org/works',
            {'query.bibliographic': query, 'rows': CROSSREF_PAGE_SIZE, 'cursor': cursor or '*'})['message']
        items = payload['items']
        next_cursor = payload.get('next-cursor') if len(items) == CROSSREF_PAGE_SIZE else None
        total = payload.get('total-results')
        if len(items) == CROSSREF_PAGE_SIZE and not next_cursor:
            raise RuntimeError('Crossref full page lacks a continuation cursor')
    else:
        raise ValueError('Unknown database: ' + source)
    if not isinstance(items, list):
        raise ValueError('Unexpected provider result schema')
    rows = [dict(normalize(source, item), query=query) for item in items]
    return rows, next_cursor, total


def collect_pages(fetch, emit, status):
    """Follow every continuation token and preserve earlier pages on failure.

    emit receives one normalized page at a time. status is updated even when
    fetching fails, so callers cannot mistake a partial search for completion.
    """
    cursor, seen = None, set()
    status.update(pages=0, retrieved=0, reported_total=None, complete=False)
    while True:
        rows, following, total = fetch(cursor)
        emit(rows)
        status['pages'] += 1
        status['retrieved'] += len(rows)
        if status['reported_total'] is None:
            status['reported_total'] = total
        if not following:
            if status['reported_total'] is not None and status['retrieved'] < status['reported_total']:
                raise RuntimeError('Provider ended before its reported count; retrieval requires checking')
            status['complete'] = True
            return
        if following == cursor or following in seen:
            raise RuntimeError('Repeated continuation token; retrieval incomplete')
        seen.add(following)
        cursor = following


def conference_lists(client, venues=VENUES):
    """Discover all available years/tracks at a pinned repository commit."""
    tree = client.get_json('https://api.github.com/repos/papercopilot/paperlists/git/trees/main', {'recursive': '1'})
    if tree.get('truncated'):
        raise RuntimeError('Conference repository listing is truncated')
    commit, found = tree['sha'], []
    for entry in tree['tree']:
        path = entry['path']
        match = re.fullmatch(r'([^/]+)/\1(\d{4})(?:_[^/]+)?\.json', path)
        if entry['type'] == 'blob' and match and match[1] in venues:
            found.append({'path': path, 'venue': match[1], 'year': match[2], 'commit': commit})
    missing = set(venues) - {x['venue'] for x in found}
    if missing:
        raise RuntimeError('No conference lists found for: ' + ', '.join(sorted(missing)))
    return sorted(found, key=lambda x: x['path'])


def conference_records(client, listing):
    path, commit = listing['path'], listing['commit']
    raw_url = f'https://raw.githubusercontent.com/papercopilot/paperlists/{commit}/{path}'
    content = client.get_bytes(raw_url)
    if content.startswith(b'version https://git-lfs.github.com'):
        content = client.get_bytes(f'https://media.githubusercontent.com/media/papercopilot/paperlists/{commit}/{path}')
    import json
    items = json.loads(content)
    if not isinstance(items, list):
        raise ValueError('Unexpected conference-list schema')
    for item in items:
        status = clean(item.get('status')).lower()
        if any(x in status for x in ('reject', 'withdraw', 'submitted', 'under review')):
            continue
        # Entries with no explicit acceptance label remain reviewable.
        accepted = any(x in status for x in ('accept', 'poster', 'oral', 'spotlight', 'main', 'technical', 'conference'))
        url = clean(item.get('site') or item.get('openreview'))
        pdf = clean(item.get('pdf') or item.get('oa'))
        if not pdf and 'openreview.net/forum?id=' in url:
            pdf = url.replace('/forum?id=', '/pdf?id=')
        yield dict(
            source='conferences', source_record_id=clean(item.get('id') or item.get('paper_id') or url),
            title=clean(item.get('title')), abstract=clean(item.get('abstract') or item.get('tldr')),
            authors=clean(item.get('authors') or item.get('author')), year=listing['year'],
            publication_date='', venue=listing['venue'].upper(), publication_type='conference',
            doi=normalized_doi(item.get('doi')), url=url, pdf_url=pdf,
            query='visual-counterfactual screening of ' + path,
            conference_status='accepted' if accepted else 'acceptance_unverified',
            source_list_url=raw_url,
        )
