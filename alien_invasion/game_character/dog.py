#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/23/2019 8:57 PM 
# File  : dog.py 
# IDE   : PyCharm

# 12-2

import pygame


class Dog():

    def __init__(self, screen):
        """初始化小狗并设置其位置"""
        self.screen = screen

        # 加载小狗图像并获取其外接矩形
        self.image = pygame.image.load('images/dog.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将小狗图像放置到屏幕底部的中央
        self.rect.center = self.screen_rect.center
        # self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制小狗"""
        self.screen.blit(self.image, self.rect)
