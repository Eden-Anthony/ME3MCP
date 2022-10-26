# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:37:58 2022

@author: TonyE
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.tsa.tsatools import lagmat
from sklearn import cluster

#Histograms
df = pd.read_csv('faithful.csv')   
n = df.shape[0]
lagduration = lagmat(df['duration'], maxlag = 1)

fig, ax = plt.subplots(sharex = True, sharey = True)
ax.scatter(x= lagduration, y = df['waiting'], marker='o')
lag_df = df.copy()
lag_df['lag'] = lagduration
lag_df = lag_df[['waiting','lag']]
K = 2
C = cluster.KMeans (n_clusters = K, random_state = 0).fit(lag_df)
group_1 = lag_df.loc[C.labels_ == 0]
group_2 = lag_df.loc[C.labels_ == 1]
    
ax.scatter (x = group_1['lag'], y = group_1['waiting'], color = 'red')
ax.scatter (x = group_2['lag'], y = group_2['waiting'], color = 'green')
ax.set_xlabel ('Previous Duration')
ax.set_ylabel ('Wait time (mins)')