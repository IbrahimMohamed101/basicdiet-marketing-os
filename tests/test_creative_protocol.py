"""Safety invariants: source review, concept feasibility, measurable KPI and copy linting."""
import copy
import json
from pathlib import Path
import unittest

from scripts.validate_creative import validate_assets, validate_record, read_frontmatter, validate_production
from scripts.lint_copy import check_copy
from scripts.security import contains_credential

ROOT = Path(__file__).resolve().parents[1]


class CreativeProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT/"assets/drive-source-index.json").read_text(encoding="utf-8"))
        cls.record = read_frontmatter(ROOT/"content/production/2026-10-09-food-desire-butter-chicken.md")
        cls.asset_id = "1H2InhiMdECMrs8bsf6L_h9yM-rOfYqw6"
        cls.logo_id = "1I8-a2wQiP26JnHRblQYdM3fgE0WEQnAg"

    def test_existing_draft_is_valid_and_measurement_disconnected(self):
        idx = validate_assets(self.index)
        self.assertEqual(idx[self.asset_id]["visual_review"],"ai_reviewed")
        self.assertTrue(validate_record(self.record, idx))
        self.assertGreaterEqual(validate_production(ROOT/"content/production", idx),1)
        self.assertIsNone(self.record["primary_kpi"]["threshold"])

    def test_ai_review_cannot_impersonate_human_and_flags_need_evidence(self):
        idx=copy.deepcopy(self.index)
        asset=next(x for x in idx["candidate_files"] if x["file_id"]==self.asset_id)
        asset["visual_review"]="human_reviewed"
        with self.assertRaisesRegex(ValueError,"human_visual_verified"):
            validate_assets(idx)
        asset.update(human_visual_verified_by="Restaurant owner",human_visual_verified_on="2026-10-09",human_visual_verified_evidence="Approved original reference in owner review")
        self.assertEqual(validate_assets(idx)[self.asset_id]["visual_review"],"human_reviewed")
        asset["rights_verified"]=True
        with self.assertRaisesRegex(ValueError,"rights_verified_by"):
            validate_assets(idx)

    def test_source_dates_are_not_frozen(self):
        idx=copy.deepcopy(self.index)
        idx["checked_at"]="2026-10-07"
        self.assertGreaterEqual(len(validate_assets(idx)),20)

    def test_concept_level_feasibility_rubric(self):
        assets=validate_assets(self.index)
        m=copy.deepcopy(self.record)
        m["concepts"][0]["asset_ids"]=["file-that-was-not-indexed"]
        with self.assertRaisesRegex(ValueError,"asset_ids"):validate_record(m,assets)
        m=copy.deepcopy(self.record)
        m["concepts"][0]["feasible_now"]=False
        m["concepts"][0]["rejected_reason"]="Need another real source to build it."
        with self.assertRaisesRegex(ValueError,"selected concept"):validate_record(m,assets)
        m=copy.deepcopy(self.record)
        m["concepts"][1]["score_breakdown"]["hook"]=8
        with self.assertRaisesRegex(ValueError,"score_breakdown"):validate_record(m,assets)

    def test_disconnected_measurement_blocks_ready(self):
        assets=validate_assets(self.index)
        m=copy.deepcopy(self.record)
        m["status"]="READY_FOR_HUMAN_APPROVAL"
        with self.assertRaisesRegex(ValueError,"metric source disconnected"):validate_record(m,assets)
        m=copy.deepcopy(self.record)
        m["primary_kpi"]["threshold"]=200
        with self.assertRaisesRegex(ValueError,"no fabricated KPI"):validate_record(m,assets)

    def test_brand_and_food_human_review_needed_for_production(self):
        idx=copy.deepcopy(self.index)
        for item in idx["candidate_files"]:
            if item["file_id"] not in (self.asset_id,self.logo_id):continue
            item.update(visual_review="human_reviewed",human_visual_verified_by="Restaurant owner",human_visual_verified_on="2026-10-09",human_visual_verified_evidence="Owner's authorized source review ID",
                        rights_verified=True,rights_verified_by="Restaurant owner",rights_verified_on="2026-10-09",rights_verified_evidence="Documented rights granted by owner")
            if item["file_id"]==self.asset_id:
                item.update(menu_verified=True,menu_verified_by="Restaurant owner",menu_verified_on="2026-10-09",menu_verified_evidence="Current menu item proof from owner")
        assets=validate_assets(idx)
        m=copy.deepcopy(self.record)
        m["status"]="READY_FOR_HUMAN_APPROVAL"
        m["primary_kpi"].update(threshold=2,baseline=1,source_status="manual_verified",evidence="Manually recorded tracked visits screenshot proof")
        with self.assertRaisesRegex(ValueError,"official logo"):validate_record(m,assets)
        m["brand_logo_asset_id"]=self.logo_id
        self.assertTrue(validate_record(m,assets))
        m["status"]="APPROVED_BY_OWNER"
        with self.assertRaisesRegex(ValueError,"owner approval"):validate_record(m,assets)
        m["approvals"]=[{"by":"Restaurant owner","date":"2026-10-09","evidence":"Confirmed external review reference"}]
        self.assertTrue(validate_record(m,assets))
        m["status"]="PRODUCED";m["generated_asset_url"]="https://example.com/approved.mp4"
        self.assertTrue(validate_record(m,assets))
        m["status"]="PUBLISHED_VERIFIED"
        with self.assertRaisesRegex(ValueError,"canonical verified post URL"):validate_record(m,assets)
        m["publication"]={"url":"https://www.instagram.com/p/test-post/","verified_by":"Operator","verified_on":"2026-10-09"}
        self.assertTrue(validate_record(m,assets))

    def test_linter_catches_unverified_health_claims(self):
        m=copy.deepcopy(self.record)
        m["copy"]["caption"]+=" #وجبات_صحية"
        with self.assertRaisesRegex(ValueError,"blocked creative claim"):check_copy(m)
        with self.assertRaisesRegex(ValueError,"blocked creative claim"):validate_record(m,validate_assets(self.index))

    def test_more_credential_shapes(self):
        self.assertTrue(contains_credential("AIza"+"a"*35))
        self.assertTrue(contains_credential("sk_live_"+"a"*24))
        self.assertTrue(contains_credential("EAA"+"B"*48))
        self.assertFalse(contains_credential("The private secret is stored elsewhere."))

if __name__=="__main__":
    unittest.main()
