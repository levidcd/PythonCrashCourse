#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   alien.py
@Time    :   2020/10/05 20:47:22
@Author  :   
@Version :   1.0
@Contact :   
@WebSite :   
@Desc    :          
'''
# Start typing your code from here
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('./images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)