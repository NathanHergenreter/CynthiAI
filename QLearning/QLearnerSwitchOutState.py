#!/usr/bin/env python
# coding: utf-8

class QLearnerSwitchOutState(QLearnerSimple):
        
    def update(self, turn, ratio, ratioOpp, reward):
        numHitsKey = get_num_hits_key(ratio)
        oppNumHitsKey = get_num_hits_key(ratioOpp)
        
        curVal = self.qTable[turn][numHitsKey]['opponent'][oppNumHitsKey]['reward']
        self.qTable[turn][numHitsKey]['opponent'][oppNumHitsKey]['reward'] = curVal + self.alpha * (reward + (self.discount * curVal) - curVal)

    def get_num_hits_key(self, ratio):
        for key, value in self.qTable.items():
            if ratio >= value['ratio']:
                return key

