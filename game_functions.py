import pygame,sys

def check_events(ai_settings, ball):
    '''响应相应的鼠标和按键事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #速度控制
            check_speed_events(event, ai_settings)
        #改变窗体大小时的响应 -> 对应该改变程序中设定的窗体大小
        elif event.type == pygame.VIDEORESIZE:
            size = ai_settings.screen_width,ai_settings.screen_height = event.size[0],event.size[1]
            ai_settings.screen = pygame.display.set_mode(size,pygame.RESIZABLE)
        #鼠标
        check_mouse_events(event, ai_settings, ball)

def check_mouse_events(event, ai_settings, ball):
    '''鼠标控制'''
    if event.type == pygame.MOUSEBUTTONDOWN:  # 点击左键
        if event.button == 1:
            ball.still = True

    elif event.type == pygame.MOUSEBUTTONUP:  # 松开左键
        ball.still = False
        if event.button == 1:
            ball.ballrect = ball.ballrect.move(event.pos[0] - ball.ballrect.left, event.pos[1] - ball.ballrect.top)
    elif event.type == pygame.MOUSEMOTION:  # 按住左键
        if event.buttons[0] == 1:
            ball.ballrect = ball.ballrect.move(event.pos[0] - ball.ballrect.left, event.pos[1] - ball.ballrect.top)
    if pygame.display.get_active() and not ai_settings.still:
        ball.ballrect = ball.ballrect.move(ai_settings.speed)

def check_speed_events(event, ai_settings):
    '''方向键控制移动速度，ESC键退出'''
    if event.key == pygame.K_LEFT:
        ai_settings.speed[0] = ai_settings.speed[0] if ai_settings.speed[0] == 0 else (abs(
            ai_settings.speed[0]) - 1) * int(ai_settings.speed[0] / abs(ai_settings.speed[0]))
    elif event.key == pygame.K_RIGHT:
        ai_settings.speed[0] = ai_settings.speed[0] + 1 if ai_settings.speed[0] > 0 else ai_settings.speed[0] - 1
    elif event.key == pygame.K_UP:
        ai_settings.speed[1] = ai_settings.speed[1] + 1 if ai_settings.speed[1] > 0 else ai_settings.speed[1] - 1
    elif event.key == pygame.K_DOWN:
        ai_settings.speed[1] = ai_settings.speed[1] if ai_settings.speed[1] == 0 else (abs(
            ai_settings.speed[1]) - 1) * int(ai_settings.speed[1] / abs(ai_settings.speed[1]))
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def update_screen(screen, ai_settings, ball, bg_color):
    '''限制小球运动范围和刷新窗口'''
    #窗口最小化时停止运动，小球碰壁反弹
    if pygame.display.get_active():
        ball.ballrect = ball.ballrect.move(ai_settings.speed)
    if ball.ballrect.left < 0 or ball.ballrect.right > ai_settings.screen_width:
        ai_settings.speed[0] = - ai_settings.speed[0]
        if ball.ballrect.right > ai_settings.screen_width and ball.ballrect.right + ai_settings.speed[0] > ball.ballrect.right:
            ai_settings.speed[0] = - ai_settings.speed[0]
    if ball.ballrect.top < 0 or ball.ballrect.bottom > ai_settings.screen_height:
        ai_settings.speed[1] = - ai_settings.speed[1]
        if ball.ballrect.bottom > ai_settings.screen_height and ball.ballrect.bottom + ai_settings.speed[1] > ball.ballrect.bottom:#使小球不会卡在边缘上
            ai_settings.speed[1] = - ai_settings.speed[1]
    # 将color填充为背景色
    color(bg_color, ball, ai_settings)
    #screen.fill(ai_settings.color)
    screen.fill(bg_color)
    #将ball绘制在ballrect之上，让图像随着rect移动而移动
    screen.blit(ball.image, ball.ballrect)
    pygame.display.update()
    #pygame.display.flip() 比上面慢

def color(bg_color, ball, ai_settings):
    '''颜色控制'''
    bg_color.r = RGBChannel(ball.ballrect.left * 255 / ai_settings.screen_width)#水平距离
    bg_color.g = RGBChannel(ball.ballrect.top * 255 / ai_settings.screen_height)#垂直距离
    bg_color.b = RGBChannel(min(ai_settings.speed[0], ai_settings.speed[1]) * 255 / max(ai_settings.speed[0], ai_settings.speed[1],1))#最小速度/最大速度

def RGBChannel(a):
    '''将颜色参数限定为0 - 255之间的整数'''
    return 0 if a < 0 else (255 if a > 255 else int(a))