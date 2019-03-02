#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/2/2019 3:57 PM 
# File  : world_fdi.py 
# IDE   : PyCharm

# 16-7

import csv
import pygal.maps.world
from pygal.style import LightColorizedStyle, RotateStyle

from country_codes import get_country_code

filename = 'fdini.csv'
with open(filename) as f:
    reader = csv.reader(f)
    fdi = {}
    for index, row in enumerate(reader):
        if index > 4:
            country = row[0]
            code = get_country_code(country)
            fdi_data = int(float(row[60]) / 100000000)
            if code:
                fdi[code] = fdi_data
            else:
                print("ERROR - " + country)
        else:
            pass

# 将数据进行可视化
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World FDI Net Inflows in 2016, by Country, Current US$'
wm.add('FDI Net Inflows', fdi)

wm.render_to_file('world_fdi.svg')
