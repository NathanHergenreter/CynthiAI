#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import sys


# In[3]:


def get_moves():
    file = open(sys.path[0] + '/../Data/moves.json')
    movesDict = json.load(file)
    file.close()
    return movesDict


# In[6]:


def get_move(move):
    return get_moves()[move.lower()]


# In[10]:


def get_moves_names():
    return get_moves().keys()

