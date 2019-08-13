import pygame
from settings import Settings
from ball import Ball
import game_functions as gf

def run_game():

    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height),pygame.RESIZABLE)
    pygame.display.set_caption("壁球游戏")
    #载入图标
    icon = pygame.image.load("icon.jpg")
    pygame.display.set_icon(icon)
    #创建一个小球
    ball = Ball()
    fclock = pygame.time.Clock()# 帧数刷新速度控制

 #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, ball)
        #每次循环重绘屏幕，让最近的屏幕可见
        gf.update_screen(screen, ai_settings, ball)
        fclock.tick(ai_settings.fps)#每秒钟进行fps次帧刷新

run_game()
