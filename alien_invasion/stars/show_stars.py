#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 2:58 PM 
# File  : show_rains.py
# IDE   : PyCharm

# 13-1 and 13-2

import pygame
from pygame.sprite import Group

from star_settings import Settings
import star_functions as sf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # 设置游戏窗口左上角的标题
    pygame.display.set_caption("Stars Show")
    # 创建一个星星编组
    stars = Group()
    # 创建星星人群
    sf.create_fleet(settings, screen, stars)

    # 开始游戏的主循环
    while True:
        sf.check_keys()
        sf.update_screen(settings, screen, stars)


run_game()
