#!/usr/bin/env python3
"""Collect basic asset details from this computer and append them to a CSV.

Standard library only. Works on Windows, macOS and Linux.
Usage:  python asset_inventory.py [output.csv]
"""
import csv
import datetime
import getpass
import os
import platform
import shutil
import socket
import subprocess
import sys

FIELDS = ["collected_at", "hostname", "username", "os", "os_version", "architecture",
          "manufacturer", "model", "serial_number", "ram_gb", "disk_total_gb", "disk_free_gb"]


def run(cmd):
    """Run a command and return its output, or '' if it fails."""
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=20).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def powershell(expr):
    return run(["powershell", "-NoProfile", "-Command", expr])


def get_hardware():
    system = platform.system()
    if system == "Windows":
        return {
            "manufacturer": powershell("(Get-CimInstance Win32_ComputerSystem).Manufacturer"),
            "model": powershell("(Get-CimInstance Win32_ComputerSystem).Model"),
            "serial_number": powershell("(Get-CimInstance Win32_BIOS).SerialNumber"),
            "ram_bytes": powershell("(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory"),
        }
    if system == "Darwin":
        return {
            "manufacturer": "Apple",
            "model": run(["sysctl", "-n", "hw.model"]),
            "serial_number": run(["sh", "-c",
                "system_profiler SPHardwareDataType | awk '/Serial Number/{print $NF}'"]),
            "ram_bytes": run(["sysctl", "-n", "hw.memsize"]),
        }
    ram = ""
    try:
        with open("/proc/meminfo") as f:
            ram = str(int(f.readline().split()[1]) * 1024)
    except (OSError, ValueError, IndexError):
        pass
    return {
        "manufacturer": run(["cat", "/sys/class/dmi/id/sys_vendor"]),
        "model": run(["cat", "/sys/class/dmi/id/product_name"]),
        "serial_number": run(["cat", "/sys/class/dmi/id/product_serial"]),
        "ram_bytes": ram,
    }


def gb(value):
    try:
        return round(int(value) / 1024 ** 3, 1)
    except (TypeError, ValueError):
        return ""


def collect():
    hw = get_hardware()
    root = os.path.abspath(os.sep)
    total, _used, free = shutil.disk_usage(root)
    return {
        "collected_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "hostname": socket.gethostname(),
        "username": getpass.getuser(),
        "os": platform.system(),
        "os_version": platform.version() if platform.system() == "Windows" else platform.release(),
        "architecture": platform.machine(),
        "manufacturer": hw["manufacturer"],
        "model": hw["model"],
        "serial_number": hw["serial_number"],
        "ram_gb": gb(hw["ram_bytes"]),
        "disk_total_gb": gb(total),
        "disk_free_gb": gb(free),
    }


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "asset_record.csv"
    row = collect()
    new_file = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow(row)
    print(f"Recorded {row['hostname']} to {path}")


if __name__ == "__main__":
    main()
