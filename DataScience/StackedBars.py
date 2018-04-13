# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)
#create your plot here
plt.figure(figsize=(10,8))

p1 = plt.bar(range(len(unit_topics)), As, 0.4)
p2 = plt.bar(range(len(unit_topics)), Bs, 0.4,bottom=As)
p3 = plt.bar(range(len(unit_topics)), Cs, 0.4,bottom=c_bottom)
p4 = plt.bar(range(len(unit_topics)), Ds, 0.4,bottom=d_bottom)
p5 = plt.bar(range(len(unit_topics)), Fs, 0.4,bottom=f_bottom)
plt.show()