#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/20/2019 8:47 PM 
# File  : priv_admin_module.py 
# IDE   : PyCharm

from user_module import User


class Admin(User):

    def __init__(self, first_name, last_name, login_attempts, location):
        super().__init__(first_name, last_name, login_attempts, location)
        self.privileges = Privileges()


class Privileges:

    def __init__(self, ):
        self.privileges = ["can add post", "can ban user", "can delete post"]

    def show_privileges(self):
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print(privilege)
