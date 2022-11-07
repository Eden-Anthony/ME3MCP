# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:33:29 2022

@author: TonyE
"""

from scipy import stats
import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace (-10,10,100)
y = stats.norm.pdf (x,1,2)

fig,ax = plt.subplots()
ax.plot (x,y)
ax.set_title ("Probability Distribution")
ax.set_xlabel("x")
ax.set_ylabel("P(X = x)")


fig,ax2 = plt.subplots()
ax2.plot (x,stats.norm.cdf(x))
ax2.set_title ("Cumulative Distribution")
ax2.set_xlabel("x")
ax2.set_ylabel("P(X <= x)")

sampleSets = [100,200,500,1000]

for samples in sampleSets:
    
    x3 = np.random.normal(1,2,samples)
    fig, ax3, = plt.subplots()
    counts, bins, bars = ax3.hist(x3) #Plot randomly generated distribution
    newBins = np.zeros(len(counts))
    ax3.set_xlabel("n")
    ax3.set_ylabel("Frequency")
    title = "Samples = " + str(samples) 
    ax3.set_title(title)
    ax3.plot(x,y*samples, 'r') #Plot true distribution
    for j in range (0,len(bins)-1):
        newBins[j] = (bins[j]+bins[j+1])*0.5
    
    n = sum(counts)
    total= sum(counts*newBins)
    sampleMean = total/n
    sampleVariance = (1/(n-1))*sum((counts*newBins**2)- sampleMean**2)
