#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 10:10 AM 
# File  : side_shot.py 
# IDE   : PyCharm

# 12-5

import pygame
from pygame.sprite import Group

from sideshot_settings import Settings
from sideshot_ship import Ship
import side_game_functions as sgf


def run_game():
    """初始化游戏设置"""

    pygame.init()
    ss_settings = Settings()
    screen = pygame.display.set_mode((ss_settings.screen_width, ss_settings.screen_height))
    pygame.display.set_caption("Side Shot")

    ship = Ship(ss_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        sgf.check_events(ss_settings, screen, ship, bullets)
        ship.update()
        sgf.update_bullets(ss_settings, bullets)
        sgf.update_screen(ss_settings, screen, ship, bullets)


run_game()
