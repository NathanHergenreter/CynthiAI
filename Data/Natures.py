#!/usr/bin/env python
# coding: utf-8

import json
import sys

def get_natures():
    return get_natures_full().keys()

def get_natures_full():
    file = open(sys.path[0] + '/../Data/natures.json')
    naturesDict = json.load(file)
    file.close()
    return naturesDict

def get_nature(nature):
    return get_natures_full()[nature]
