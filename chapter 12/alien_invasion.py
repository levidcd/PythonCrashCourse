#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   alien_invasion.py
@Time    :   2020/10/05 17:15:38
@Author  :   
@Version :   1.0
@Contact :   
@WebSite :   
@Desc    :          
'''
# Start typing your code from here
import sys
import pygame


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

        # 设置背景色
        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 每次循环时重绘屏幕
            self.screen.fill(self.bg_color)

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
