import json
from pygal import *
from pygal.style import RotateStyle

from pygal_maps_world.maps import COUNTRIES
from pygal_maps_world.maps import World



def get_country_name(country_name):
    """returns for distinct country its 2-latters code for Pygal"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if country wasnt finded, it would return None
    return None
 
# coping data from file to list pop_data
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_population = {}
# population of per country   
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_name(country_name)
        if code:
            cc_population[code] = population
        else:
            print("Error - " + country_name)
            
        # grouping countries by 3 types of pipulations
        cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
        for cc, pop in cc_population.items():
            if pop < 10000000:   # 10 000 000
                cc_pop_1[cc] = pop
            elif pop < 1000000000 : # 1 000 000 000
                cc_pop_2[cc] = pop
            else:
                cc_pop_3[cc] = pop

wm_style = RotateStyle('#336699')

wm = World(style = wm_style)
wm.title = 'World population in 2010, By countries'
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('word_pop_by_groups_wm_style.svg')



