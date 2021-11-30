#!/usr/bin/env python
# coding: utf-8

class QLearnerSwitchInState(QLearnerSimple):
        
    def update(self, ratio, ratioOpp, reward):
        numHitsKey = get_num_hits_key(ratio)
        oppNumHitsKey = get_num_hits_key(ratioOpp)
        
        curVal = self.qTable[numHitsKey]['opponent'][oppNumHitsKey]['reward']
        self.qTable[numHitsKey]['opponent'][oppNumHitsKey]['reward'] = curVal + self.alpha * (reward + (self.discount * curVal) - curVal)

    def get_num_hits_key(self, ratio):
        for key, value in self.qTable.items():
            if ratio >= value['ratio']:
                return key

