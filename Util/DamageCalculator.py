#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from poke_env.environment.weather import *
from Util.StatCalculator import *
from Data.Natures import *
from Data.TypeChart import *

# Returns amount of damage as a ratio of lost hp to target's full hp
def damage_calc_approx(user, userDex, target, targetDex, level, move, weather):
    power = move['basePower']
    
    atkBase = userDex['baseStats']['atk'] if move['category'] == 'Physical' else userDex['baseStats']['spa']
    atkEv = user['evs']['Atk'] if move['category'] == 'Physical' else user['evs']['SpA']
    atkIv = user['ivs']['Atk'] if move['category'] == 'Physical' else user['ivs']['SpA']
    atkNature = get_nature(user['nature'])
    atkNatureVal = atkNature['atk'] if move['category'] == 'Physical' else atkNature['spa']
    atk = non_hp_stat_calc(atkBase, atkEv, atkIv, level, atkNatureVal)
    
    defBase = targetDex['baseStats']['def'] if move['category'] == 'Physical' else targetDex['baseStats']['spd']
    defEv = target['evs']['Def'] if move['category'] == 'Physical' else target['evs']['SpD']
    defIv = target['ivs']['Def'] if move['category'] == 'Physical' else target['ivs']['SpD']
    defNature = get_nature(target['nature'])
    defNatureVal = defNature['def'] if move['category'] == 'Physical' else defNature['spd']
    dfn = non_hp_stat_calc(defBase, defEv, defIv, level, defNatureVal)
    
    weatherEff = weather_effect(weather, move['type'])
    stab = 1.5 if move['type'] in userDex['types'] else 1.0
    typeEff = get_type_weakness(targetDex['types'], [move['type']])
    
    hp = hp_stat_calc(targetDex['baseStats']['hp'], target['evs']['HP'], target['ivs']['HP'], level)
    randomAve = 1.85 / 2
    
    dmg = (( (((2 * level) / 5) + 2) * power * atk/dfn ) / 50 + 2) * weatherEff * stab * typeEff * randomAve
    
    return dmg / hp

def weather_effect(weather, moveType):
    if weather == Weather.RAINDANCE:
        if moveType == 'Water':
            return 1.5
        elif moveType == 'Fire':
            return 0.5
    elif weather == Weather.SUNNYDAY:
        if moveType == 'Fire':
            return 1.5
        elif moveType == 'Water':
            return 0.5
        
    return 1.0

