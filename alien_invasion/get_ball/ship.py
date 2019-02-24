#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/23/2019 8:11 PM 
# File  : ship.py 
# IDE   : PyCharm

# 13-5 and 13-6

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """docstring for Ship"""

    def __init__(self, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('E:/Desktop/python_introduction_to_programming/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_left = False
        self.moving_right = False

    def update_ship(self):
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= 2
        if self.moving_right:
            self.rect.x += 2

    def bliteme(self):
        self.screen.blit(self.image, self.rect)
