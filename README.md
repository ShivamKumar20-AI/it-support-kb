# IT Support Knowledge Base

A personal learning project: a small first-line IT support knowledge base, with templates, a simple asset inventory tool and a practice lab. It is built around everyday desktop support tasks: troubleshooting, user accounts and permissions, documentation and asset records.

> This is a learning project. The articles are written from published guidance and my own study. The sample asset data is fictional. Nothing here comes from any employer.

## What is in it

| Folder | Contents |
|---|---|
| [`kb/`](kb) | Eight knowledge base articles: accounts and lockouts, printers, slow PCs, network, Outlook, drivers, new user permissions, monitors and USB |
| [`templates/`](templates) | A KB article template, a single point lesson template and a worked example |
| [`scripts/`](scripts) | An asset inventory tool in Python that records a device's details to a CSV |
| [`quality-audit-toolkit/`](quality-audit-toolkit) | A second project: an operational audit checklist, Excel audit tracker, trend script and sample report (fictional data) |
| [`sample-data/`](sample-data) | A fictional CMDB-style asset register |
| [`lab/`](lab) | A learning log of the guided Windows labs I have completed |

## Article format
Every article has the same sections: **Symptom, Likely causes, Steps, Escalate when, Notes**. This keeps fixes consistent and makes it clear when to hand a problem on.

## Asset inventory
The tool collects hostname, user, operating system, make, model, serial number, memory and disk space, and appends one row per run to a CSV. That can then feed an asset register or CMDB.

```bash
python3 scripts/asset_inventory.py asset_record.csv
```

The script uses only the Python standard library and runs on Windows, macOS and Linux.

## Skills this shows
Technical writing, troubleshooting method, Windows administration basics, least-privilege access, asset management, and simple scripting.
