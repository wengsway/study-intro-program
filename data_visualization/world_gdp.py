#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/2/2019 1:16 PM 
# File  : world_gdp.py 
# IDE   : PyCharm

# 16-6

import json
import pygal.maps.world
from pygal.style import LightColorizedStyle, RotateStyle

from country_codes import get_country_code

# 读取数据文件
"""
扣除 Arab World、Euro area、High income 等 45 个地区。
"""
filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

# 获得各个国家的GDP数据
gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict["Year"] == 2016:
        country = gdp_dict["Country Name"]
        gdp = int(gdp_dict["Value"] / 1000000000)
        code = get_country_code(country)
        if code:
            gdps[code] = gdp
        else:
            print("ERROR - " + country)

# 将数据进行可视化
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World GDP in 2016, by Country'
wm.add('GDP in current USD, Billion', gdps)

wm.render_to_file('world_gdp.svg')
