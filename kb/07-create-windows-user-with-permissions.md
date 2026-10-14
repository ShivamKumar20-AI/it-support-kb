# Creating a Windows user account with the right permissions

**Category:** Accounts and access | **Audience:** First-line support

## Symptom / request
A new starter needs a local Windows account, or an existing user needs access to a folder or elevated rights.

## Principle
Give the **least privilege** needed. Standard users for normal work. Administrator only where there is a documented need and approval.

## Steps (local account)
1. Confirm the request is **approved** by the user's manager and recorded in a ticket.
2. Open **Settings > Accounts > Other users > Add account** (or `lusrmgr.msc` on Pro editions).
3. Create the user with a temporary password and tick **User must change password at next logon**.
4. Add the account to the correct group:
   - **Users** for standard access
   - **Administrators** only with documented approval
5. For folder access, right-click the folder > Properties > Security > Edit. Add the user or, better, a group, and tick only the rights needed (Read, or Read and Write). Avoid giving "Full control" unless necessary.
6. Sign in as the new user to **test**: can they open what they need, and are they blocked from what they should not reach?
7. Record the account, group membership and approval in the ticket and the asset record.

## Escalate when
- The account should be created in the company directory (Active Directory or Entra ID), not locally
- Elevated rights are requested without approval
- The request involves access to sensitive or restricted data

## Notes
Prefer groups over individuals when setting folder permissions. It makes later reviews and leavers much easier to manage.
