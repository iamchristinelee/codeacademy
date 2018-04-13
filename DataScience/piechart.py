# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

#Make your plot here

plt.figure(figsize=(10,8))
plt.pie(num_hardest_reported,labels = unit_topics,autopct='%d%%')
plt.axis('equal')
ax = plt.subplot()

plt.title('Hardest Topics')
#plt.xlabel('')
#plt.ylabel('')
plt.savefig('my_pie_chart.png')

plt.show()
