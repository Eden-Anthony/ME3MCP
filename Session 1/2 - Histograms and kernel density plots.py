# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:30:20 2022

@author: TonyE
"""

import pandas as pd
import numpy as np

#Histograms
df = pd.read_csv('faithful.csv')[['waiting','day']]    
#df_grouped = df.groupby('day').sum()
smallest_wait = df.min()
largest_wait = df.max()

Sturges_bin_size = 1 + int(np.log2(df.shape[0]))
bins = np.linspace (smallest_wait[0], largest_wait[0], 50)
histogram = df.hist(bins= bins, column = "waiting")[0][0]
histogram.set_title('')
histogram.set_xlabel('Wait Time')
histogram.set_ylabel('Frequency')

containers=histogram.containers[0]
freq = []
for rect in containers:
    freq.append(rect.get_height())
for rect in containers: freq.append(rect.get_height())
n = sum(freq)
relfreq = freq/n

wait_list = df['waiting'].values.tolist()
relfreq_hist = df.hist(bins= bins, column = "waiting", weights=np.ones_like(wait_list) / len(wait_list))[0][0]
relfreq_hist.set_title('Relative Frequnecies')
relfreq_hist.set_xlabel('Wait Time (mins)')

df['waiting'].plot.kde(ax = relfreq_hist)
#df['waiting'].plot.kde()
