#!/usr/bin/env python3

from math import pi

import matplotlib
matplotlib.use('agg')

from matplotlib import pyplot as plt

ns = []
vs = []

with open('pi.txt') as f:
    for l in f:
        n, v = l.split()
        ns.append(int(n))
        vs.append(float(v))

es = [abs(v - pi)**0.5 for v in vs]

plt.loglog(ns, es)
plt.loglog(ns, [n**-0.5 for n in ns])
plt.savefig('pi.png', dpi=144)
