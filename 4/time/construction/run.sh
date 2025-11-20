#!/bin/bash


g++ uhr_segment.cpp -std=c++11 -O0 -o uhr_segment;
./uhr_segment time_construction_segment_tree.csv 32 1 536870912 2;


g++ uhr_sparse.cpp -std=c++11 -O0 -o uhr_sparse;
./uhr_sparse time_construction_sparse_table.csv 32 1536870912 2;
