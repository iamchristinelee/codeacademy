# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 18:42:07 2018

@author: theso
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
print orders.head(10)
pricey_shoes=orders.groupby('shoe_type').price.max()

print pricey_shoes
print (type(pricey_shoes))

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print pricey_shoes
print type(pricey_shoes)