#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import sys


# In[4]:


def get_natures():
    return get_natures_full().keys()


# In[5]:


def get_natures_full():
    file = open(sys.path[0] + '/../Data/natures.json')
    naturesDict = json.load(file)
    file.close()
    return naturesDict

