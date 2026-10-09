"""Network access, record identities, and auditable output helpers."""
import csv
import hashlib
import html
import json
import os
import re
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def clean(value):
    if isinstance(value, list):
        return '; '.join(filter(None, (clean(x) for x in value)))
    if isinstance(value, dict):
        return clean(value.get('name') or value.get('author') or '')
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', str(value or '')))).strip()


def normalized_title(value):
    return ''.join(c for c in unicodedata.normalize('NFKD', clean(value)).casefold() if c.isalnum())


def normalized_doi(value):
    return re.sub(r'^https?://(?:dx\.)?doi\.org/', '', clean(value).lower()).strip()


def record_id(record):
    identity = record.get('doi') or normalized_title(record.get('title')) or record.get('url') or record.get('source_record_id')
    if not identity:
        raise ValueError('Record has no usable identity')
    return hashlib.sha256(identity.encode('utf-8')).hexdigest()[:20]


def save_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def read_csv(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def write_csv(path, records):
    fields = list(dict.fromkeys(k for r in records for k in r)) or ['record_id', 'title']
    with Path(path).open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fields)
        writer.writeheader()
        writer.writerows(records)


class Client:
    """Retry transient errors without exposing credentials in saved requests."""
    def __init__(self, delay=1.0):
        self.delay = delay

    def get_bytes(self, url, params=None):
        if urlparse(url).scheme not in ('https', 'http'):
            raise ValueError('Only HTTP(S) retrieval is supported')
        host = urlparse(url).hostname
        headers = {'User-Agent': 'VisualCounterfactualReview/1.0'}
        keys = {
            'api.openalex.org': ('OPENALEX_API_KEY', 'Authorization', 'Bearer '),
            'api.semanticscholar.org': ('SEMANTIC_SCHOLAR_API_KEY', 'x-api-key', ''),
            'api.github.com': ('GITHUB_TOKEN', 'Authorization', 'Bearer '),
        }
        if host in keys:
            variable, header, prefix = keys[host]
            if os.environ.get(variable):
                headers[header] = prefix + os.environ[variable]
        full_url = url + ('?' + urlencode(params) if params else '')
        for attempt in range(4):
            time.sleep(self.delay)
            try:
                with urlopen(Request(full_url, headers=headers), timeout=90) as response:
                    return response.read()
            except HTTPError as exc:
                if attempt == 3 or exc.code not in (429, 500, 502, 503, 504):
                    raise RuntimeError(f'{host}: HTTP {exc.code}; retrieval incomplete') from None
                try:
                    wait = float(exc.headers.get('Retry-After', 0))
                except ValueError:
                    wait = 0
                time.sleep(min(60, max(wait, 2 ** (attempt + 1))))
            except (URLError, TimeoutError, OSError):
                if attempt == 3:
                    raise RuntimeError(f'{host}: network failure; retrieval incomplete') from None
                time.sleep(2 ** (attempt + 1))

    def get_json(self, url, params=None):
        return json.loads(self.get_bytes(url, params).decode('utf-8-sig'))


def deduplicate(records):
    """Merge DOI/exact-title matches while retaining query/source provenance."""
    merged, dois, titles = [], {}, {}
    for original in records:
        row = dict(original)
        doi, title = normalized_doi(row.get('doi')), normalized_title(row.get('title'))
        row['doi'] = doi
        match = dois.get(doi) if doi else None
        if match is None and title:
            for candidate in titles.get(title, []):
                if not doi or not candidate.get('doi') or candidate['doi'] == doi:
                    match = candidate
                    break
        if match is None:
            merged.append(row)
            match = row
        else:
            for key, value in row.items():
                if not match.get(key) and value:
                    match[key] = value
            for key in ('source', 'query', 'source_record_id'):
                match[key] = '; '.join(dict.fromkeys(filter(None, (match.get(key, '') + '; ' + row.get(key, '')).split('; '))))
        if doi:
            dois[doi] = match
        if title:
            bucket = titles.setdefault(title, [])
            if not any(item is match for item in bucket):
                bucket.append(match)
    for row in merged:
        row['record_id'] = record_id(row)
    return merged
