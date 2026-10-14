# Single Point Lesson: Clear a stuck print queue

| Field | Detail |
|---|---|
| Task | Remove stuck print jobs that block a printer |
| Who is it for | Any user, or first-line support |
| Time needed | 2 minutes |
| Tools or access needed | Windows PC, local admin rights for steps 3 to 5 |

## Why this matters
One stuck job stops every document behind it. Users keep clicking print and the queue gets longer.

## Steps
1. Open **Settings > Bluetooth & devices > Printers & scanners**, select the printer, then **Open print queue**.
2. Right-click the stuck job and choose **Cancel**. If it clears, stop here.
3. If it will not cancel, press **Windows key + R**, type `services.msc` and press Enter.
4. Find **Print Spooler**, right-click and choose **Stop**. Then delete all files in `C:\Windows\System32\spool\PRINTERS`.
5. Right-click **Print Spooler** again and choose **Start**.
6. Print a test page.

## Check it worked
- The queue is empty and the test page prints.

## Common mistakes
- Deleting the PRINTERS folder itself instead of the files inside it
- Forgetting to start the Print Spooler again

## Who to contact
- IT service desk, if the queue jams again within the same day
