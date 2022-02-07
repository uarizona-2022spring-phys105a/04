#!/usr/bin/env bash

for i in {1..100}; do
    echo $i $(./pi.py ${i}000)
done | tee > pi.txt

./plot.py
