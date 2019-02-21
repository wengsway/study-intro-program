#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 1:58 PM 
# File  : user_profile.py 
# IDE   : PyCharm


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile


user_profile = build_profile('weng', 'quan', location='wuhan', major='finance', age='23')
print(user_profile)
