# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:06:45 2022

@author: ae1220
"""

import pandas as pd
import numpy as np
#import seaborn as sns

#Boxplots
df = pd.read_csv('faithful.csv')[['waiting','day']]    
overall_boxplot = df[['waiting']].boxplot()
boxplot = df.boxplot(by= 'day')
boxplot.set_title('')
boxplot.set_ylabel('Waiting time between successive eruptions (mins)')
boxplot.set_xlabel('Day')

#Histograms
smallest_wait = df.min()
largest_wait = df.max()

bins = np.linspace (smallest_wait[0], largest_wait[0], 50)
histogram = df.hist(bins= bins, column = "waiting")[0][0]
histogram.set_title('')
histogram.set_xlabel('Wait Time')
histogram.set_ylabel('Frequency')

containers=histogram.containers[0]
freq = []
for rect in containers:
    freq.append(rect.get_height())
