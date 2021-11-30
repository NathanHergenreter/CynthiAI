#!/usr/bin/env python
# coding: utf-8

class QLearnerSimplePokemon(QLearnerSimple):
        
    def update(self, pokemonKey, key, reward):
        curVal = self.qTable[key][pokemonKey] if key in self.qTable and pokemonKey in self.qTable[key] else 0
        self.qTable[key][pokemonKey] = curVal + self.alpha * (reward + (self.discount * curVal) - curVal)

