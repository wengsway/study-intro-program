#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 5:14 PM 
# File  : na_populations.py 
# IDE   : PyCharm

import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')