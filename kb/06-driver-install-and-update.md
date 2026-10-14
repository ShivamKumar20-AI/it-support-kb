# Installing, updating or rolling back a driver

**Category:** Hardware | **Audience:** First-line support

## Symptom
A device (printer, network adapter, monitor, webcam, USB device) does not work, or shows a yellow warning in Device Manager.

## Likely causes
- Driver missing, corrupt or the wrong version
- A Windows update replaced a working driver
- Device is new and Windows has no driver for it

## Steps
1. Open **Device Manager** (right-click Start > Device Manager). Find the device. A yellow triangle means a driver problem.
2. Note the device name and, in Properties > Details > Hardware Ids, the hardware ID if it is unknown.
3. Check Windows Update first (Settings > Windows Update > Advanced options > Optional updates > Driver updates).
4. If none is offered, download the driver from the **manufacturer's own site** for the exact model and Windows version. Never use third-party driver download sites.
5. Install the driver (right-click device > Update driver > Browse my computer, or run the installer). Restart if asked.
6. If the problem started after an update, use **Properties > Driver > Roll Back Driver** if available.
7. Confirm the device works and the warning has cleared. Record the driver version in the ticket.

## Escalate when
- No driver exists for the Windows version in use
- The driver install fails with a security or signing error
- The device is faulty hardware (works on another PC? If not, replace it)

## Notes
Test the device on a second PC to find out quickly whether the device or the first PC is at fault.
