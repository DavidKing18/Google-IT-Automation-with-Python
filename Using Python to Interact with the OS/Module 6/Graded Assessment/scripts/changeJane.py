#!/usr/bin/env python3

import sys
import subprocess

oldFiles = sys.argv[1]

with open(file=oldFiles) as file:
        oldPaths = [path.strip() for path in file.readlines()]

newPaths = [path.replace("jane", "jdoe") for path in oldPaths]
for i in range(2):
        subprocess.run(["mv", oldPaths[i], newPaths[i]])

# E no fit run! Wrote this on a remote linux machine 😅
