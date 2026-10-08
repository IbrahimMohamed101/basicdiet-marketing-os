import argparse
import copy
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from contextlib import ExitStack

from scripts import daily_brief as d
from scripts import records as r
from scripts.migrate_backlog import migrate

SAMPLE = '''# Ideas
| ID | Pillar | Format | Hook | Grounding | Primary goal |
|---|---|---|---|---|---|
|C001|Food Desire|Reel|كبسة|Asset|Awareness|
| C003 | Food Desire | Reel | تنوع | Menu | Awareness |
| C006 | Education | Carousel | أحجام الوجبات | Portions | Consideration |
| C016 | Trust | Reel | من المطبخ | Prep assets | Trust |
'''


def publication(idea='C003'):
    return {'id':idea,'date':'2026-09-01','channel':'instagram','status':'published',
            'url':f'https://www.instagram.com/reel/{idea}/', 'verified_by':'operations reviewer',
            'verified_on':'2026-09-02','verification_source':'authorized platform inspection'}


class DailyBriefTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.stack=ExitStack()
        self.addCleanup(self.stack.close)
        for name in ('IDEAS','PUBLICATIONS','PUBLISHED','RUNS','PERFORMANCE'):
            original=getattr(d,name)
            local=self.root/original.name
            local.write_bytes(original.read_bytes())
            self.stack.enter_context(patch.object(d,name,local))
        self.ideas=r.load_ideas(d.IDEAS)
        self.write(d.PUBLICATIONS,'publications',[])
        self.write(d.RUNS,'runs',[])
        self.write(d.PERFORMANCE,'performance',[])
        d.PUBLISHED.write_text('# Content Log\n_No content entries recorded yet in Marketing OS v1._\n')
        self.args=argparse.Namespace(as_of='2026-10-08', channel='instagram',goal='auto',idea_id='',
            out_dir=str(self.root/'out'),ai=False,model='gpt-5',max_output_tokens=1200,dry_run=False)
        self.stack.enter_context(patch.object(d,'saudi_today',return_value='2026-10-08'))

    def write(self,path,key,rows):
        path.write_text(json.dumps({'schema_version':1,key:rows},ensure_ascii=False))

    def test_priority_and_goal(self):
        self.assertEqual(d.select_idea(self.ideas,[],'','auto')['id'],'C003')
        self.assertEqual(d.select_idea(self.ideas,[],'','trust')['id'],'C016')

    def test_legacy_parser_whitespace_escaped_pipe(self):
        rows=r.parse_backlog(SAMPLE.replace('تنوع',r'تنوع \| أكل'))
        self.assertEqual(rows[1]['hook'],'تنوع | أكل')

    def test_legacy_parser_rejects_damaged_duplicate_empty(self):
        for value in ('', SAMPLE+'| C003 | bad |', SAMPLE+SAMPLE, SAMPLE.replace('Awareness','Unknown')):
            with self.subTest(value=value[-30:]),self.assertRaises(ValueError):
                r.parse_backlog(value)

    def test_migration_preserves_all_30_and_no_overwrite(self):
        dest=self.root/'migrated.json'
        source=d.ROOT/'content/ideas/backlog.md'
        rows=migrate(source,dest)
        self.assertEqual(len(rows),30)
        self.assertEqual(rows,self.ideas)
        with self.assertRaises(FileExistsError):migrate(source,dest)

    def test_publication_excluded_on_every_channel(self):
        self.write(d.PUBLICATIONS,'publications',[publication()])
        for channel in sorted(d.CHANNELS):
            self.args.channel=channel
            packet,_=d.build(self.args)
            self.assertNotEqual(packet['idea']['id'],'C003')
            self.assertEqual(packet['confirmed_published_count'],1)

    def test_publication_proof_missing_invalid_future_unknown(self):
        for key,value in [('url','https://example.org/post/1'),('url','https://instagram.com/profile'),
                          ('verified_by',''),('verified_on','2026-09-00'),('date','2027-01-01'),
                          ('status','scheduled'),('id','C999'),('url','https://instagram.com.evil.com/reel/1/')]:
            row=publication();row[key]=value
            self.write(d.PUBLICATIONS,'publications',[row])
            with self.subTest(key=key,value=value),self.assertRaises(ValueError):d.run(self.args)
            self.assertFalse((self.root/'out').exists())

    def test_legacy_evidence_never_bleeds_into_next_heading(self):
        log='''### 2026-09-01 — CONTENT-C003
**Status:** Published
### Unknown heading
**Status:** Published
**Post URL:** https://instagram.com/reel/abc/
'''
        with self.assertRaisesRegex(ValueError,'lacks valid'):r.confirmed_publications(log)

    def test_legacy_valid_scheduled_and_corrupt_published(self):
        good='''### 2026-09-01 — CONTENT-C003
**Status:** Published
**Post URL:** https://instagram.com/reel/abc/
### 2026-09-02 — CONTENT-C006
**Status:** Scheduled
'''
        self.assertEqual([x['id'] for x in r.confirmed_publications(good)],['C003'])
        with self.assertRaises(ValueError):r.confirmed_publications(good.replace('https://instagram.com/reel/abc/',''))

    def test_legacy_log_is_still_consulted(self):
        d.PUBLISHED.write_text('### 2026-09-01 — CONTENT-C003\n**Status:** Published\n**Post URL:** https://instagram.com/reel/abc/\n')
        self.assertEqual(d.build(self.args)[0]['idea']['id'],'C006')

    def test_requested_used_unknown_conflicting_goal_exhausted(self):
        for args in [(self.ideas,[publication()],'C003','auto'),(self.ideas,[],'C999','auto'),
                     (self.ideas,[],'C003','conversion'),(self.ideas,[{'id':x['id']} for x in self.ideas],'','auto')]:
            with self.subTest(args=args[2:]),self.assertRaises(ValueError):d.select_idea(*args)

    def test_run_reserves_idea_next_run_avoids_duplicate(self):
        with patch.object(d,'ai_suggestions',side_effect=AssertionError('Network forbidden')):
            first=d.run(self.args);second=d.run(self.args)
        self.assertEqual(first['idea']['id'],'C003')
        self.assertNotEqual(first['idea']['id'],second['idea']['id'])
        self.assertEqual(len(r.load_collection(d.RUNS,'runs')),2)
        self.assertEqual(r.load_collection(d.PUBLICATIONS,'publications'),[])

    def test_reservation_release_does_not_release_publication(self):
        self.write(d.RUNS,'runs',[{'run_id':'old','date':'2026-09-01','idea_id':'C003','channel':'instagram','status':'released'}])
        self.assertEqual(d.build(self.args)[0]['idea']['id'],'C003')
        self.write(d.PUBLICATIONS,'publications',[publication()])
        self.assertNotEqual(d.build(self.args)[0]['idea']['id'],'C003')

    def test_concurrent_run_is_rejected_before_network(self):
        with d.ledger_lock(d.RUNS),self.assertRaisesRegex(ValueError,'lock'):
            d.run(self.args)
        self.assertFalse(d.RUNS.with_suffix('.lock').exists())

    def test_dry_run_is_deterministic_no_api_no_reservation(self):
        self.args.dry_run=True
        before=d.RUNS.read_bytes()
        with patch.object(d,'ai_suggestions',side_effect=AssertionError('Unexpected AI')):
            one=d.run(self.args)
            self.args.out_dir=str(self.root/'second')
            two=d.run(self.args)
        self.assertEqual(one,two)
        self.assertEqual(d.RUNS.read_bytes(),before)
        self.assertEqual(one['status'],'DRAFT_REVIEW_REQUIRED')
        self.assertFalse(one['live_facts_verified'])
        self.assertIsNone(one['creative']['asset']['verified_file_id'])
        self.assertEqual(len(one['agents']),6)
        self.assertTrue(all(len(x['sha256'])==64 for x in one['sources']))

    def test_output_replay_does_not_overwrite(self):
        self.args.dry_run=True
        d.run(self.args)
        with self.assertRaisesRegex(ValueError,'already exists'):d.run(self.args)

    def test_all_profiles_have_specific_creative_in_all_channels(self):
        profiles=d.profiles_for(self.ideas)
        captions=set()
        for idea in self.ideas:
            captions.add(profiles[idea['id']]['caption'])
            for channel in d.CHANNELS:
                packet=d.make_packet(idea,channel,'2026-10-08',0,profiles[idea['id']])
                self.assertGreaterEqual(len(packet['creative']['direction'].splitlines()),3)
                self.assertNotEqual(packet['creative']['hook'],idea['hook'])
                self.assertTrue(packet['audience'])
                for old in ('KSA96','BASIC15','48g','مفيهوش','شوف ده'):
                    self.assertNotIn(old,packet['creative']['caption_draft'])
        self.assertGreaterEqual(len(captions),30)

    def test_invalid_or_missing_inputs_no_output_or_false_success(self):
        for content in ('','{','{"schema_version":2,"ideas":[]}', '{"schema_version":1,"ideas":[],"ideas":[]}',
                        '{"schema_version":1,"ideas":[null]}'):
            d.IDEAS.write_text(content)
            with self.subTest(content=content),self.assertRaises(ValueError):d.run(self.args)
        d.IDEAS.unlink()
        with self.assertRaises(ValueError):d.run(self.args)
        self.assertFalse((self.root/'out').exists())

    def test_missing_context_fails_before_api_or_artifact(self):
        with patch.object(d,'CONTEXT',['missing-state.md']),patch.object(d,'ai_suggestions') as api:
            with self.assertRaises(ValueError):d.run(self.args)
            api.assert_not_called()
        self.assertFalse((self.root/'out').exists())

    def test_corrupt_history_and_performance_fail_closed(self):
        for path in (d.RUNS,d.PUBLICATIONS,d.PERFORMANCE):
            original=path.read_bytes();path.write_text('not json')
            with self.subTest(path=path.name),self.assertRaises(ValueError):d.run(self.args)
            path.write_bytes(original)

    def test_future_noncanonical_invalid_date(self):
        for date in ('2026-02-30','20261008','2026-10-09','bad'):
            self.args.as_of=date
            with self.subTest(date=date),self.assertRaises(ValueError):d.run(self.args)

    def test_optional_ai_failure_preserves_manual_draft_and_status(self):
        self.args.ai=True
        with patch.object(d,'ai_suggestions',side_effect=ValueError('Provider unavailable')):
            packet=d.run(self.args)
        output=Path(self.args.out_dir)/packet['run_id']
        self.assertEqual(packet['ai']['status'],'failed')
        self.assertTrue((output/'daily-brief.md').is_file())
        self.assertFalse((output/'ai-suggestions.md').exists())
        self.assertEqual(json.loads((output/'daily-brief.json').read_text())['ai']['status'],'failed')

    def test_ai_output_is_separate(self):
        self.args.ai=True
        with patch.object(d,'ai_suggestions',return_value='UNVERIFIED suggestion'):
            packet=d.run(self.args)
        output=Path(self.args.out_dir)/packet['run_id']
        self.assertEqual((output/'ai-suggestions.md').read_text(),'UNVERIFIED suggestion')
        self.assertNotIn('UNVERIFIED suggestion',(output/'daily-brief.md').read_text())

    def test_performance_requires_real_record_and_valid_denominator(self):
        row={'idea_id':'C003','publication_url':publication()['url'],'channel':'instagram',
             'metric':'saves_per_reach','numerator':10,'denominator':100,'window_days':7,
             'measured_on':'2026-09-09','source':'sanitized authorized platform report'}
        self.write(d.PERFORMANCE,'performance',[row])
        with self.assertRaises(ValueError):d.build(self.args)
        self.write(d.PUBLICATIONS,'publications',[publication()])
        self.assertEqual(d.build(self.args)[0]['performance']['record_count'],1)
        for field,value in [('denominator',0),('numerator',True),('metric','revenue'),('measured_on','2026-09-02')]:
            bad=copy.deepcopy(row);bad[field]=value;self.write(d.PERFORMANCE,'performance',[bad])
            with self.subTest(field=field),self.assertRaises(ValueError):d.build(self.args)

    def test_performance_changes_tiebreak_only_for_comparable_channel(self):
        perf=[{'idea_id':i,'channel':'instagram','metric':'saves_per_reach','numerator':20,'denominator':100}
              for i in ('C011','C012')]
        # Records already schema-validated by build; unit test isolates deterministic rank.
        self.assertEqual(d.select_idea(self.ideas,[],'','awareness',performance=perf)['id'],'C011')
        self.assertEqual(d.select_idea(self.ideas,[],'','awareness',performance=perf,channel='tiktok')['id'],'C003')

    def test_cli_has_no_publish_or_spend_options(self):
        proc=subprocess.run([sys.executable,str(d.ROOT/'scripts/daily_brief.py'),'--publish'],capture_output=True,text=True)
        self.assertEqual(proc.returncode,2)
        self.assertIn('unrecognized arguments',proc.stderr)

    def test_record_field_type_corruption_fails_with_clear_error(self):
        cases = [(d.IDEAS,'ideas',self.ideas[0],'id',[]),
                 (d.PUBLICATIONS,'publications',publication(),'channel',{}),
                 (d.RUNS,'runs',{'run_id':'r','date':'2026-10-08','idea_id':'C003','channel':'instagram','status':'reserved'},'status',[])]
        for path,key,row,field,value in cases:
            original=path.read_bytes();bad=copy.deepcopy(row);bad[field]=value
            self.write(path,key,[bad])
            with self.subTest(field=field),self.assertRaisesRegex(ValueError,'fields/types'):d.build(self.args)
            path.write_bytes(original)

    def test_partial_but_valid_json_cannot_drop_original_ideas(self):
        self.write(d.IDEAS,'ideas',self.ideas[:2])
        with self.assertRaisesRegex(ValueError,'missing original'):d.run(self.args)
        self.assertFalse((self.root/'out').exists())

    def test_unrecognizable_legacy_log_fails_closed(self):
        for text in ('garbled history','# Content Log\n', '### 2026-10-08 — CONTENT-C003\n'):
            d.PUBLISHED.write_text(text)
            with self.assertRaises(ValueError):d.run(self.args)

    def test_cli_ai_failure_returns_partial_status_code(self):
        import os
        self.args.ai=True
        self.args.dry_run=True
        with patch.dict(os.environ,{},clear=True), patch.object(d.argparse.ArgumentParser,'parse_args',return_value=self.args):
            self.assertEqual(d.main(),3)
        self.assertTrue(list((self.root/'out').glob('*/daily-brief.md')))


class DateTests(unittest.TestCase):
    def test_saudi_day_boundary(self):
        self.assertEqual(d.saudi_today(dt.datetime(2026,10,7,21,1,tzinfo=dt.timezone.utc)),'2026-10-08')
        self.assertEqual(d.saudi_today(dt.datetime(2026,10,7,20,59,tzinfo=dt.timezone.utc)),'2026-10-07')

    def test_naive_clock_rejected(self):
        with self.assertRaises(ValueError):d.saudi_today(dt.datetime(2026,10,8))


if __name__=='__main__':unittest.main()
