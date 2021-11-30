#!/usr/bin/env python
# coding: utf-8

import json
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

table_record_file_dir = sys.path[0] + '/../ActionSelectionTable/Records/MoveDamageSelectionTable.json'

from QLearning.QLearnerMoveDamage import *

def get_keys():
    return ['one', 'two', 'three', 'four', 'five', 'six', 'n']

def get_ratio():
    return [1.00, 0.50, 0.34, 0.25, 0.20, 0.17, 0.0]

# Returns existing move-by-damage selection table recorded as json
# If no json exists, returns empty dictionary
def get_move_damage_selection_table():
    try:
        with open(table_record_file_dir, 'r') as file:
            moveDamageSelectionTable = json.load(file)
    except IOError as e:
        reset_move_damage_selection_table()
        moveDamageSelectionTable = get_move_damage_selection_table()
        
    return moveDamageSelectionTable

def record_move_damage_selection_table(table):
    with open(table_record_file_dir, 'w') as file:
        json.dump(table, file)

def reset_move_damage_selection_table():
    new_table = dict()
    keys = get_keys()
    ratios = get_ratio()
    
    for i in range(7):
        dmg_dict = { 'reward': 0, 'ratio': ratios[i] }
        new_table[keys[i]] = dmg_dict
    
    record_move_damage_selection_table(new_table)
    
def get_move_damage_q_learner(alpha, discount):
    return QLearnerMoveDamage(get_move_target_selection_table(), alpha, discount)

