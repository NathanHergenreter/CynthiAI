#!/usr/bin/env python
# coding: utf-8

import json
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

table_record_file_dir = sys.path[0] + '/../ActionSelectionTable/Records/MoveTargetSelectionTable.json'

from QLearning.QLearnerSimplePokemon import *

# Returns existing move-by-target-pokemon selection table recorded as json
# If no json exists, returns empty dictionary
def get_move_target_selection_table():
    try:
        with open(table_record_file_dir, 'r') as file:
            moveTargetSelectionTable = json.load(file)
    except IOError as e:
        moveTargetSelectionTable = dict()
        
    return moveTargetSelectionTable

def record_move_target_selection_table(table):
    with open(table_record_file_dir, 'w') as file:
        json.dump(table, file)

def reset_move_target_selection_table_record():
    record_move_target_selection_table(dict())
    
def get_move_target_q_learner(alpha, discount):
    return QLearnerSimplePokemon(get_move_target_selection_table(), alpha, discount)
