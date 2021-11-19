#!/usr/bin/env python
# coding: utf-8

# In[30]:


import json
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
from Data.Learnset import *
from Data.Pokedex import *

table_record_file_dir = sys.path[0] + '/../TeamSelection/Records/MoveSelectionTable.json'


# In[31]:


# Returns existing move selection table recorded as json
# If no json exists, returns empty dictionary
def get_move_selection_table():
    try:
        with open(table_record_file_dir, 'r') as file:
            moveSelectionTable = json.load(file)
    except IOError as e:
        moveSelectionTable = dict()
        
    return moveSelectionTable


# In[33]:


def record_move_selection_table(table):
    with open(table_record_file_dir, 'w') as file:
        json.dump(table, file)


# In[36]:


def reset_move_selection_table_record():
    record_move_selection_table(dict())
