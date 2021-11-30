#!/usr/bin/env python
# coding: utf-8

import json
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

table_record_file_dir = sys.path[0] + '/../TeamSelectionTable/Records/AbilitySelectionTable.json'

from QLearning.QLearnerSimple import *

# Returns existing ability selection table recorded as json
# If no json exists, returns empty dictionary
def get_ability_selection_table():
    try:
        with open(table_record_file_dir, 'r') as file:
            abilitySelectionTable = json.load(file)
    except IOError as e:
        abilitySelectionTable = dict()
        
    return abilitySelectionTable

def record_ability_selection_table(table):
    with open(table_record_file_dir, 'w') as file:
        json.dump(table, file)

def reset_ability_selection_table_record():
    record_ability_selection_table(dict())
    
def get_ability_q_learner(alpha, discount):
    return QLearnerSimple(get_ability_selection_table(), alpha, discount)

