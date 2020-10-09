#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   settings.py
@Time    :   2020/10/05 19:06:07
@Author  :   
@Version :   1.0
@Contact :   
@WebSite :   
@Desc    :          
'''
# Start typing your code from here


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5
        self.ship_limit = 3
        
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        
        # 1 right  -1 left 
        self.fleet_direction = 1

        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        
