import random

import pygame
from Config import *
from BulletForHero import BulletForHero


class HeroPlane:

    def __init__(self, scene):
        # 持有场景对象
        self.scene = scene
        # 加载图像资源
        self.image = pygame.image.load('source/plane/hero.png')
        # 获得飞机边框
        self.bbox = self.image.get_rect()
        # 飞机初始位置
        self.bbox[0] = SCREEN_W / 2 - self.bbox[2] / 2
        self.bbox[1] = SCREEN_H - self.bbox[3] - 10
        # 移动速度
        self.speed = 5
        # 初始化弹夹
        self.bullets = BulletForHero(scene)

    def top(self):
        if self.bbox[1] <= 0:
            return
        self.bbox.move_ip(0, -self.speed)

    def bottom(self):
        if self.bbox[1] >= SCREEN_H - self.bbox[3]:
            return
        self.bbox.move_ip(0, self.speed)

    def left(self):
        if self.bbox[0] <= 0:
            return
        self.bbox.move_ip(-self.speed, 0)

    def right(self):
        if self.bbox[0] >= (SCREEN_W - self.bbox[2]):
            return
        self.bbox.move_ip(self.speed, 0)

    def shoot(self, num):
        shoot_x = self.bbox[0] + self.bbox[2] / 2
        shoot_y = self.bbox[1]
        self.bullets.shoot(shoot_x, shoot_y, num)

    def draw_element(self):
        # 绘制飞机
        self.scene.blit(self.image, self.bbox)
        # 绘制子弹
        self.bullets.draw_element()

    def calc_position(self):
        # 只计算子弹坐标
        self.bullets.calc_position()


if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 初始化英雄飞机
    hero = HeroPlane(window)

    actions = [hero.top, hero.bottom, hero.left, hero.right]
    action_index = 0
    index = 0
    while True:
        # 清空屏幕
        window.fill((0, 0, 0))
        # 计算飞机子弹坐标
        hero.calc_position()
        # 绘制飞机和子弹
        hero.draw_element()
        # 发射子弹
        hero.shoot(3)

        # 随机选择方向
        actions[action_index]()
        index += 1
        if index > 50:
            action_index = random.randint(0, 3)
            index = 0

        pygame.event.get()
        pygame.display.update()
        clock.tick(60)
























