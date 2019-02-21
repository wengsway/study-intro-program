#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 8:47 PM 
# File  : several_module_test.py 
# IDE   : PyCharm


from user_module import User
from priv_admin_module import Admin, Privileges

my_admin = Admin('weng', 'sway', 0, 'wuhan')
my_admin.privileges.show_privileges()
