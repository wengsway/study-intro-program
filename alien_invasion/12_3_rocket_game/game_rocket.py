#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/23/2019 10:51 PM 
# File  : game_rocket.py 
# IDE   : PyCharm

import pygame

from rocket_settings import RocketSettings
from rocket import Rocket
import rocket_function as rf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    rocket_settings = RocketSettings()
    screen = pygame.display.set_mode((rocket_settings.screen_width, rocket_settings.screen_height))
    # 设置游戏窗口左上角的标题
    pygame.display.set_caption("Rocket Game")

    # 创建一个火箭
    rocket = Rocket(screen)

    # 开始游戏的主循环
    while True:
        rf.check_events(rocket)
        rocket.update()
        rf.update_screen(rocket_settings, screen, rocket)


run_game()