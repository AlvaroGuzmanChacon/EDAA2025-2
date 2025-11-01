#!/bin/bash

R=32
L=10000000
U=100000000
S=10000000
F="results_${R}_${L}_${U}_${S}.csv"
#F="results.csv"

if [ -f "results/$F" ] ; then
    rm "results/$F"
fi

g++ uhr.cpp -std=c++11 -O0 -o uhr;
./uhr results/$F $R $L $U $S;

