#!/bin/bash

R=64
L=1
U=100000000
S=1000000
F="res.csv"
#F="results.csv"

if [ -f "results/$F" ] ; then
    rm "results/$F"
fi

g++ uhr.cpp -std=c++11 -O0 -o uhr;
./uhr results/$F $R $L $U $S;


#awk 'NR >= 2' "results/$F" >> "results/res.csv";
