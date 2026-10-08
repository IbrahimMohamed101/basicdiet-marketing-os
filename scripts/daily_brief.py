#!/usr/bin/env python3
"""Basic Diet daily draft, deterministic by input; no social platform integrations."""
from __future__ import annotations
import argparse
from contextlib import contextmanager
import datetime as dt
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.records import (CHANNELS, GOALS as IDEA_GOALS, confirmed_publications,
    iso_date, load_collection, load_ideas, load_performance, load_publications,
    load_runs, nonempty, parse_backlog, read_required)
from scripts.provider import ai_suggestions

IDEAS = ROOT / 'content/ideas/backlog.json'
PUBLISHED = ROOT / 'content/published/content-log.md'
PUBLICATIONS = ROOT / 'content/published/publications.json'
RUNS = ROOT / 'content/drafts/runs.json'
PERFORMANCE = ROOT / 'data/analytics/creative-performance.json'
PROFILES = ROOT / 'content/ideas/creative.json'
PREFERRED = ['C003', 'C006', 'C016', 'C001', 'C011', 'C020', 'C019']
GOALS = {x.lower() for x in IDEA_GOALS} | {'auto'}
CONTEXT = ['AGENTS.md', 'STATE.md', '.agents/skills/basic-diet-marketing/SKILL.md',
           'content/strategy.md', 'content/winners.md', 'knowledge/brand.md',
           'knowledge/product-marketing.md', 'knowledge/positioning-messaging.md',
           'knowledge/audience-voc.md', 'knowledge/voc-findings.md',
           'knowledge/offers-pricing.md', 'assets/catalog.md',
           'data/analytics/measurement-framework.md', '.agents/product-marketing.md']
KPI = {'Awareness': ('Reach', 'Unique accounts reached, seven days after publication; diagnostic only'),
       'Consideration': ('Tracked menu visits', 'Unique visits from the approved tagged link over seven days; unavailable until tracking is verified'),
       'Trust': ('Saves', 'Platform saves over seven days; not proof of subscriptions'),
       'Conversion': ('First-time paid subscribers', 'First-ever paid subscriptions attributed to this creative over seven days; unavailable without reconciled attribution'),
       'Engagement': ('Story poll votes', 'Platform poll votes within 24 hours; no inference about purchase intent')}


