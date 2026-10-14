# Lab: Windows accounts, permissions and a troubleshooting exercise

A practice lab for first-line support skills, run in a free virtual machine. It covers the tasks described in knowledge base articles 06 and 07.

## What you need
- A PC or Mac that can run a virtual machine (VirtualBox is free)
- A Windows 11 evaluation ISO from Microsoft's website (no purchase needed for evaluation)
- About 3 hours

## Part 1: Build the machine
1. Install VirtualBox and create a new VM: 4 GB memory, 2 CPUs, 60 GB disk.
2. Install Windows 11 from the ISO. Create the first admin account.
3. Run Windows Update and take a snapshot named "clean-install".

## Part 2: Accounts and permissions
1. Create two standard users, `user.sales` and `user.warehouse`, with "must change password at next logon" ticked.
2. Create a folder `C:\Shared\Sales`. Give `user.sales` Read and Write and give `user.warehouse` no access (remove inherited rights if needed).
3. Sign in as each user. Confirm `user.sales` can save a file there and `user.warehouse` is blocked.
4. Add `user.warehouse` to a new group `Warehouse-Read` and give that group Read-only on a second folder `C:\Shared\Reports`. Confirm they can open files but not save.
5. Record what you did and what you saw.

## Part 3: Break and fix
Take a snapshot first, then break one thing at a time and fix it using the knowledge base:
1. Disable the network adapter, then restore it using article 04 steps.
2. Stop the Print Spooler service and fix it as in the single point lesson.
3. Fill the disk with large files, find them, and clear space as in article 03.
4. Disable a driver in Device Manager and restore it using article 06.

## Part 4: Asset record
1. Copy `scripts/Get-AssetInventory.ps1` into the VM and run it.
2. Check the CSV it produces and compare it with Settings > System > About.

## Write-up (what to record)
For each part: what you did, what you expected, what happened, and what you would do differently. Add screenshots. Only record what you actually did.
