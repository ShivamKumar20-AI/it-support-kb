# Printer shows offline or will not print

**Category:** Peripherals | **Audience:** First-line support

## Symptom
A document is sent to print but nothing comes out, or the printer shows "Offline" or "Error" on the user's PC.

## Likely causes
- Printer powered off, out of paper or toner, or showing a jam
- Network cable or Wi-Fi connection to the printer lost
- Stuck job blocking the print queue
- Wrong default printer selected
- Driver problem after a Windows update

## Steps
1. Check the printer itself: power, paper, toner, jams and any message on its display. Fix what you can see.
2. Check the printer's network connection (link light on the cable, or IP address shown on the display).
3. On the user's PC, open **Settings > Bluetooth & devices > Printers & scanners** and check the printer is not marked offline. Make sure **Use printer offline** is not ticked.
4. Check the **print queue**. Cancel stuck jobs. If a job will not cancel:
   - Open Services (`services.msc`), stop **Print Spooler**
   - Delete everything in `C:\Windows\System32\spool\PRINTERS`
   - Start **Print Spooler** again
5. Print a **test page** from the printer properties.
6. If it still fails, remove the printer and add it again. Reinstall the driver (see article 06).
7. Confirm the user can print, and log the cause.

## Escalate when
- The printer is hardware-faulty (repeating error code, mechanical noise)
- Several users are affected (likely a network or print server issue)
- The print server is down

## Notes
If only one user is affected, the problem is almost always on their PC. If many are affected, it is the printer or the network.
