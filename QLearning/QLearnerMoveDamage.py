#!/usr/bin/env python
# coding: utf-8

class QLearnerMoveDamage(QLearnerSimple):
        
    def update(self, ratio, reward):
        numHitsKey = self.get_num_hits_key(ratio)
        curVal = self.qTable[numHitsKey]['reward']
        self.qTable[numHitsKey]['reward'] = curVal + self.alpha * (reward + (self.discount * curVal) - curVal)
        
    def get_num_hits_key(self, ratio):
        for key, value in self.qTable.items():
            if ratio >= value['ratio']:
                return key

