#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 10:34 AM 
# File  : sideshot_settings.py 
# IDE   : PyCharm

# 12-5


class Settings():
    """存储所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 游戏设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3