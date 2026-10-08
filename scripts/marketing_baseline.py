#!/usr/bin/env python3
"""Safely capture Basic Diet commercial MARKETING aggregates; never user/payment records.

Offline by default. Live mode is a deliberate GET with a dashboard admin token in env.
Only explicitly allowlisted aggregate fields are written to disk.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
from pathlib import Path
import re
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

BACKEND_ENDPOINT = (
    "https://basicdiet145-production-51e9.up.railway.app"
    "/api/dashboard/accounting/marketing-analytics"
)
WINDOWS = (30, 60, 90)
COUNTS = (
    "registrations", "loggedInUsers", "checkoutStarted", "checkoutUsers",
    "pendingCheckouts", "abandonedCheckouts", "failedPayments",
    "paidTransactions", "paidCustomers", "firstTimeSubscribers",
    "repeatSubscribers", "newRegistrationsPaid", "cancellations",
)
MONEY = ("appRevenueHalala", "totalSubscriptionRevenueHalala", "aovHalala")
RATES = ("registerToPaidRate", "checkoutToPaidRate", "repeatCustomerRate")
MAX_RESPONSE = 2_000_000


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON property")
        result[key] = value
    return result


def json_document(raw):
    if len(raw) > MAX_RESPONSE:
        raise ValueError("Analytics input is too large")
    try:
        return json.loads(raw, object_pairs_hook=unique_object,
                          parse_constant=lambda _: (_ for _ in ()).throw(ValueError("Nonfinite number")))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("Invalid JSON response") from None


def report_dates(as_of):
    try:
        end = dt.date.fromisoformat(as_of)
    except (TypeError, ValueError):
        raise ValueError("Expected YYYY-MM-DD end date") from None
    if end.isoformat() != as_of:
        raise ValueError("Expected canonical YYYY-MM-DD end date")
    return {days: {"from": (end - dt.timedelta(days=days - 1)).isoformat(),
                   "to": as_of, "days": days} for days in WINDOWS}


def saudi_yesterday():
    return (dt.datetime.now(ZoneInfo("Asia/Riyadh")).date() - dt.timedelta(days=1)).isoformat()


def strictly_nonnegative(value, key, *, maximum=None):
    if type(value) not in (float, int) or not math.isfinite(value) or value < 0:
        raise ValueError(f"Invalid numeric aggregate: {key}")
    if maximum is not None and value > maximum:
        raise ValueError(f"Invalid rate range: {key}")
    return value


def normalize_report(doc, expected_range, captured_at, origin):
    """Fail closed on incompatible metadata; copy numerical aggregates only."""
    if type(doc) is not dict:
        raise ValueError("Expected analytics object")
    report = doc.get("data", doc)
    if doc.get("status") is False or type(report) is not dict:
        raise ValueError("Backend returned an error")
    if report.get("reportType") != "marketing_analytics":
        raise ValueError("Unexpected reportType")
    if report.get("timezone") != "Asia/Riyadh" or report.get("currency") != "SAR" or report.get("moneyUnit") != "halala":
        raise ValueError("Wrong timezone/currency; refusing misleading snapshot")
    block = report.get("range")
    if type(block) is not dict or any(block.get(k) != v for k, v in expected_range.items()):
        raise ValueError("Response date range does not match request")
    # Backend supplies explicit default filter values even without query filters.
    default_filters = {"promoCode": "", "fulfillmentMethod": "all", "paymentProvider": "all",
                       "daysCount": None, "grams": None, "mealsPerDay": None}
    if report.get("filters") not in ({}, None, default_filters):
        raise ValueError("Filtered report is not an unsegmented baseline")
    kpis = report.get("kpis")
    if type(kpis) is not dict:
        raise ValueError("Missing KPI aggregate")
    cleaned = {}
    for key in COUNTS + MONEY:
        v = kpis.get(key)
        if type(v) is not int:
            raise ValueError(f"Missing/invalid integer KPI: {key}")
        cleaned[key] = int(strictly_nonnegative(v, key))
    for key in RATES:
        value = kpis.get(key)
        cleaned[key] = strictly_nonnegative(value, key, maximum=100)
    # No copying of arbitrary unknown arrays, user IDs, contact details, links,
    # raw payments, sessions, provider logs, or free-text notes.
    return {
        "schema_version": 1, "kind": "marketing_baseline",
        "verification": "official_authenticated_aggregate_response" if origin == "live" else "operator_supplied_aggregate_not_live_verified",
        "period": expected_range, "captured_at": captured_at,
        "timezone": "Asia/Riyadh", "currency": "SAR", "money_unit": "halala",
        "source": "GET /api/dashboard/accounting/marketing-analytics",
        "source_mode": origin, "filters": {}, "kpis": cleaned,
        "limitations": [
            "No app installs/first_open in the backend metric layer",
            "No reliable ad/creative source-to-first-paid attribution",
            "Registration and login metrics are not necessarily filtered by checkout segments",
            "Paid customers/revenue and conversion rates have backend-specific definitions",
        ],
    }


def format_markdown(snapshot):
    k = snapshot["kpis"]
    period = snapshot["period"]
    return "\n".join([
        "# Basic Diet — Aggregate marketing baseline", "",
        f"**Reporting range:** {period['from']} → {period['to']} ({period['days']} inclusive Saudi days)",
        f"**Captured:** {snapshot['captured_at']} | Currency SAR | Monetary fields stored as halala",
        f"**Source:** {snapshot['source']} | Mode: {snapshot['source_mode']}",
        f"**Evidence:** {snapshot['verification']}", "",
        "| Metric | Value |", "| --- | ---: |",
        *[f"| {key} | {k[key]} |" for key in COUNTS + MONEY + RATES],
        "", "## Interpret with care", "",
        *[f"- {item}" for item in snapshot["limitations"]],
        "", "**Not an app-install count, causal advertising report, or individual customer export.**", ""
    ])


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Analytics redirect denied")


def live_report(expected_range):
    token = os.environ.get("BASICDIET_DASHBOARD_TOKEN", "")
    if not token or "\n" in token or "\r" in token or len(token) > 8192:
        raise ValueError("Set BASICDIET_DASHBOARD_TOKEN securely to use --live")
    uri = BACKEND_ENDPOINT + "?" + urllib.parse.urlencode({
        "from": expected_range["from"], "to": expected_range["to"],
        "comparePrevious": "false"
    })
    req = urllib.request.Request(uri, method="GET", headers={
        "Authorization": "Bearer " + token, "Accept": "application/json",
    })
    try:
        opener = urllib.request.build_opener(NoRedirect())
        with opener.open(req, timeout=25) as response:
            raw = response.read(MAX_RESPONSE + 1)
    except urllib.error.HTTPError as exc:
        raise ValueError(f"Dashboard analytics HTTP {exc.code}; credentials/permissions may be missing") from None
    except (urllib.error.URLError, TimeoutError, OSError):
        raise ValueError("Analytics endpoint unavailable; no data captured") from None
    return json_document(raw)


def load_offline(directory, days):
    file = directory / f"{days}d.json"
    if not file.is_file():
        raise ValueError(f"Missing {days}d.json input")
    return json_document(file.read_bytes())


def capture(*, end_date, input_dir=None, live=False, out_dir=None, now=None):
    if (input_dir is None) == (not live):
        raise ValueError("Choose exactly one source: --input-dir OR --live")
    if out_dir is None:
        raise ValueError("Specify a local output directory")
    today = dt.datetime.now(ZoneInfo("Asia/Riyadh")).date()
    as_of = dt.date.fromisoformat(end_date)
    if as_of >= today:
        raise ValueError("Baseline must end before the current Saudi reporting day")
    periods = report_dates(end_date)
    timestamp = now or dt.datetime.now(dt.timezone.utc).isoformat()
    snapshots = []
    for days in WINDOWS:
        report = live_report(periods[days]) if live else load_offline(Path(input_dir), days)
        snapshots.append(normalize_report(report, periods[days], timestamp, "live" if live else "manual_import"))
    # Validate all windows before writing any files. Refuse overwrites.
    output = Path(out_dir)
    output.mkdir(parents=True, exist_ok=True)
    paths = [output / f"baseline-{end_date}-{days}d.{ext}"
             for days in WINDOWS for ext in ("json", "md")]
    if any(path.exists() for path in paths):
        raise ValueError("Snapshot already exists; no files overwritten")
    completed = []
    try:
        for snapshot in snapshots:
            days = snapshot["period"]["days"]
            base = f"baseline-{end_date}-{days}d"
            for extension, contents in (
                ("json", json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"),
                ("md", format_markdown(snapshot))
            ):
                path = output / f"{base}.{extension}"
                with open(path, "x", encoding="utf-8") as handle:
                    handle.write(contents)
                completed.append(path)
    except OSError:
        for file in completed:
            file.unlink(missing_ok=True)
        raise
    return snapshots


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--input-dir", type=Path, help="Directory containing 30d.json, 60d.json, 90d.json")
    mode.add_argument("--live", action="store_true", help="Explicit opt-in to authenticated GET requests")
    parser.add_argument("--to-date", default=None, help="YYYY-MM-DD; default last completed Saudi day")
    parser.add_argument("--out-dir", type=Path, default=Path("output/marketing-baseline"))
    args = parser.parse_args()
    try:
        windows = capture(end_date=args.to_date or saudi_yesterday(),
                          input_dir=args.input_dir, live=args.live, out_dir=args.out_dir)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"CAPTURED {len(windows)} aggregate-only snapshots in {args.out_dir}; "
          "review before any Git commit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
