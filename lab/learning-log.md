# Learning log: Windows fundamentals

A record of the guided, browser-based labs I have completed to build Windows support skills, from the TryHackMe Windows Fundamentals module. Each entry links the topic to a knowledge base article in this repository.

---

## Room 1: [Windows Fundamentals 1](https://tryhackme.com/room/windowsfundamentals1xbx)
- **Date completed:** 14 October 2026
- **What it covered:** the Windows desktop, the NTFS file system, User Account Control (UAC) and the Control Panel.
- **What I learned:**
  1. NTFS supports file and folder permissions, and the older FAT32 does not. Permissions are set under a folder's Properties > Security tab (Read, Write, Modify, Full control).
  2. UAC makes standard users enter administrator credentials, and asks administrators to confirm, before a change that affects the whole system. This limits what malware or a mistake can do.
  3. Settings and the Control Panel are the main places to change system, network and account options, so knowing where each option lives saves time when supporting users.
- **Related article:** [`kb/07-create-windows-user-with-permissions.md`](../kb/07-create-windows-user-with-permissions.md)

## Room 2: [Windows Fundamentals 2](https://tryhackme.com/room/windowsfundamentals2x0x)
- **Date completed:** 14 October 2026
- **What it covered:** system configuration, UAC settings, resource monitoring and the Windows Registry.
- **What I learned:**
  1. System Configuration (`msconfig`) and Task Manager show what starts with Windows and which processes use CPU, memory and disk, which is the first check for a slow PC.
  2. Computer Management and Resource Monitor (`resmon`) group tools such as Event Viewer, Services, Local Users and Groups, and Device Manager in one place.
  3. The Registry (`regedit`) stores Windows and application settings, so changes to it need care and a backup first.
- **Related article:** [`kb/03-slow-pc.md`](../kb/03-slow-pc.md)

## Room 3: [Windows Fundamentals 3](https://tryhackme.com/room/windowsfundamentals3xzx)
- **Date completed:** 14 October 2026
- **What it covered:** Windows Updates, Windows Security and BitLocker.
- **What I learned:**
  1. Windows Update keeps the system patched, and pending or failed updates are a common cause of odd behaviour, so I check them early when troubleshooting.
  2. Windows Security brings together virus and threat protection and the firewall, and these should not be disabled to fix a fault.
  3. BitLocker encrypts a drive so the data is protected if a device is lost, and the recovery key must be stored safely.
- **Related article:** [`kb/03-slow-pc.md`](../kb/03-slow-pc.md)

---

## Next steps
- CompTIA A+ Core 1 (hardware) and Core 2 (operating systems): in progress
