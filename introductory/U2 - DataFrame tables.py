# -*- coding: utf-8 -*-
"""
Created on Sat Mar 03 07:30:34 2018

@author: theso
"""
import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name':['t-shirt','t-shirt','skirt','skirt'],
  'Color':['blue','green','red','black']
})

print df1