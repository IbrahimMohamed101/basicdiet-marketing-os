"""Versioned local records. No networking; malformed input fails closed."""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

GOALS = {'Awareness', 'Consideration', 'Trust', 'Conversion', 'Engagement'}
CHANNELS = {'instagram', 'facebook', 'tiktok', 'snapchat'}
FIELDS = ('id', 'pillar', 'format', 'hook', 'grounding', 'goal')


def read_required(path: Path) -> str:
    try:
        text = path.read_text(encoding='utf-8')
    except (OSError, UnicodeError):
        raise ValueError(f'Missing or unreadable required file: {path.name}') from None
    if not text.strip():
        raise ValueError(f'Empty required file: {path.name}')
    if len(text.encode('utf-8')) > 2_000_000:
        raise ValueError(f'Input too large: {path.name}')
    return text


def iso_date(value: str) -> dt.date:
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise ValueError('Expected date YYYY-MM-DD')
    return dt.date.fromisoformat(value)


def nonempty(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key')
        result[key] = value
    return result


def load_json(path: Path):
    try:
        return json.loads(read_required(path), object_pairs_hook=unique_object,
                          parse_constant=lambda _: (_ for _ in ()).throw(ValueError('Nonfinite JSON number')))
    except json.JSONDecodeError:
        raise ValueError(f'Invalid JSON: {path.name}') from None


# Field/type contracts are intentionally small and executable without a schema library.
SCHEMAS = {
    'ideas': {key: str for key in FIELDS},
    'publications': {key: str for key in ('id','date','channel','status','url','verified_by','verified_on','verification_source')},
    'runs': {key: str for key in ('run_id','date','idea_id','channel','status')},
    'profiles': {**{key: str for key in ('id','hook','caption','subject','audience','asset_group','verification_required')}, 'shots':list, 'stories':list},
    'performance': {**{key: str for key in ('idea_id','publication_url','channel','metric','measured_on','source')},
                    **{key: int for key in ('numerator','denominator','window_days')}},
}


def load_collection(path: Path, key: str) -> list:
    obj = load_json(path)
    if not isinstance(obj, dict) or obj.get('schema_version') != 1 or type(obj.get('schema_version')) is not int:
        raise ValueError(f'Unsupported schema: {path.name}')
    rows = obj.get(key)
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError(f'Invalid {key} collection')
    schema = SCHEMAS[key]
    for row in rows:
        if row.keys() != schema.keys() or any(type(row[field]) is not kind for field,kind in schema.items()):
            raise ValueError(f'Invalid fields/types in {key}')
        if any(not value.strip() for value in row.values() if isinstance(value,str)):
            raise ValueError(f'Empty field in {key}')
    return rows


def validate_ideas(ideas: list[dict]) -> list[dict]:
    if not isinstance(ideas, list) or not all(isinstance(x, dict) and nonempty(x.get('id')) for x in ideas):
        raise ValueError('Ideas must have string IDs')
    if not ideas or len({x['id'] for x in ideas}) != len(ideas):
        raise ValueError('Backlog empty or duplicate idea IDs')
    for row in ideas:
        if any(not nonempty(row.get(f)) for f in FIELDS):
            raise ValueError('Incomplete idea')
        if not re.fullmatch(r'C\d{3}', row['id']) or row['goal'] not in GOALS:
            raise ValueError('Invalid idea ID or goal')
    return ideas


def parse_backlog(markdown: str) -> list[dict]:
    """Legacy six-column table, accepting whitespace and escaped literal pipes."""
    rows = []
    for line in markdown.splitlines():
        if not re.match(r'^\s*\|\s*C\d', line):
            continue
        cells = [s.strip().replace(r'\|', '|') for s in re.split(r'(?<!\\)\|', line.strip().strip('|'))]
        if len(cells) != len(FIELDS):
            raise ValueError('Malformed content backlog row')
        rows.append(dict(zip(FIELDS, cells)))
    return validate_ideas(rows)


def load_ideas(path: Path) -> list[dict]:
    if path.suffix == '.md':
        return parse_backlog(read_required(path))
    return validate_ideas(load_collection(path, 'ideas'))


def publication_url(url: str, channel: str | None = None) -> bool:
    if not isinstance(url, str):
        return False
    try:
        parsed = urlsplit(url)
        domains = {'instagram': ('instagram.com',), 'facebook': ('facebook.com', 'fb.watch'),
                   'tiktok': ('tiktok.com',), 'snapchat': ('snapchat.com',)}
        allowed = domains.get(channel, sum(domains.values(), ()))
        host = parsed.hostname or ''
        if parsed.scheme != 'https' or parsed.username or parsed.password or parsed.query or parsed.fragment:
            return False
        if parsed.port or not any(host == d or host.endswith('.' + d) for d in allowed):
            return False
        # A profile/homepage is not post evidence. No live verification is implied.
        return bool(re.fullmatch(r'/(?:p|reel|reels|posts|stories|story|spotlight)/[^/\s]+/?', parsed.path)
                    or re.fullmatch(r'/@[^/\s]+/video/\d+/?', parsed.path)
                    or (host == 'fb.watch' and re.fullmatch(r'/[^/\s]+/?', parsed.path)))
    except ValueError:
        return False


def confirmed_publications(markdown: str) -> list[dict]:
    """Legacy compatibility. Never borrow evidence from a following heading."""
    found = []
    if not re.search(r'(?m)^###\s+', markdown) and '_No content entries recorded yet in Marketing OS v1._' not in markdown:
        raise ValueError('Unrecognized or incomplete legacy publication log')
    blocks = re.split(r'(?m)^###\s+', markdown)[1:]
    for block in blocks:
        title, _, body = block.partition('\n')
        if 'YYYY-MM-DD' in title:  # preserved historical template
            continue
        status = re.search(r'(?im)^\*\*Status:\*\*\s*([^\n]+)', body)
        if not status:
            raise ValueError('Legacy publication entry missing status')
        status = status.group(1).strip().lower()
        if status in {'scheduled', 'cancelled', 'draft'}:
            continue
        if status != 'published':
            raise ValueError('Unknown legacy publication status')
        marker = re.fullmatch(r'(\d{4}-\d{2}-\d{2})\s+[—-]\s+(?:CONTENT-)?(C\d{3})\s*', title)
        url = re.search(r'(?im)^\*\*(?:Post URL|Publication URL):\*\*\s*(\S+)', body)
        if not marker or not url or not publication_url(url.group(1)):
            raise ValueError('Published legacy entry lacks valid date, ID or post URL')
        iso_date(marker.group(1))
        found.append({'date': marker.group(1), 'id': marker.group(2), 'url': url.group(1),
                      'verification': 'legacy_recorded_url_not_live_checked'})
    return sorted(found, key=lambda r: (r['date'], r['id']), reverse=True)


def load_publications(path: Path, legacy: Path, ideas: list[dict], today: str) -> list[dict]:
    rows = load_collection(path, 'publications')
    known = {x['id'] for x in ideas}
    urls = set()
    for row in rows:
        if not nonempty(row.get('id')) or not nonempty(row.get('channel')):
            raise ValueError('Publication ID/channel must be strings')
        if row.get('status') != 'published' or row.get('channel') not in CHANNELS:
            raise ValueError('Invalid publication status/channel')
        if not publication_url(row.get('url'), row['channel']):
            raise ValueError('Publication requires canonical platform post URL')
        for field in ('verified_by', 'verification_source'):
            if not nonempty(row.get(field)):
                raise ValueError('Publication missing verification evidence')
        if iso_date(row.get('verified_on')) < iso_date(row.get('date')) or row['verified_on'] > today:
            raise ValueError('Invalid publication verification date')
    # Keep consulting legacy logs; migration must not resurrect published ideas.
    combined = rows + confirmed_publications(read_required(legacy))
    result = []
    for row in combined:
        if row.get('id') not in known or iso_date(row.get('date')) > iso_date(today):
            raise ValueError('Publication has unknown idea or future date')
        if row['url'] in urls:
            raise ValueError('Duplicate publication URL across records')
        urls.add(row['url'])
        result.append(row)
    return sorted(result, key=lambda r: (r['date'], r['id']), reverse=True)


def load_runs(path: Path, ideas: list[dict], today: str) -> list[dict]:
    rows = load_collection(path, 'runs')
    ids = set()
    for row in rows:
        if not nonempty(row.get('idea_id')) or not nonempty(row.get('channel')) or not nonempty(row.get('status')):
            raise ValueError('Draft identifiers/status must be strings')
        if row.get('idea_id') not in {x['id'] for x in ideas} or row.get('channel') not in CHANNELS:
            raise ValueError('Invalid draft idea/channel')
        if row.get('status') not in {'reserved', 'released'} or not nonempty(row.get('run_id')):
            raise ValueError('Invalid draft status/run ID')
        if row['run_id'] in ids or iso_date(row.get('date')) > iso_date(today):
            raise ValueError('Duplicate run or future draft date')
        ids.add(row['run_id'])
    return rows


def load_performance(path: Path, published: list[dict], today: str) -> list[dict]:
    rows = load_collection(path, 'performance')
    by_url = {r['url']: r for r in published}
    seen = set()
    for row in rows:
        if any(not nonempty(row.get(k)) for k in ('publication_url', 'idea_id', 'channel', 'metric')):
            raise ValueError('Performance identifiers must be strings')
        post = by_url.get(row['publication_url'])
        if not post or post['id'] != row.get('idea_id') or row.get('channel') not in CHANNELS:
            raise ValueError('Performance must reference recorded publication')
        if not publication_url(post['url'], row['channel']):
            raise ValueError('Performance channel differs from publication')
        if row.get('metric') not in {'saves_per_reach', 'landing_visits_per_reach'}:
            raise ValueError('Unsupported comparable performance metric')
        if type(row.get('numerator')) is not int or type(row.get('denominator')) is not int:
            raise ValueError('Performance counts must be integers')
        if not 0 <= row['numerator'] <= row['denominator'] or row['denominator'] <= 0:
            raise ValueError('Invalid performance denominator/count')
        if row.get('window_days') != 7 or not nonempty(row.get('source')):
            raise ValueError('Performance requires source and seven-day window')
        measured = iso_date(row.get('measured_on'))
        if measured < iso_date(post['date']) + dt.timedelta(days=7) or measured > iso_date(today):
            raise ValueError('Invalid performance measurement date')
        identity = (row['publication_url'], row['metric'])
        if identity in seen:
            raise ValueError('Duplicate performance observation')
        seen.add(identity)
    return rows
