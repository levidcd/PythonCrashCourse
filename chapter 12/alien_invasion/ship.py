import pygame


class Ship(object):
    '''管理飞船类'''

    def __init__(self, ai_game):
        '''初始化飞船设置初始位置'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 设定新飞船的位置
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        '''指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
