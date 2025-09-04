"""如何使用 PyGame 创建游戏主窗口"""
import pygame
import os  # 66666

if __name__ == '__main__':

    # 1. PyGame 模块初始化
    pygame.init()

    # 2. 创建窗口
    window = pygame.display.set_mode([512, 768])

    # 3. 设置标题
    pygame.display.set_caption('飞机大战 v1.0')

    # 4. 窗口循环
    # 一秒钟循环100次，对于游戏叫做 帧率
    clock = pygame.time.Clock()
    while True:

        # 希望循环尽量保持在一秒钟 60 次
        clock.tick(60)
