import pygame

class Ball():

    def __init__(self):
        '''初始化小球'''
        #此游戏没有设定小球的初始位置
        #小球加载+获得rect对象
        self.image = pygame.image.load("timg.jpg")
        self.ballrect = self.image.get_rect()
