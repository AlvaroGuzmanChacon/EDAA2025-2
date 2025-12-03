#!/bin/bash

REP=$1

for ((i = 5; i <= 10; i++)); do
	N=$((2**i))
	sed -i '9c\N='$N Makefile
	sed -n '9p' Makefile
	rm mm
	rm mmt
	rm mms
	make

	sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -x ";" -o temp.txt -r $REP -e task-clock,cycles,instructions,L1-dcache-loads,L1-dcache-load-misses ./mm
	#awk -F";" '{print $1 ";" $2 ";" $3}' temp.txt > MM_$N.csv
	awk -F";" '{print $3}' temp.txt | paste -sd ';' - > MM_$N.csv
	awk -F";" '{print $1}' temp.txt | paste -sd ';' - >> MM_$N.csv
	sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -x ";" -o temp.txt -r $REP -e task-clock,cycles,instructions,L1-dcache-loads,L1-dcache-load-misses ./mmt
	awk -F";" '{print $3}' temp.txt | paste -sd ';' - > MMT_$N.csv
	awk -F";" '{print $1}' temp.txt | paste -sd ';' - >> MMT_$N.csv
	sudo /usr/lib/linux-tools/6.8.0-88-generic/perf stat -x ";" -o temp.txt -r $REP -e task-clock,cycles,instructions,L1-dcache-loads,L1-dcache-load-misses ./mms
	awk -F";" '{print $3}' temp.txt | paste -sd ';' - > MMS_$N.csv
	awk -F";" '{print $1}' temp.txt | paste -sd ';' - >> MMS_$N.csv

done

