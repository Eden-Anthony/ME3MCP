# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:13:47 2022

@author: TonyE
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Histograms
df = pd.read_csv('faithful.csv')   
fig, axes = plt.subplots(3,5, sharex = True, sharey = True)

count = 1

for i in range (0, 3):
    for j in range (0,5):
        ax = axes[i][j]
        sub_df = df[df['day'] == count]
        sub_df['x1'] = [x for x in range(1, sub_df.shape[0]+1)]
        #print(sub_df['x1'])
        scatter_plot = sub_df.plot.line(y = 'waiting',x = 'x1', ax = ax, fontsize = 8, legend = None)
        
        scatter_plot.set_xlabel ('Eruption num')
        scatter_plot.set_title ('Day ' + str(count), fontsize = 8)
        count += 1
        #print (sub_df.tail())
