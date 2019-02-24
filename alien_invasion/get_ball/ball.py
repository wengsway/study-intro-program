#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/24/2019 1:57 PM 
# File  : ball.py
# IDE   : PyCharm

# 13-5 and 13-6

from pygame.sprite import Sprite
from random import randint
import pygame


class Ball(Sprite):
    """docstring for Ball"""

    def __init__(self, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('E:/Desktop/python_introduction_to_programming/alien_invasion/images/ball.bmp')
        self.rect = self.image.get_rect()

        # 设置位置
        self.rect.x = randint(0, self.screen_rect.right - self.rect.width)
        self.rect.y = 0

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

