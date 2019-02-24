#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 8:27 PM 
# File  : game_status.py 
# IDE   : PyCharm

# 13-5 and 13-6


class GameStatus(object):
    """docstring for GameStatus"""

    def __init__(self):
        self.game_active = True
        self.total = 0
        self.catched = 0
        self.loss = 0

    def check_active(self):
        if self.loss == 3:
            self.game_active = False
