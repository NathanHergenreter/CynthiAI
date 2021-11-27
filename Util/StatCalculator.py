#!/usr/bin/env python
# coding: utf-8

import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

def non_hp_stat_calc(base, ev, iv, level, natureVal):
    return (((2 * base + (ev / 4) + iv) * level) / 100 + 5) * natureVal

def hp_stat_calc(base, ev, iv, level):
    return ((2 * base + (ev / 4) + iv) * level) / 100 + level + 10
