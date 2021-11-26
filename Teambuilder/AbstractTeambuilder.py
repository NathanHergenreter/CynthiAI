#!/usr/bin/env python
# coding: utf-8

# In[19]:


import random
import numpy as np

import os
import sys
import abc

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)


# In[18]:


from poke_env.teambuilder.teambuilder import Teambuilder

from TeamSelectionTable.AbilitySelectionQTable import *
from TeamSelectionTable.ItemSelectionQTable import *
from TeamSelectionTable.MoveSelectionQTable import *
from TeamSelectionTable.NatureSelectionQTable import *
from TeamSelectionTable.PokemonSelectionQTable import *


# In[22]:


class AbstractTeambuilder(Teambuilder):
    
    @staticmethod
    def GetEVsDict():
        return { 'HP': 0, 'Atk': 0, 'SpA': 0, 'Def': 0, 'SpD': 0, 'Spe': 0 }
    
    @staticmethod
    def GetPokemonString(pokemon, gender, item, ability, evs, nature, moves):
        pokemonString = ''
        pokemonString += pokemon
        pokemonString += ' ' + '(' + gender.capitalize() + ')'
        pokemonString += ' @ ' + item.lower().title() + '\n'
        
        pokemonString += 'Ability: ' + ability.lower().title() + '\n'
        
        pokemonString += 'EVs: '
        evsString = []
        if(evs['HP'] > 0): evsString.append(str(evs['HP']) + ' HP')
        if(evs['Atk'] > 0): evsString.append(str(evs['Atk']) + ' Atk')
        if(evs['SpA'] > 0): evsString.append(str(evs['SpA']) + ' SpA')
        if(evs['Def'] > 0): evsString.append(str(evs['Def']) + ' Def')
        if(evs['SpD'] > 0): evsString.append(str(evs['SpD']) + ' SpD')
        if(evs['Spe'] > 0): evsString.append(str(evs['Spe']) + ' Spe')
        evsString = ' / '.join(evsString)
        pokemonString += evsString + '\n'
            
        pokemonString += nature.capitalize() + ' Nature\n'
        
        pokemonString += '- ' + moves[0].lower().title() + '\n'
        pokemonString += '- ' + moves[1].lower().title() + '\n'
        pokemonString += '- ' + moves[2].lower().title() + '\n'
        pokemonString += '- ' + moves[3].lower().title() + '\n'
        
        return pokemonString
        
    @staticmethod
    def CombineTeam(pokemon_list):
        teamString = ''
        for mon in pokemon_list:
            teamString += '\n' + mon
            
        return teamString
    
    @staticmethod
    def RandomGender(pokemon_dex):
        if 'gender' in pokemon_dex:
            return pokemon_dex['gender']
        
        if 'genderRatio' in pokemon_dex:
            genders = pokemon_dex['genderRatio'].keys()
            gendersArr = np.asarray(list(genders))
            firstGenderChance = list(pokemon_dex['genderRatio'].values())[0]
            return gendersArr[0] if random.uniform(0,1) > firstGenderChance else gendersArr[1]
        
        return 'M' if random.randint(0,1) == 0 else 'F'
            
    @abc.abstractmethod
    def yield_team(self):
        return
