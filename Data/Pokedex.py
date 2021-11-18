#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import sys


# In[2]:


def get_dex():
    file = open(sys.path[0] + '/../Data/pokedex.json')
    dexDict = json.load(file)
    file.close()
    return dexDict


# In[17]:


def get_dex_pokemon(pokemon):
    return get_dex()[pokemon.lower()]


# In[15]:


def extraneous_form(form):
    return form == 'Alola' or form == 'Galar'

def get_pokemon():
    dexDict = get_dex()
    
    filteredDex = dict()
    for key, value in dexDict.items():
        isValid = value['num'] > 0
        # Checks if form is not regional, if so does not add to filtered dex
        if 'forme' in value:
            isValid = isValid and extraneous_form(value['forme'])
        if isValid:
            filteredDex[key] = value
                
    return filteredDex.keys()

