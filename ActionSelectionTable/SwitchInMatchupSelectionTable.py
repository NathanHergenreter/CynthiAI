#!/usr/bin/env python
# coding: utf-8

import json
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

table_record_file_dir = sys.path[0] + '/../ActionSelectionTable/Records/SwitchInMatchupSelectionTable.json'

# Returns existing switch-in-by-pokemon-matchup selection table recorded as json
# If no json exists, returns empty dictionary
def get_switch_in_matchup_selection_table():
    try:
        with open(table_record_file_dir, 'r') as file:
            switchInMatchupSelectionTable = json.load(file)
    except IOError as e:
        switchInMatchupSelectionTable = dict()
        
    return switchInMatchupSelectionTable

def record_switch_in_matchup_selection_table(table):
    with open(table_record_file_dir, 'w') as file:
        json.dump(table, file)

def reset_switch_in_matchup_selection_table_record():
    record_switch_in_matchup_selection_table(dict())

