#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 2:58 PM 
# File  : show_rains.py
# IDE   : PyCharm

# 13-3 and 13-4

import pygame
from pygame.sprite import Group

from rain_settings import Settings
from rain import Rain
import rain_functions as rf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # 设置游戏窗口左上角的标题
    pygame.display.set_caption("Raining Show")
    # 创建一个雨滴编组
    rains = Group()
    # 创建雨滴族群
    rf.create_fleet(settings, screen, rains)

    # 开始游戏的主循环
    while True:
        rf.check_keys()
        rf.change_direction(settings, rains)
        rf.continue_rains(settings, screen, rains)
        rf.update_screen(settings, screen, rains)


run_game()
