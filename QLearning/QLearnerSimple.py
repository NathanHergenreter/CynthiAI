#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class QLearnerSimple:
    def __init__(self, qTable, alpha, discount):
        self.qTable = qTable
        self.alpha = alpha
        self.discount = discount
        
    def update(key, reward):
        curVal = qTable[key]
        qTable[key] = curVal + alpha * (reward + (discount * curVal) - curVal)

