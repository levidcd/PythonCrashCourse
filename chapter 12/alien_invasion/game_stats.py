#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   game_stats.py
@Time    :   2020/10/09 15:42:37
@Author  :   
@Version :   1.0
@Contact :   
@WebSite :   
@Desc    :          
'''
# Start typing your code from here
class GameStats:
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_stats = True
        self.game_active = True
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit