# Outlook will not open or keeps asking for a password

**Category:** Applications | **Audience:** First-line support

## Symptom
Outlook freezes on start-up, shows "Disconnected" or "Trying to connect", or keeps prompting for credentials.

## Likely causes
- Network or sign-in problem
- Cached credentials out of date after a password change
- Corrupt Outlook profile or data file
- A faulty add-in
- Mailbox over its size limit

## Steps
1. Check the internet connection first. Test in a web browser and confirm the user can sign in to webmail. If webmail also fails, the problem is the account, not Outlook.
2. If the user recently changed their password, sign out of Office, then clear old entries in **Credential Manager** (Windows Credentials, anything with "Office" or "Outlook") and sign in again.
3. Start Outlook in **safe mode**: hold Ctrl while opening it, or run `outlook.exe /safe`. If it works, an add-in is the cause. Disable add-ins under File > Options > Add-ins.
4. Run an Office **Quick Repair** (Settings > Apps > Installed apps > Microsoft 365 > Modify).
5. If the problem continues, create a **new Outlook profile** (Control Panel > Mail > Show Profiles > Add) and set it as default.
6. Check whether the mailbox is full and advise the user to archive or delete large items.
7. Confirm Outlook opens and mail is syncing. Log the cause.

## Escalate when
- Webmail also fails (account or licence issue)
- The mailbox is on hold or at a hard size limit
- Many users are affected (possible service issue)

## Notes
Always check webmail first. It splits "account problem" from "this PC's Outlook" in one step.
