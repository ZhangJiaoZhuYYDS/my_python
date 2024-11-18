import pygame

# 1. 创建矩形
def test01():
    pygame.init()
    window = pygame.display.set_mode([512, 768])
    pygame.display.set_caption('飞机大战 v1.0')
    clock = pygame.time.Clock()

    # 创建矩形对象
    object = pygame.Rect(100, 200, 50, 50)

    while True:
        # 第一个参数: 矩形绘制的窗口
        # 第二个参数: 绘制矩形的颜色 RGB
        # 第三个参数: 绘制矩形的位置和尺寸
        pygame.draw.rect(window, (0, 0, 255), object)

        pygame.display.update()
        clock.tick(60)



# 2. 鼠标事件
def test02():

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    pygame.display.set_caption('飞机大战 v1.0')
    clock = pygame.time.Clock()

    # 创建矩形对象
    object = pygame.Rect(100, 200, 50, 50)


    is_drag = False
    while True:
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (0, 0, 255), object)

        # 当我们在窗口使用鼠标进行点击的时候，此时就会发生鼠标点击事件
        # PyGame 就会将所有的鼠标点击事件存储到一个列表中，我们只需要从列表中取出事件并处理即可

        # 获得当前这个帧发生的所有事件
        event_list = pygame.event.get()
        for event in event_list:
            # pygame.QUIT 表示事件的类型，窗口的关闭按钮被点击
            # event.type 获得当前遍历事件的类型
            if event.type == pygame.QUIT:
                pygame.display.quit()

            # 1. 判断鼠标(左键)点击到矩形上面，并且处于按下的状态
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 判断按下鼠标是否是左键
                if event.button == pygame.BUTTON_LEFT:
                    # 判断某个点是否在矩形内部
                    if object.collidepoint(event.pos):
                        is_drag = True


            # 2. 判断鼠标左键是否弹起
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    is_drag = False


            # 3. 鼠标拖动事件
            if event.type == pygame.MOUSEMOTION:
                if is_drag:
                    dx = event.pos[0] - object[0] - object[2]/2
                    dy = event.pos[1] - object[1] - object[3]/2
                    object.move_ip(dx, dy)  # ip inplace 就地修改


        pygame.display.update()
        clock.tick(60)


# 3. 键盘事件
def test03():
    pygame.init()
    window = pygame.display.set_mode([512, 768])
    pygame.display.set_caption('飞机大战 v1.0')
    clock = pygame.time.Clock()

    # 创建矩形对象
    object = pygame.Rect(100, 200, 50, 50)

    while True:

        window.fill((0, 0, 0))
        pygame.draw.rect(window, (0, 0, 255), object)


        # 获得所有的事件
        event_list = pygame.event.get()
        for event in event_list:
            # 窗口关闭事件
            if event.type == pygame.QUIT:
                pygame.display.quit()

            print(event.type)
            # 键盘事件
            # if event.type == pygame.KEYDOWN:
            # 获得键盘所有按键的状态
            keys = pygame.key.get_pressed()
            print(keys)
            speed = 10
            if keys[pygame.K_w]:
                object.move_ip(0, -speed)

            if keys[pygame.K_s]:
                object.move_ip(0, speed)

            if keys[pygame.K_a]:
                object.move_ip(-speed, 0)

            if keys[pygame.K_d]:
                object.move_ip(speed, 0)


        pygame.display.update()
        clock.tick(60)



if __name__ == '__main__':
    test03()
