"""Phase 4 marketing baseline: exact API contract, privacy, safety, zero default network."""
import datetime as dt
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from scripts import marketing_baseline as m


def fake_report(period):
    kpis = {k: 3 for k in m.COUNTS}
    kpis.update({k: 2000 for k in m.MONEY})
    kpis.update({k: 25.0 for k in m.RATES})
    return {
        "status": True, "data": {
            "reportType": "marketing_analytics", "timezone": "Asia/Riyadh",
            "currency": "SAR", "moneyUnit": "halala", "range": period,
            "filters": {
                "promoCode": "", "fulfillmentMethod": "all",
                "paymentProvider": "all", "daysCount": None, "grams": None,
                "mealsPerDay": None,
            },
            "kpis": kpis,
            "users": [{"name": "MUST NEVER APPEAR", "phone": "+966500000000"}],
            "notes": ["MUST NEVER APPEAR"],
        }
    }


class BaselineTests(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.TemporaryDirectory()
        self.addCleanup(self.root.cleanup)
        self.src = Path(self.root.name) / "input"
        self.out = Path(self.root.name) / "output"
        self.src.mkdir()
        self.end = "2025-10-07"
        self.expected = m.report_dates(self.end)
        for days, period in self.expected.items():
            (self.src / f"{days}d.json").write_text(
                json.dumps(fake_report(period)), encoding="utf-8")

    def test_inclusive_periods(self):
        self.assertEqual(self.expected[30], {"from": "2025-09-08", "to": "2025-10-07", "days": 30})
        self.assertEqual(self.expected[60], {"from": "2025-08-09", "to": "2025-10-07", "days": 60})
        self.assertEqual(self.expected[90], {"from": "2025-07-10", "to": "2025-10-07", "days": 90})

    def test_offline_snapshot_is_aggregate_and_no_network(self):
        with patch.object(m, "live_report", side_effect=AssertionError("No network allowed")):
            snaps = m.capture(end_date=self.end, input_dir=self.src,
                              out_dir=self.out, now="2025-10-08T00:00:00+00:00")
        self.assertEqual(len(snaps), 3)
        all_data = "\n".join(p.read_text() for p in self.out.glob("*"))
        self.assertNotIn("MUST NEVER APPEAR", all_data)
        self.assertNotIn("+966500000000", all_data)
        self.assertIn("firstTimeSubscribers", all_data)
        self.assertEqual(len(list(self.out.glob("*.json"))), 3)
        self.assertEqual(len(list(self.out.glob("*.md"))), 3)
        self.assertEqual(snaps[0]["verification"], "operator_supplied_aggregate_not_live_verified")

    def test_already_exists_never_overwritten(self):
        m.capture(end_date=self.end, input_dir=self.src, out_dir=self.out)
        with self.assertRaisesRegex(ValueError, "already exists"):
            m.capture(end_date=self.end, input_dir=self.src, out_dir=self.out)

    def test_missing_middle_window_writes_nothing(self):
        (self.src / "60d.json").unlink()
        with self.assertRaisesRegex(ValueError, "Missing 60d"):
            m.capture(end_date=self.end, input_dir=self.src, out_dir=self.out)
        self.assertFalse(list(self.out.glob("*.json")))

    def test_mismatched_backend_period_rejected(self):
        file = self.src / "30d.json"
        d = json.loads(file.read_text())
        d["data"]["range"]["days"] = 31
        file.write_text(json.dumps(d))
        with self.assertRaisesRegex(ValueError, "date range"):
            m.capture(end_date=self.end, input_dir=self.src, out_dir=self.out)

    def test_filtered_report_not_unsegmented(self):
        doc = fake_report(self.expected[30])
        doc["data"]["filters"]["promoCode"] = "KSA96"
        with self.assertRaisesRegex(ValueError, "Filtered report"):
            m.normalize_report(doc, self.expected[30], "now", "manual_import")

    def test_missing_first_paid_rejected(self):
        doc = fake_report(self.expected[30])
        del doc["data"]["kpis"]["firstTimeSubscribers"]
        with self.assertRaisesRegex(ValueError, "firstTimeSubscribers"):
            m.normalize_report(doc, self.expected[30], "now", "manual_import")

    def test_integer_fields_not_bool_or_negative(self):
        for bad in (True, -1, 1.2):
            doc = fake_report(self.expected[30])
            doc["data"]["kpis"]["registrations"] = bad
            with self.assertRaises(ValueError):
                m.normalize_report(doc, self.expected[30], "now", "manual_import")

    def test_wrong_currency_fails(self):
        doc = fake_report(self.expected[30])
        doc["data"]["currency"] = "USD"
        with self.assertRaisesRegex(ValueError, "currency"):
            m.normalize_report(doc, self.expected[30], "now", "manual_import")

    def test_duplicate_json_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate JSON"):
            m.json_document(b'{"a": 1, "a": 2}')

    def test_live_denied_without_token(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaisesRegex(ValueError, "BASICDIET_DASHBOARD_TOKEN"):
                m.live_report(self.expected[30])

    def test_explicit_source_mode_only(self):
        with self.assertRaisesRegex(ValueError, "exactly one source"):
            m.capture(end_date=self.end, input_dir=None, live=False, out_dir=self.out)
        with self.assertRaisesRegex(ValueError, "exactly one source"):
            m.capture(end_date=self.end, input_dir=self.src, live=True, out_dir=self.out)

    def test_no_today_or_future(self):
        today = dt.datetime.now(m.ZoneInfo("Asia/Riyadh")).date().isoformat()
        with self.assertRaisesRegex(ValueError, "before the current"):
            m.capture(end_date=today, input_dir=self.src, out_dir=self.out)

    def test_live_get_no_redirect(self):
        request_range = self.expected[30]
        with patch.dict("os.environ", {"BASICDIET_DASHBOARD_TOKEN": "temporary-test-token"}):
            with patch.object(m.urllib.request, "build_opener") as mocked:
                opener = mocked.return_value
                obj = fake_report(request_range)
                class FakeResponse:
                    def __enter__(self):
                        return self
                    def __exit__(self, *args):
                        return False
                    def read(self, limit):
                        return json.dumps(obj).encode("utf-8")
                opener.open.return_value = FakeResponse()
                self.assertEqual(m.live_report(request_range)["status"], True)
                req = opener.open.call_args[0][0]
                self.assertEqual(req.get_method(), "GET")
                self.assertTrue(req.full_url.startswith(m.BACKEND_ENDPOINT + "?"))
                self.assertIn("Bearer temporary-test-token", req.headers["Authorization"])

if __name__ == "__main__":
    unittest.main()
