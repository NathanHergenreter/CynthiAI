#!/usr/bin/env python
# coding: utf-8

import json
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

table_record_file_dir = sys.path[0] + '/../ActionSelectionTable/Records/SwitchOutStateSelectionTable.json'

from QLearning.QLearnerSwitchOutState import *

# Table is predefined, only table values should be modified!!!
def get_speed_advantage_keys():
    return ['firstTurn', 'secondTurn']

def get_rem_hits_keys():
    return ['one', 'two', 'three', 'four', 'five', 'six', 'n']

def get_rem_hits_ratio():
    return [1.00, 0.50, 0.34, 0.25, 0.20, 0.17, 0.0]

# Returns existing switch-out-by-state selection table recorded as json
# If no json exists, returns empty dictionary
def get_switch_out_state_selection_table():
    try:
        with open(table_record_file_dir, 'r') as file:
            switchOutStateSelectionTable = json.load(file)
    except IOError as e:
        reset_switch_out_state_selection_table_record()
        switchOutStateSelectionTable = get_switch_out_state_selection_table()
        
    return switchOutStateSelectionTable

def record_switch_out_state_selection_table(table):
    with open(table_record_file_dir, 'w') as file:
        json.dump(table, file)

def reset_switch_out_state_selection_table_record():
    table = dict()
    keys = get_rem_hits_keys()
    ratios = get_rem_hits_ratio()
    oppKeys = get_rem_hits_keys()
    oppRatios = get_rem_hits_ratio()
    
    for turnKey in get_speed_advantage_keys():
        turnKeyDict = dict()
        for i in range(7):
            remHitsKeyDict = dict()
            for i in range(7):
                remHitsKeyDict[oppKeys[i]]['reward'] = 0
                remHitsKeyDict[oppKeys[i]]['ratio'] = oppRatios[i]

            turnKeyDict = { 'opponent': remHitsKeyDict, 'ratio': ratios[i] }
        table[turnKey] = turnKeyDict  
    
    record_switch_out_state_selection_table(table)
    
def get_switch_out_state_q_learner(alpha, discount):
    return QLearnerSwitchOutState(get_switch_out_state_selection_table(), alpha, discount)

