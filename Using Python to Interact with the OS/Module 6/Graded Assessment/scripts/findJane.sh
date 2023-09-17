# E no fit run! Wrote this on a remote linux machine 😅

#!/bin/bash

> oldFiles.txt

files=$(ls ~/data | grep "jane_")

for file in $files; do
        parent_dir="/home/student-01-f9d2a9d2f510"
        abs_path=$parent_dir/data/$file
        if test -e $abs_path; then
                echo $abs_path >>  oldFiles.txt;
        fi;
done;
