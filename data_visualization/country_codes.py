#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/28/2019 5:03 PM 
# File  : country_codes.py 
# IDE   : PyCharm

from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Congo, Rep.':
            return 'cg'
        elif country_name == 'Dominica':
            return 'do'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Hong Kong SAR, China':
            return 'hk'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Kiribati':
            return 'ki'
        elif country_name == 'Qatar':
            return 'qa'
        elif country_name == 'Vanuatu':
            return 'vu'
        elif country_name == 'West Bank and Gaza':
            return 'wb'
        elif country_name == 'Tuvalu':
            return 'tu'
        elif country_name == 'Trinidad and Tobago':
            return 'tt'
        elif country_name == 'Tonga':
            return 'ta'
        elif country_name == 'Barbados':
            return 'bb'
        elif country_name == 'Fiji':
            return 'fj'
        elif country_name == 'Grenada':
            return 'gd'
        elif country_name == 'Kosovo':
            return 'kv'
        elif country_name == 'Marshall Islands':
            return 'mi'
        elif country_name == 'Micronesia, Fed. Sts.':
            return 'mf'
        elif country_name == 'Nauru':
            return 'nr'
        elif country_name == 'Northern Mariana Islands':
            return 'nm'
        elif country_name == 'Palau':
            return 'pu'
        elif country_name == 'Samoa':
            return 'su'
        elif country_name == 'Solomon Islands':
            return 'ss'
        elif country_name == 'American Samoa':
            return 'as'
        elif country_name == 'Antigua and Barbuda':
            return 'ab'
        elif country_name == 'Bahamas, The':
            return 'bm'
        elif country_name == 'Cabo Verde':
            return 'cb'
        elif country_name == 'Comoros':
            return 'cs'
        elif country_name == 'St. Kitts and Nevis':
            return 'kn'
        elif country_name == 'St. Lucia':
            return 'lc'
        elif country_name == 'St. Vincent and the Grenadines':
            return 'vg'
    # 如果没有找到指定的国家，就返回None
    return None

