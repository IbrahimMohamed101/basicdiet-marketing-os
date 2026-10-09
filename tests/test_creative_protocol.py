"""Behavioral tests: evidence transitions and record invariants, not frozen dates/false flags."""
import copy
import json
from pathlib import Path
import unittest

from scripts.validate_creative import validate_assets, validate_record, read_frontmatter, validate_production

ROOT=Path(__file__).resolve().parents[1]

class CreativeProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original=json.loads((ROOT/"assets/drive-source-index.json").read_text(encoding="utf-8"))
        cls.record=read_frontmatter(ROOT/"content/production/2026-10-09-food-desire-butter-chicken.md")

    def test_real_index_and_current_draft_validate(self):
        assets=validate_assets(self.original)
        self.assertIn("1H2InhiMdECMrs8bsf6L_h9yM-rOfYqw6",assets)
        self.assertTrue(validate_record(self.record,assets))
        self.assertGreaterEqual(validate_production(ROOT/"content/production",assets),1)

    def test_conditional_asset_rights_allowed_with_evidence(self):
        idx=copy.deepcopy(self.original);a=idx["candidate_files"][3]
        a["rights_verified"]=True
        with self.assertRaisesRegex(ValueError,"rights_verified"):
            validate_assets(idx)
        a.update(rights_verified_by="Brand owner",rights_verified_on="2026-10-09",rights_verified_evidence="Authorized signed usage approval reference")
        self.assertTrue(validate_assets(idx)[a["file_id"]]["rights_verified"])
        a["rights_verified_on"]="2035-01-01"
        with self.assertRaises(ValueError):validate_assets(idx)

    def test_conditional_visual_verification_and_date_not_frozen(self):
        idx=copy.deepcopy(self.original)
        idx["checked_at"]="2026-10-08"
        self.assertEqual(len(validate_assets(idx)),len(idx["candidate_files"]))
        a=idx["candidate_files"][0]
        a["visual_review"]="reviewed"
        with self.assertRaises(ValueError):validate_assets(idx)
        a.update(visual_verified_by="QA reviewer",visual_verified_on="2026-10-09",visual_evidence="Evidence note in source catalog")
        self.assertIn(a["file_id"],validate_assets(idx))

    def test_three_distinct_meaningful_concept_fields(self):
        assets=validate_assets(self.original);m=copy.deepcopy(self.record)
        m["concepts"][1]["angle"]=m["concepts"][0]["angle"]
        with self.assertRaisesRegex(ValueError,"duplicate"):validate_record(m,assets)
        m=copy.deepcopy(self.record);m["concepts"][1]["visual"]=m["concepts"][0]["visual"]
        with self.assertRaisesRegex(ValueError,"duplicate"):validate_record(m,assets)
        m=copy.deepcopy(self.record);m["primary_kpi"]["threshold"]=0
        with self.assertRaisesRegex(ValueError,"KPI"):validate_record(m,assets)

    def test_cannot_approve_or_publish_without_actual_evidence(self):
        assets=validate_assets(self.original)
        for status in ("READY_FOR_HUMAN_APPROVAL","APPROVED_BY_OWNER","PRODUCED","PUBLISHED_VERIFIED"):
            m=copy.deepcopy(self.record);m["status"]=status
            with self.assertRaises(ValueError):validate_record(m,assets)
        m=copy.deepcopy(self.record);m["publication"]={"url":"https://instagram.com/p/fake","verified_by":"Operator","verified_on":"2026-10-09"}
        with self.assertRaisesRegex(ValueError,"unpublished"):validate_record(m,assets)

    def test_stage_progression_if_evidence_satisfied(self):
        idx=copy.deepcopy(self.original);item=idx["candidate_files"][3]
        item.update(rights_verified=True,rights_verified_by="Restaurant owner",rights_verified_on="2026-10-09",rights_verified_evidence="Owner's documented consent for use",menu_verified=True,menu_verified_by="Admin operator",menu_verified_on="2026-10-09",menu_verified_evidence="Current menu item detail record")
        assets=validate_assets(idx)
        m=copy.deepcopy(self.record);m["status"]="READY_FOR_HUMAN_APPROVAL"
        self.assertTrue(validate_record(m,assets))
        m["status"]="APPROVED_BY_OWNER";m["approvals"]=[{"by":"Restaurant owner","date":"2026-10-09","evidence":"Dated approval record / authorized message"}]
        self.assertTrue(validate_record(m,assets))
        m["status"]="PRODUCED";m["generated_asset_url"]="https://example.org/approved-final.mp4"
        self.assertTrue(validate_record(m,assets))
        m["status"]="PUBLISHED_VERIFIED";m["publication"]={"url":"https://www.instagram.com/p/EXAMPLE/","verified_by":"Social operator","verified_on":"2026-10-09"}
        self.assertTrue(validate_record(m,assets))

if __name__=="__main__":
    unittest.main()
