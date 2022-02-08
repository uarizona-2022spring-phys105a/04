#!/usr/bin/env python3

from math import pi

import matplotlib
matplotlib.use('agg')

from matplotlib import pyplot as plt

ns = []
vs = []

for n in [100, 200, 400, 800, 1600, 3200]:
    with open(f'pi-{n}.txt') as f:
        v = [float(l) for l in f]
    ns.append(n)
    vs.append(sum(v) / len(v))

es = [abs(v - pi) for v in vs]

plt.loglog(ns, es)
plt.loglog(ns, [0.1 * n**-0.5 for n in ns])
plt.savefig('pi.png', dpi=144)
