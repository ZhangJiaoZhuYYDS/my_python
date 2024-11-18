import pygame

# 1. 指定位置绘制图像
def test01():
    pygame.init()
    window = pygame.display.set_mode([512, 768])
    pygame.display.set_caption('飞机大战 v1.0')
    clock = pygame.time.Clock()

    # 1. 加载图像: 将图片加载到 PyGame 中，转换为 PyGame 对象
    image = pygame.image.load('demo.png')

    while True:
        # 2. 绘制图像
        window.blit(image, (0, 0))  # 默认绘制整个图像
        # window.blit(image, (100, 100), (0, 0, 70, 70))

        # 3. 刷新窗口
        pygame.display.update()

        clock.tick(60)

# 2. 绘制图像的移动
def test02():

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    pygame.display.set_caption('飞机大战 v1.0')
    clock = pygame.time.Clock()

    # 1. 加载图像: 将图片加载到 PyGame 中，转换为 PyGame 对象
    image = pygame.image.load('demo.png')
    position = [0, 0]

    while True:

        # 清空窗口
        # RGB (0, 255)
        window.fill((0, 0, 0))

        # 2. 绘制图像
        window.blit(image, position)  # 默认绘制整个图像

        # 计算下一次图像绘制的位置
        position[0] += 1
        position[1] += 1

        # 3. 刷新窗口
        pygame.display.update()

        clock.tick(60)


if __name__ == '__main__':
    test01()

