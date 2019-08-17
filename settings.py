import pygame

class Settings():
    '''存储《控制球游戏》的所有设置的类'''

    def __init__(self):
        '''初始化游戏设置'''
        #屏幕设置
        self.screen_width = 600
        self.screen_height = 400
        self.color = (0,0,0)
        self.fps = 300 #每秒帧率参数
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("壁球游戏")

        #球的设置
        self.speed = [1,1]
        self.still = False