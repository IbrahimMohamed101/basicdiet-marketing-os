"""No-network checks for automation stage audit fail-closed behavior."""
import tempfile
import unittest
from pathlib import Path

from scripts.check_scheduled_pipeline import check_date

DAY = "2026-10-13"
FILES = ["01-ideas.md", "02-critique.md", "03-approved-brief.md",
         "04-draft-images.md", "05-final-review.md"]


class PipelineAuditTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.stage_dir = self.root / "automation" / "daily" / DAY
        self.stage_dir.mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def write_handoffs(self):
        for index, filename in enumerate(FILES, 1):
            number = f"{index:02}"
            status = "NEEDS_USER_REVIEW" if index == 5 else "COMPLETED"
            output = (
                f"date: {DAY}\nstage: {number}\nstatus: {status}\n"
                f"run_key: {DAY}:{number}\nsource_refs: [real-source]\n"
                "predecessor_refs: [earlier]\nattempts: 2\n"
                "generated_at_riyadh: 2026-10-13T11:00:00+03:00\n"
                "next_action: human-review\n"
            )
            if index == 4:
                output += "draft_image_urls: https://drive.google.com/file/d/demo/view\n"
            if index == 5:
                output += "final_image_url: https://drive.google.com/file/d/demo/view\n"
            (self.stage_dir / filename).write_text(output, encoding="utf-8")

    def test_missing_outputs_fail(self):
        self.assertEqual(len(check_date(self.root, DAY)), 5)

    def test_complete_handoff_passes(self):
        self.write_handoffs()
        self.assertEqual(check_date(self.root, DAY), [])

    def test_final_image_link_absence_fails(self):
        self.write_handoffs()
        file = self.stage_dir / FILES[-1]
        file.write_text(file.read_text().replace("final_image_url:", "placeholder:"), encoding="utf-8")
        self.assertTrue(any("final_image_url" in x for x in check_date(self.root, DAY)))

    def test_blocked_stage_fails(self):
        self.write_handoffs()
        file = self.stage_dir / FILES[3]
        file.write_text(file.read_text().replace("status: COMPLETED", "status: BLOCKED"), encoding="utf-8")
        self.assertTrue(any("BLOCKED" in x for x in check_date(self.root, DAY)))


if __name__ == "__main__":
    unittest.main()
