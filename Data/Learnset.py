#!/usr/bin/env python
# coding: utf-8

# In[18]:


import json
import sys


# In[19]:


def get_learnset_full():
    file = open(sys.path[0] + '/../Data/learnset.json')
    learnsetDict = json.load(file)
    file.close()
    return learnsetDict


def get_learnset_names():
    return get_learnset_full().keys()

# In[20]:


def get_learnset(pokemon):
    file = open(sys.path[0] + '/../Data/learnset.json')
    learnsetDict = json.load(file)
    file.close()
    return learnsetDict[pokemon.lower()]['learnset'].keys()

