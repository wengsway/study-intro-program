#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:04 PM 
# File  : cities.py 
# IDE   : PyCharm

cities = {
    'shanghai': {
        'country': 'china',
        'population': '3000',
        'fact': 'very big'
    },
    'london': {
        'country': 'england',
        'population': '2000',
        'fact': 'more fog'
    },
    'new york': {
        'country': 'america',
        'population': '2500',
        'fact': 'big'}
}
for city, info in cities.items():
    print("\n" + city.title() + "'s information are:")
    print("\tcountry: " + info['country'].title())
    print("\tpopulation: " + str(info['population']))
    print("\tfact: " + info['fact'])
