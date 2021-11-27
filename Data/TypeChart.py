#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import sys

def get_types():
    file = open(sys.path[0] + '/../Data/typeChart.json')
    typesDict = json.load(file)
    file.close()
    return typesDict

def get_type(typ):
    typeKey = typ.lower().capitalize()
    typesDict = get_types()
    for typeDict in typesDict:
        if typeDict['name'] == typeKey:
            return typeDict
        
    return typesDict[0]

def get_type_effectiveness(typeOf, typeTarget):
    typeOfDict = get_type(typeOf)
    typeTargetDict = get_type(typeTarget)
    
    effectiveness = 1
    if typeTargetDict['name'] in typeOfDict['immunes']:
        effectiveness = 0
    elif typeTargetDict['name'] in typeOfDict['weaknesses']:
        effectiveness = 0.5
    elif typeTargetDict['name'] in typeOfDict['strengths']:
        effectiveness = 2
        
    return effectiveness

def get_type_effectiveness_two(typeOf, typeTarget1, typeTarget2):
    return get_type_effectiveness(typeOf, typeTarget1) * get_type_effectiveness(typeOf, typeTarget2)

def get_type_weakness(typesOf, typesOpponent):
    weakness = 1
    for typeOf in typesOf:
        for typeOpponent in typesOpponent:
            weakness *= get_type_effectiveness(typeOpponent, typeOf)
            
    return weakness

