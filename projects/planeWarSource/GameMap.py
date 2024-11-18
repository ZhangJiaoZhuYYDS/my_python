import random
import pygame
from Config import *


class GameMap:

    def __init__(self, scene):

        # 持有窗口对象
        self.scene = scene

        # 加载地图资源
        map_index = MAP_INDEX if MAP_INDEX >= 1 and MAP_INDEX <= 5 else random.randint(1, 5)
        map_filename = f'source/map/map-{map_index}.jpg'
        self.image1 = pygame.image.load(map_filename)
        self.image2 = self.image1.copy()

        # 图片位置
        self.y1 = 0
        self.y2 = -SCREEN_H

        # 地图滚动速度
        self.scroll_speed = 3


    def draw_element(self):
        """绘制地图所需要的图像到窗口上"""
        self.scene.blit(self.image1, (0, self.y1))
        self.scene.blit(self.image2, (0, self.y2))


    def calc_position(self):
        """计算需要绘制的图像的位置"""

        self.y1 += self.scroll_speed
        if self.y1 >= SCREEN_H:
            self.y1 = 0

        self.y2 += self.scroll_speed
        if self.y2 >= 0:
            self.y2 = -SCREEN_H





















