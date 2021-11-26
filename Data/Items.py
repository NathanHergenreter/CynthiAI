#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import sys


# In[14]:


def get_items():
    file = open(sys.path[0] + '/../Data/items.json')
    itemsDict = json.load(file)
    file.close()
    return itemsDict

