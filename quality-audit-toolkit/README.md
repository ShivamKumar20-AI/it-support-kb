# Quality Audit Toolkit

A personal learning project showing how operational process audits can be set up, recorded and reported. It covers a checklist template, an Excel tracker with formulas, a short Python trend script and a sample report.

> **All data is fictional.** It was generated for this project. Nothing here comes from any employer or client, and I am not claiming to have audited a warehouse. It is a worked example of the method.

## What is in it

| File | Purpose |
|---|---|
| [`templates/process-audit-checklist-returns.md`](templates/process-audit-checklist-returns.md) | A process audit checklist with pass/fail checks, evidence fields and follow-up |
| [`data/audit-tracker.xlsx`](data/audit-tracker.xlsx) | Excel workbook: audit log with formulas (pass rate, result, month, confirmation status) and a summary sheet by area, month and confirmation outcome |
| [`data/audit-log-sample.csv`](data/audit-log-sample.csv) | The same fictional audit records as a CSV |
| [`scripts/audit_trends.py`](scripts/audit_trends.py) | Reads the CSV and prints pass rates by area and month, common findings and confirmation outcomes |
| [`reports/sample-audit-report.md`](reports/sample-audit-report.md) | A sample report that turns the results into findings and recommendations |

## How it works
1. Each audit is scored against a checklist. A pass rate of 90% or more is a **Pass**.
2. Every failed routine audit needs a **confirmation audit** to check the fix. The tracker shows each one as Closed, Re-failed or Awaiting confirmation.
3. The summary shows where failures are concentrated, how they change over time, and which findings repeat.

```bash
python3 scripts/audit_trends.py data/audit-log-sample.csv
```

The script uses only the Python standard library.

## Skills this shows
Audit planning, evidence-based checking, spreadsheet analysis with formulas, trend and repeat-issue analysis, confirmation auditing, and clear reporting.
