# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:33:29 2022

@author: TonyE
"""

from scipy import stats
import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace (-10,10,100)
y = stats.norm.pdf (x)

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