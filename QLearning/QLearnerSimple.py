#!/usr/bin/env python
# coding: utf-8

class QLearnerSimple:
    def __init__(self, qTable, alpha, discount):
        self.qTable = qTable
        self.alpha = alpha
        self.discount = discount
        
    def update(self, key, reward):
        curVal = self.qTable[key] if key in self.qTable else 0
        self.qTable[key] = curVal + self.alpha * (reward + (self.discount * curVal) - curVal)

