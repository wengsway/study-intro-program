#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/23/2019 11:24 PM 
# File  : button_key.py 
# IDE   : PyCharm

# 12-4

import sys
import pygame


def button_key():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("12-4")
    bg_color = (255, 255, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bg_color = (255, 0, 255)
                elif event.key == pygame.K_DOWN:
                    bg_color = (0, 255, 255)
                elif event.key == pygame.K_LEFT:
                    bg_color = (255, 255, 0)
                elif event.key == pygame.K_RIGHT:
                    bg_color = (0, 0, 255)
        screen.fill(bg_color)
        pygame.display.flip()


button_key()
