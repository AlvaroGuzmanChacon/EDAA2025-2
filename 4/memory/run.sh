#!/bin/bash

g++ sp_groesse.cpp -O0 -std=c++11 -g -o sp_groesse;
rm massif.out*;
valgrind --tool=massif ./sp_groesse;
mv massif.out* massif.out;
python3 valgrind_parser.py massif.out sp_table_size.csv;

g++ seg_groesse.cpp -O0 -std=c++11 -g -o seg_groesse;
rm massif.out*;
valgrind --tool=massif ./seg_groesse;
mv massif.out* massif.out;
python3 valgrind_parser.py massif.out seg_table_size.csv;
