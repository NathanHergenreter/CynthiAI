#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


def get_abilities():
    file = open('abilities.json')
    abilitiesDict = json.load(file)
    file.close()
    return abilitiesDict

