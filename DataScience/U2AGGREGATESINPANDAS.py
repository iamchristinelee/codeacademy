import matplotlib.pyplot as plt
import numpy as np
import panda as pd

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

df = pd.read_csv('shoefly_page_visits.csv')
df.head(10)
df.groupby(['month', 'utm_source']).id.count().reset_index()
df.groupby(['month', 'utm_source']).id.count()\
    .reset_index()\
    .pivot(columns='month', index='utm_source', values='id')
    
