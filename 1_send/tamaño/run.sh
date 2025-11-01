#!/bin/bash

R=256
L=1000000
U=1024000000
S=2
F="res_size_B.csv"
#F="results.csv"

if [ -f "results/$F" ] ; then
    rm "results/$F"
fi

g++ uhr.cpp -std=c++11 -O0 -o uhr;
./uhr results/$F $R $L $U $S;


#awk 'NR >= 2' "results/$F" >> "results/res.csv";
