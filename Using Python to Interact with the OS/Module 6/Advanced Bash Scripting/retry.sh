#!/bin/bash

n=0
command=$1
echo $command
while ! $command && [ $n -le 4 ]; do
	sleep $n
	((n+=1))
	echo "Retry #$n"
done;
