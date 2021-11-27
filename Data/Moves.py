#!/usr/bin/env python
# coding: utf-8

import json
import sys

def get_moves():
    file = open(sys.path[0] + '/../Data/moves.json')
    movesDict = json.load(file)
    file.close()
    return movesDict

def get_move(move):
    return get_moves()[move.replace(' ', '').lower()]

def get_moves_names():
    names_dict = dict()
    for key, value in get_moves().items():
        names_dict[key] = value['name']
    return names_dict