def saudi_today(now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    if now.tzinfo is None:
        raise ValueError('Clock requires timezone-aware datetime')
    return now.astimezone(ZoneInfo('Asia/Riyadh')).date().isoformat()


def select_idea(ideas, published, requested, goal, runs=(), performance=(), channel='instagram'):
    if goal not in GOALS or channel not in CHANNELS:
        raise ValueError('Invalid goal/channel')
    used = {x['id'] for x in published}
    reserved = {x['idea_id'] for x in runs if x['status'] == 'reserved'}
    if requested:
        selected = next((x for x in ideas if x['id'] == requested), None)
        if not selected:
            raise ValueError(f'Unknown idea: {requested}')
        if requested in used:
            raise ValueError(f'Idea already published: {requested}')
        if requested in reserved:
            raise ValueError(f'Idea already reserved in a draft: {requested}')
        if goal != 'auto' and selected['goal'].lower() != goal:
            raise ValueError('Requested idea conflicts with goal')
        return selected
    candidates = [x for x in ideas if x['id'] not in used | reserved
                  and (goal == 'auto' or x['goal'].lower() == goal)]
    if not candidates:
        raise ValueError('No available unused idea; review draft reservations or add ideas')
    recent = {x['id'] for x in published[:3]}
    recent_pillars = {x['pillar'] for x in ideas if x['id'] in recent}
    # Comparable, same-channel 7-day observations only. This is a tie-break hypothesis,
    # never a statistical winner or commercial attribution claim.
    by_id = {x['id']: x for x in ideas}
    scores = {}
    for row in performance:
        if row['channel'] != channel:
            continue
        prior = by_id[row['idea_id']]
        expected = 'landing_visits_per_reach' if prior['goal'] in {'Consideration', 'Conversion'} else 'saves_per_reach'
        if row['metric'] != expected:
            continue
        key = (prior['goal'], prior['pillar'])
        scores.setdefault(key, []).append(row['numerator'] / row['denominator'])
    priority = {x: i for i, x in enumerate(PREFERRED)}
    baseline = min(candidates, key=lambda x: (x['pillar'] in recent_pillars, priority.get(x['id'],1000), x['id']))
    comparison_goal = baseline['goal'] if goal == 'auto' else goal.title()
    def rank(idea):
        rates = scores.get((idea['goal'], idea['pillar']), [])
        signal = sum(rates) / len(rates) if len(rates) >= 2 else 0
        return (idea['pillar'] in recent_pillars, idea['goal'] != comparison_goal, -signal, priority.get(idea['id'], 1000), idea['id'])
    return sorted(candidates, key=rank)[0]


def profiles_for(ideas):
    profiles = load_collection(PROFILES, 'profiles')
    if not all(nonempty(p.get('id')) for p in profiles):
        raise ValueError('Creative profile IDs must be strings')
    mapping = {p['id']: p for p in profiles}
    if len(mapping) != len(profiles) or not {i['id'] for i in ideas} <= mapping.keys():
        raise ValueError('Missing/duplicate creative profile')
    for p in profiles:
        if any(not nonempty(p.get(f)) for f in ('hook','caption','audience','subject','asset_group','verification_required')):
            raise ValueError('Incomplete creative profile')
        if any(not isinstance(p.get(key), list) or len(p[key]) < 3 or not all(nonempty(s) for s in p[key]) for key in ('shots','stories')):
            raise ValueError('Creative profile needs at least three scenes/cards')
    return mapping


def make_packet(idea, channel, today, published_count, profile=None):
    profile = profile or profiles_for([idea])[idea['id']]
    kind = idea['format']
    adapted = kind
    if channel in {'tiktok','snapchat'} and 'Reel' not in kind and 'Stor' not in kind:
        adapted = 'Vertical sequence adapted from ' + kind
    elif channel == 'tiktok' and kind == 'Reel':
        adapted = 'Short vertical video'
    elif channel == 'snapchat' and kind == 'Reel':
        adapted = 'Vertical Story sequence'
    cta = 'شوف تفاصيل الخيارات من القناة الرسمية لـ Basic Diet.'
    if idea['goal'] == 'Engagement':
        cta = 'شاركنا اختيارك في التصويت.'
    funnel = {'Awareness':'Awareness', 'Consideration':'Consideration', 'Trust':'Consideration',
              'Conversion':'Decision', 'Engagement':'Engagement'}[idea['goal']]
    kpi, definition = KPI[idea['goal']]
    creative = {
        'hook':profile['hook'], 'format':adapted,
        'direction':'\n'.join(profile['shots']), 'caption_draft':profile['caption']+'\n\n'+cta+'\n#BasicDiet',
        'cta':cta, 'destination_url':None,
        'story': '\n'.join(f'{i}. {story}' for i, story in enumerate(profile['stories'],1)),
        'asset': {'catalog':'assets/catalog.md', 'suggested_group':profile['asset_group'],
                  'subject':profile['subject'], 'verified_file_id':None, 'rights_verified':False,
                  'status':'UNVERIFIED_CATALOG_REFERENCE', 'required':profile['verification_required']},
        'kpi': kpi, 'kpi_definition':definition,
        'paid_suitability':'NOT_READY: concept may be evaluated after organic results, approved media rights, offer economics and paid attribution; no budget proposed',
    }
    return {'schema_version':1, 'status':'DRAFT_REVIEW_REQUIRED', 'date':today, 'timezone':'Asia/Riyadh',
            'channel':channel, 'idea':idea, 'objective':idea['goal'], 'audience':profile['audience'],
            'audience_evidence':'Hypothesis from knowledge/audience-voc.md (2026-10-07)',
            'funnel_stage':funnel, 'confirmed_published_count':published_count, 'creative':creative,
            'live_facts_verified':False, 'ai':{'status':'disabled'},
            'checks': ['Verify actual platform history; missing records do not prove an idea was never posted',
                       'Verify exact source asset, rights and current menu before production',
                       'Verify any price, promotion, nutrition, fulfillment or testimonial independently',
                       'Approve final Arabic copy, crop and official destination URL',
                       'Obtain action-specific approval for asset generation, posting, messages or ad spend',
                       'NO publishing, scheduling, spending or production changes performed'],
            'sources':[], 'agents':[]}


def handoffs(packet):
    return [
        {'role':'research','skills':['customer-research'], 'inputs':['sources','idea.grounding'],
         'outputs':['audience_evidence','live_facts_verified'], 'status':'historical_context_only'},
        {'role':'strategy','skills':['content-strategy'], 'inputs':['idea','selection'],
         'outputs':['objective','audience','funnel_stage'], 'status':'proposal'},
        {'role':'creative','skills':['social','video'] if 'Reel' in packet['idea']['format'] else ['social'],
         'inputs':['audience','idea','sources'], 'outputs':['creative'], 'status':'draft'},
        {'role':'analytics','skills':['analytics','attribution'], 'inputs':['objective','performance'],
         'outputs':['creative.kpi','creative.kpi_definition'], 'status':'measurement_proposed'},
        {'role':'media-buyer','skills':['ads','ad-creative'], 'inputs':['creative','live_facts_verified'],
         'outputs':['creative.paid_suitability'], 'status':'blocked_pending_evidence_and_approval'},
        {'role':'operations','skills':[], 'inputs':['checks','agents'],
         'outputs':['status','run_id'], 'status':'review_required'},
    ]


def validate_packet(packet):
    if packet.get('status') != 'DRAFT_REVIEW_REQUIRED' or packet.get('live_facts_verified') is not False:
        raise ValueError('Unsafe packet status')
    if packet.get('timezone') != 'Asia/Riyadh' or packet.get('channel') not in CHANNELS:
        raise ValueError('Invalid packet channel/timezone')
    iso_date(packet.get('date'))
    for key in ('objective','audience','funnel_stage','run_id'):
        if not nonempty(packet.get(key)):
            raise ValueError('Incomplete packet')
    for key in ('hook','format','direction','caption_draft','cta','story','kpi','kpi_definition','paid_suitability'):
        if not nonempty(packet['creative'].get(key)):
            raise ValueError('Incomplete creative')
    if len(packet['agents']) != 6 or not packet['sources'] or not packet['checks']:
        raise ValueError('Incomplete provenance/handoffs')


def to_markdown(packet):
    c = packet['creative']
    lines = ['# Basic Diet — Daily Content Draft', '', '**STATUS: DRAFT_REVIEW_REQUIRED — NOT PUBLISHED**',
             f"Date: {packet['date']} (Asia/Riyadh) | Channel: {packet['channel']} | Idea: {packet['idea']['id']}",
             f"Objective: {packet['objective']} | Audience (hypothesis): {packet['audience']} | Funnel: {packet['funnel_stage']}",
             f"Format: {c['format']}", '', '## Creative', '', f"**Hook:** {c['hook']}", '',
             '**Scenes / cards:**', '', c['direction'], '', '**Caption:**', '', c['caption_draft'], '',
             '**Supporting Stories:**', '', c['story'], '', f"**CTA:** {c['cta']}",
             '**Destination:** UNVERIFIED — check official channel before publication',
             f"**Asset:** {c['asset']['suggested_group']} — {c['asset']['subject']}; catalog only, no verified file ID or rights",
             f"**Primary KPI:** {c['kpi']} — {c['kpi_definition']}", f"**Paid suitability:** {c['paid_suitability']}",
             '', '## Selection and evidence', '', packet.get('selection',{}).get('rationale','Historical context only'),
             f"Recorded publications: {packet['confirmed_published_count']}; live history was not checked.",
             f"AI status: {packet['ai']['status']}", '', '## Handoffs — deterministic stages, not independent agents', '']
    lines += [f"- {a['role']}: {a['status']}; skills: {', '.join(a['skills']) or 'native'}; outputs: {', '.join(a['outputs'])}" for a in packet['agents']]
    lines += ['', '## Approval checks', ''] + [f'- [ ] {s}' for s in packet['checks']]
    lines += ['', '## Sources read (hashes in JSON; historical sources are not live verification)', '']
    lines += [f"- {s['path']} ({s['classification']})" for s in packet['sources']]
    return '\n'.join(lines)+'\n'


@contextmanager
def ledger_lock(path):
    lock = path.with_suffix('.lock')
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise ValueError('Another draft run holds the ledger lock; inspect stale locks manually') from None
    try:
        os.close(descriptor)
        yield
    finally:
        lock.unlink()


def atomic_json(path, obj):
    fd, name = tempfile.mkstemp(dir=path.parent, prefix='.record-')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
            f.flush()
            os.fsync(f.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def build(args):
    today = args.as_of or saudi_today()
    if iso_date(today) > iso_date(saudi_today()):
        raise ValueError('Future as-of is not supported')
    ideas = load_ideas(IDEAS)
    if not {f'C{i:03}' for i in range(1,31)} <= {row['id'] for row in ideas}:
        raise ValueError('Backlog is missing original idea IDs')
    published = load_publications(PUBLICATIONS, PUBLISHED, ideas, today)
    runs = load_runs(RUNS, ideas, today)
    performance = load_performance(PERFORMANCE, published, today)
    cutoff = iso_date(today) - dt.timedelta(days=90)
    recent_performance = [r for r in performance if iso_date(r['measured_on']) >= cutoff]
    selected = select_idea(ideas, published, args.idea_id.strip().upper(), args.goal, runs, recent_performance, args.channel)
    packet = make_packet(selected, args.channel, today, len(published), profiles_for(ideas)[selected['id']])
    packet['selection'] = {'reserved_count':sum(r['status']=='reserved' for r in runs),
        'rationale':'Excluded published and reserved ideas across all platforms; rotate recent pillars; '
                    'use comparable same-channel performance only as a tie-break; then historical priority and ID. '
                    + ('Performance records available; no causal winner inferred.' if performance else 'No verified creative performance recorded.'),
        'requested_goal':args.goal, 'requested_id':args.idea_id}
    packet['performance'] = {'record_count':len(performance), 'recent_record_count':len(recent_performance), 'status':'available' if performance else 'missing'}
    packet['agents'] = handoffs(packet)
    paths = [ROOT/p for p in CONTEXT] + [ROOT/'scripts'/name for name in ('daily_brief.py','records.py','provider.py')] + [IDEAS, PUBLISHED, PUBLICATIONS, RUNS, PERFORMANCE, PROFILES]
    skills = sorted({s for stage in packet['agents'] for s in stage['skills']})
    paths += [ROOT/'.agents/skills'/s/'SKILL.md' for s in skills]
    for path in paths:
        text = read_required(path)
        classification = ('historical_unverified' if path.name in {'catalog.md','offers-pricing.md','product-marketing.md',
                           'audience-voc.md','voc-findings.md','positioning-messaging.md','strategy.md','backlog.json'}
                          else 'local_record_or_instructions')
        packet['sources'].append({'path':path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else path.name,
                                  'sha256':sha256(text.encode()).hexdigest(), 'classification':classification})
    digest = sha256(json.dumps(packet, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:12]
    packet['run_id'] = f"{today}-{args.channel}-{selected['id']}-{digest}"
    validate_packet(packet)
    return packet, runs


def execute(args):
    packet, runs = build(args)
    dest = Path(args.out_dir).resolve()/packet['run_id']
    if dest.exists():
        raise ValueError('Output run already exists; choose a new --out-dir to replay')
    dest.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.draft-', dir=dest.parent))
    try:
        if args.ai:
            try:
                suggestions = ai_suggestions(packet, args.model, getattr(args,'max_output_tokens',1200))
                (stage/'ai-suggestions.md').write_text(suggestions, encoding='utf-8')
                packet['ai'] = {'status':'unverified_suggestions','model':args.model}
            except ValueError as exc:
                packet['ai'] = {'status':'failed','error':str(exc)}
        validate_packet(packet)
        atomic_json(stage/'daily-brief.json', packet)
        (stage/'daily-brief.md').write_text(to_markdown(packet), encoding='utf-8')
        stage.rename(dest)
        if not getattr(args,'dry_run',False):
            runs.append({'run_id':packet['run_id'],'date':packet['date'],'idea_id':packet['idea']['id'],
                         'channel':packet['channel'],'status':'reserved'})
            # If the write fails the CLI fails, leaving an inspectable unreserved artifact.
            atomic_json(RUNS, {'schema_version':1,'runs':runs})
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    return packet


def run(args):
    # One shared lock protects selection + reservation; dry runs never change durable state.
    if getattr(args,'dry_run',False):
        return execute(args)
    with ledger_lock(RUNS):
        return execute(args)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--channel', choices=sorted(CHANNELS), default='instagram')
    p.add_argument('--goal', choices=sorted(GOALS), default='auto')
    p.add_argument('--idea-id', default='')
    p.add_argument('--as-of', default='', help='YYYY-MM-DD; defaults to Asia/Riyadh')
    p.add_argument('--out-dir', default='output/daily')
    p.add_argument('--dry-run', action='store_true', help='Do not reserve an idea in durable draft history')
    p.add_argument('--ai', action='store_true', help='Explicitly authorize one billable API request')
    p.add_argument('--model', default='gpt-5', help='Used only with --ai')
    p.add_argument('--max-output-tokens', type=int, default=1200)
    args = p.parse_args()
    try:
        packet = run(args)
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    status = 'DRAFT_ONLY_AI_FAILED' if packet['ai']['status']=='failed' else 'DRAFT_ONLY'
    print(f"{status}: {packet['idea']['id']}; {Path(args.out_dir)/packet['run_id']}")
    return 3 if packet['ai']['status']=='failed' else 0


if __name__ == '__main__':
    raise SystemExit(main())
