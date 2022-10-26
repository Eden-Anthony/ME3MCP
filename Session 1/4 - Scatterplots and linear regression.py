# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:56:43 2022

@author: TonyE
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.tsa.tsatools import lagmat

#Histograms
df = pd.read_csv('faithful.csv')   
n = df.shape[0]
lagduration = lagmat(df['duration'], maxlag = 1)

fig, ax = plt.subplots(sharex = True, sharey = True)
ax.scatter(x= lagduration, y = df['waiting'], marker='o')
lagmatrix = lagmat(df['duration'], maxlag=1, use_pandas=True)['duration.L.1']
xtest = lagmatrix[1:]

#print(lagduration.T*np.ones (n))
B = np.polyfit(x = lagduration.T[0][1:], y = df['waiting'][1:], deg = 1 )

x_vals = np.linspace(0,5,2)
y_vals = B[1] + B[0]*lagduration[1:]

ax.plot(lagduration[1:], y_vals, color = 'red')
ax.set_xlabel ('Previous Duration')
ax.set_ylabel ('Wait time (mins)')
ax.set_xlim([0.5,5.5])
