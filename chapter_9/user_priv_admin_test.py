#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 8:42 PM 
# File  : user_priv_admin_test.py 
# IDE   : PyCharm

# 9-11

from user_priv_admin_module import *

my_admin = Admin('weng', 'sway', 0, 'wuhan')
my_admin.privileges.show_privileges()