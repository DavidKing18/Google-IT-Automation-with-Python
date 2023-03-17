#!/bin/bash

line="-----------------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"

echo "LOCALHOST CHECK"
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything is Ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi
echo $line

echo "PATH CHECK"
if test -n "$PATH"; then echo "Your path is not empty."; fi; echo $line

echo "PATH CHECK AGAIN"
if [ -n "$PATH" ] ; then echo "Your path is not empty."; fi; echo $line
