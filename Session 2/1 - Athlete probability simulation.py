# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:51:54 2022

@author: TonyE
"""

import numpy as np
import matplotlib.pyplot as plt

simulations = 1000
failureOutcomes = np.zeros(simulations)

for i in range (0,simulations):
    drugTaker = np.random.randint(1,10,100)
    drugTaker= drugTaker == 1 # filter array
    correctID = np.random.randint(1,10,100)
    correctID = correctID > 2 # filter array
    #apply logic to check failure (drugTaker and correctID) or (not drugTaker and not correctID)
    failed = np.logical_or(np.equal(drugTaker,correctID),np.equal(np.logical_not(drugTaker),np.logical_not(correctID)))
    count = np.count_nonzero(failed == True)
    failureOutcomes[i] = count
    
fig, ax = plt.subplots()
plt.hist(failureOutcomes)
ax.set_xlabel("Number of Failure Outcomes")
ax.set_ylabel ("Frequency")


