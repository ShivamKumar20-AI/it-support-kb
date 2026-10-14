# No network or unstable Wi-Fi

**Category:** Network | **Audience:** First-line support

## Symptom
The user has no internet or network drives, or the connection keeps dropping.

## Likely causes
- Wi-Fi turned off, airplane mode on, or wrong network selected
- Loose or faulty network cable or dock
- IP address problem (no address from DHCP)
- Network adapter driver issue
- Wider network outage

## Steps
1. Ask whether others nearby are affected. If many are, escalate as a network outage.
2. Check the physical basics: cable seated at both ends, dock connected, airplane mode off, Wi-Fi switch on.
3. Try a different cable or wall port if one is available.
4. Open Command Prompt and run:
   - `ipconfig` to see whether the PC has a valid IP address. An address starting `169.254` means it did not get one from the network.
   - `ipconfig /release` then `ipconfig /renew`
   - `ping 8.8.8.8` to test internet reachability, then `ping` a known internal server to test the local network
   - `ipconfig /flushdns` if websites fail but pings by number work
5. Disable and re-enable the network adapter (Settings > Network & internet > Advanced network settings).
6. If still failing, update or reinstall the network adapter driver (article 06).
7. Confirm the connection holds for a few minutes. Log the cause.

## Escalate when
- Several users are affected
- The wall port or switch appears to be at fault
- The PC gets an IP address but cannot reach internal systems (likely VLAN, firewall or DNS)

## Notes
A `169.254.x.x` address is a useful clue: the PC is connected physically but the network is not giving it an address.
