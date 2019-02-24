#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 2/23/2019 8:27 PM 
# File  : ball_functions.py
# IDE   : PyCharm

# 13-5 and 13-6

import pygame
import sys
from ball import Ball
from ship import Ship
from time import sleep


class BallFunctions:

    def __init__(self):
        pass

    def check_event(self, ship):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    ship.moving_right = False

    def create_ball(self, ball, screen):
        if len(ball) == 0:
            b = Ball(screen)
            ball.add(b)
        else:
            pass

    def update_ball(self, ball, screen, ship, game_status):
        for b in ball:
            b.rect.y += b.speed
            if b.rect.y > b.screen_rect.bottom:
                ball.remove(b)
                game_status.loss += 1
        if pygame.sprite.groupcollide(ball, ship, True, False):
            sleep(0.5)

    def update_screen(self, screen, ship, bg_color, ball, game_status):
        screen.fill(bg_color)
        if len(ship) == 0:
            ship.add(Ship(screen))
        for h in ship:
            self.check_event(h)
            h.update_ship()
        ship.draw(screen)
        self.create_ball(ball, screen)
        self.update_ball(ball, screen, ship, game_status)
        ball.draw(screen)
        pygame.display.flip()


