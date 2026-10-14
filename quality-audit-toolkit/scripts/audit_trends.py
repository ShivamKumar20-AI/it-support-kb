#!/usr/bin/env python3
"""Summarise an audit log CSV: pass rates by area and month, repeat issues and open confirmations.

Standard library only.
Usage:  python audit_trends.py [data/audit-log-sample.csv]
"""
import csv
import sys
from collections import Counter, defaultdict

PASS_MARK = 0.90


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["rate"] = int(r["Checks passed"]) / int(r["Checks done"])
        r["result"] = "Pass" if r["rate"] >= PASS_MARK else "Fail"
        r["month"] = r["Date"][:7]
    return rows


def pct(x):
    return f"{x:.0%}"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data/audit-log-sample.csv"
    rows = load(path)
    routine = [r for r in rows if r["Audit type"] == "Routine"]

    print(f"Routine audits: {len(routine)}   Confirmation audits: {len(rows) - len(routine)}")
    fails = sum(r["result"] == "Fail" for r in routine)
    print(f"Routine fail rate: {pct(fails / len(routine))} ({fails} of {len(routine)})\n")

    print("By area (routine audits)")
    by_area = defaultdict(list)
    for r in routine:
        by_area[r["Area"]].append(r)
    for area, rs in sorted(by_area.items(), key=lambda kv: -sum(x["result"] == "Fail" for x in kv[1]) / len(kv[1])):
        f = sum(x["result"] == "Fail" for x in rs)
        avg = sum(x["rate"] for x in rs) / len(rs)
        print(f"  {area:<20} audits {len(rs):>2}  failed {f:>2}  fail rate {pct(f / len(rs)):>4}  avg pass rate {pct(avg)}")

    print("\nBy month (routine audits)")
    by_month = defaultdict(list)
    for r in routine:
        by_month[r["month"]].append(r)
    for m in sorted(by_month):
        rs = by_month[m]
        f = sum(x["result"] == "Fail" for x in rs)
        print(f"  {m}  audits {len(rs):>2}  failed {f:>2}  fail rate {pct(f / len(rs)):>4}")

    print("\nMost common findings on failed audits")
    for finding, n in Counter(r["Main finding"] for r in rows if r["result"] == "Fail" and r["Main finding"]).most_common(5):
        print(f"  {n}  {finding}")

    confirmations = defaultdict(list)
    for r in rows:
        if r["Audit type"] == "Confirmation":
            confirmations[r["Original audit ID"]].append(r)
    closed = refailed = awaiting = 0
    for r in routine:
        if r["result"] != "Fail":
            continue
        c = confirmations.get(r["Audit ID"], [])
        if any(x["result"] == "Pass" for x in c):
            closed += 1
        elif c:
            refailed += 1
        else:
            awaiting += 1
    print(f"\nConfirmation audits on failed routine audits: closed {closed}, re-failed {refailed}, awaiting {awaiting}")


if __name__ == "__main__":
    main()
