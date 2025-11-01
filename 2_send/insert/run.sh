#!/bin/bash

R=32
L=1
U=524288 #2^19
S=2

if [ -f "results/binary_insert.csv" ] ; then
    rm "results/binary_insert.csv"
fi
g++ uhr_binary.cpp -std=c++11 -O0 -o uhr_binary;
./uhr_binary results/binary_insert.csv $R $L $U $S;

if [ -f "results/binomial_insert.csv" ] ; then
    rm "results/binomial_insert.csv"
fi
g++ uhr_binomial.cpp -std=c++11 -O0 -o uhr_binomial;
./uhr_binomial results/binomial_insert.csv $R $L $U $S;

if [ -f "results/fibonacci_insert.csv" ] ; then
    rm "results/fibonacci_insert.csv"
fi
g++ uhr_fibonacci.cpp -std=c++11 -O0 -o uhr_fibonacci;
./uhr_fibonacci results/fibonacci_insert.csv $R $L $U $S;

