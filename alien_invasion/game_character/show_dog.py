#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/23/2019 9:05 PM 
# File  : show_dog.py 
# IDE   : PyCharm

# 12-2

import sys
import pygame

from dog import Dog


def show_dog():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Show Dog")

    my_dog = Dog(screen)

    while True:
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 255, 0))
        my_dog.blitme()

        pygame.display.flip()


show_dog()
