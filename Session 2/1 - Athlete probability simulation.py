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
    drugTakerFirst = np.random.randint(1,10,100)
    drugTakerFirst= drugTakerFirst == 1 # filter array
    drugTakerSecond = np.random.randint(1,10,100)
    drugTakerSecond= drugTakerSecond == 1 # filter array
    correctIDFirst = np.random.randint(1,10,100)
    correctIDFirst = correctIDFirst > 2 # filter array
    correctIDSecond = np.random.randint(1,10,100)
    correctIDSecond = correctIDSecond > 2 # filter array
    #apply logic to check failure (drugTaker and correctID) or (not drugTaker and not correctID)
    failedFirst = np.logical_or(np.equal(drugTakerFirst,correctIDFirst),np.equal(np.logical_not(drugTakerFirst),np.logical_not(correctIDFirst)))
    failedSecond = np.logical_or(np.equal(drugTakerSecond,correctIDSecond),np.equal(np.logical_not(drugTakerSecond),np.logical_not(correctIDSecond)))
    failedBoth = np.equal(failedFirst,failedSecond) # Check if failed both tests
    count = np.count_nonzero(failedBoth == True)
    failureOutcomes[i] = count
    
fig, ax = plt.subplots()
plt.hist(failureOutcomes)
ax.set_xlabel("Number of Failure Outcomes")
ax.set_ylabel ("Frequency")

# Bayes Theorem, drugTaker = D, correct ID = I



