# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 12:12:19 2018

@author: theso
"""


import pandas as pd
df = pd.read_csv('employees.csv')

df['total_earned'] = df.apply(lambda row: row['hours_worked'] * row['hourly_wage'] if row['hours_worked'] <= 40 else (((row['hours_worked']-40)*row['hourly_wage']*1.5)+(40*row['hourly_wage'])),axis=1)


print df
