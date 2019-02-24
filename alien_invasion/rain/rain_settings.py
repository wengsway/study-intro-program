#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 2:56 PM 
# File  : rain_settings.py
# IDE   : PyCharm

# 13-3 and 13-4

import pygame


class Settings:
    """存储雨滴的所有设置的类"""

    def __init__(self):
        """初始化设置"""
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 0, 255)
        self.drop_speed = 1
