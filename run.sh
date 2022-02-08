#!/usr/bin/env bash

for n in 100 200 400 800 1600 3200; do
    echo $n
    for j in {1..256}; do
	./pi.py $n
    done > pi-${n}.txt
done

./plot.py
