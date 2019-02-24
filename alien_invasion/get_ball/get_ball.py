#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/23/2019 7:50 PM 
# File  : get_ball.py
# IDE   : PyCharm

# 13-5 and 13-6

import pygame
import sys
from ship import Ship
from ball_functions import BallFunctions
from ball import Ball
from pygame.sprite import Group
from game_status import GameStatus


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("catch ball")
    bg_color = (255, 255, 255)
    ship = Ship(screen)
    function = BallFunctions()
    b = Group()
    ship = Group()
    game_status = GameStatus()
    while True:
        game_status.check_active()
        if game_status.game_active:
            function.update_screen(screen, ship, bg_color, b, game_status)
        else:
            sys.exit()


run()
