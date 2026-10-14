# Password reset and account lockout

**Category:** Accounts and access | **Audience:** First-line support

## Symptom
A user cannot sign in. They see "incorrect password", "account locked" or "your password has expired".

## Likely causes
- Password typed incorrectly (Caps Lock, keyboard layout)
- Password expired under policy
- Account locked after repeated failed attempts
- Old password saved on a phone or mapped drive, repeatedly retrying

## Steps
1. **Verify the user's identity** before any change (employee ID plus a second check, as per site policy). Never reset on an unverified request.
2. Ask the user to check Caps Lock and try once more on a different device if possible.
3. In the account directory, check whether the account is **locked** or **expired**.
4. If locked: unlock the account. If expired or forgotten: reset the password to a temporary one and set "user must change password at next sign-in".
5. Ask the user to **remove saved old passwords** from phones, mapped drives and the Windows Credential Manager (Control Panel > Credential Manager), otherwise the account will lock again.
6. Confirm the user can sign in and open their usual applications.
7. Log the ticket: cause, action taken, time to resolve.

## Escalate when
- The account keeps locking within minutes (a device is retrying an old password; ask the second-line team to check the lockout source)
- You cannot verify the user's identity
- The account was disabled rather than locked

## Notes
Never send temporary passwords by email or chat. Give them verbally or through the approved channel.
