#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 10:02 PM 
# File  : alien.py 
# IDE   : PyCharm

# 5-3 and 5-4 and 5-5

alien_color = 'green'
if alien_color == 'green':
    print("You get five points.")
if alien_color == 'yellow':
    print('You lose five points.')

if alien_color == 'green':
    print('You get five points.')
else:
    print('You get ten points.')
if alien_color != 'green':
    print("You get ten points.")
else:
    print('You get five points.')
if alien_color == 'green':
    print('You get five points.')
elif alien_color == 'yellow':
    print('You get ten points.')
elif alien_color == 'red':
    print('You get fifteen points.')
else:
    print('You get nothing.')
