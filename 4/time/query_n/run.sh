#!/bin/bash


g++ uhr_segment.cpp -std=c++11 -O0 -o uhr_segment;
./uhr_segment time_query_n_segment_tree.csv 32 4 33554432 2;


g++ uhr_sparse.cpp -std=c++11 -O0 -o uhr_sparse;
./uhr_sparse time_query_n_sparse_table.csv 32 4 33554432 2;
