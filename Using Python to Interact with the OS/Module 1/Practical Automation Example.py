#!/usr/bin/env python3

import shutil
import psutil

diskUsage = shutil.disk_usage("/")
print(diskUsage)

print("Free Space(%): ", (diskUsage.free/diskUsage.total)*100)

print(psutil.cpu_percent(0.1))
print(psutil.cpu_percent(0.5))
print(psutil.cpu_percent(1.0))
print(psutil.cpu_percent(2.0))

print()

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    pctFree = (du.free/du.total) * 100
    return pctFree > 20

def check_cpu_usage():
    pctUsage = psutil.cpu_percent(1)
    return pctUsage <75

if not check_disk_usage("/") or not check_cpu_usage():
    print("WARNING! - Your computer is at critical state")
else:
    print("Everything is OK!")