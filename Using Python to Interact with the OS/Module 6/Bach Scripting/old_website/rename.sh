#!/bin/bash

for file in *.html; do
	filename=$(basename "$file" .html)
	mv "$file" "$filename.HTM"
done;
