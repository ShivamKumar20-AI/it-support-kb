# IT Support Knowledge Base

A personal learning project: a small first-line IT support knowledge base, with templates, a simple asset inventory tool and a practice lab. It is built around everyday desktop support tasks: troubleshooting, user accounts and permissions, documentation and asset records.

> This is a learning project. The articles are written from published guidance and my own study. The sample asset data is fictional. Nothing here comes from any employer.

## What is in it

| Folder | Contents |
|---|---|
| [`kb/`](kb) | Eight knowledge base articles: accounts and lockouts, printers, slow PCs, network, Outlook, drivers, new user permissions, monitors and USB |
| [`templates/`](templates) | A KB article template, a single point lesson template and a worked example |
| [`scripts/`](scripts) | Asset inventory tools in Python and PowerShell that record a device's details to a CSV |
| [`sample-data/`](sample-data) | A fictional CMDB-style asset register |
| [`lab/`](lab) | A virtual machine lab guide for practising accounts, permissions and fault finding |

## Article format
Every article has the same sections: **Symptom, Likely causes, Steps, Escalate when, Notes**. This keeps fixes consistent and makes it clear when to hand a problem on.

## Asset inventory
The tool collects hostname, user, operating system, make, model, serial number, memory and disk space, and appends one row per run to a CSV. That can then feed an asset register or CMDB.

```bash
python3 scripts/asset_inventory.py asset_record.csv
```

On Windows you can also use `scripts/Get-AssetInventory.ps1`.

## Skills this shows
Technical writing, troubleshooting method, Windows administration basics, least-privilege access, asset management, and simple scripting.
