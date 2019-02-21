#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 2:19 PM 
# File  : making_pizzas.py 
# IDE   : PyCharm

"""
# 导入整个模块
import pizza_module

pizza_module.make_pizza(16, 'apple', 'pear', 'beef')
"""
"""
# 导入模块中的某一个或多个（逗号相隔）函数
from pizza_module import make_pizza

make_pizza(16,'apple','pear','beef','water')
"""
"""
# 给导入的模块的某个函数取别名
from pizza_module import make_pizza as mp

mp(16, 'apple', 'beef')
"""
"""
# 给整个模块取别名
import pizza_module as p

p.make_pizza(16, 'apple', 'beef')
"""
# 导入模块中的所有函数
from pizza_module import *

make_pizza(16,'apple')
