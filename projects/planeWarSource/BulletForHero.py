import math

import pygame

from Bullet import Bullet


class BulletForHero:

    def __init__(self, scene):
        # 初始化子弹列表
        self.bullet_list = [Bullet(scene) for _ in range(15)]
        # 控制子弹发射间隔（帧）
        self.frame_limit = 8
        self.frame_index = 0

    def calc_position(self):
        for bullet in self.bullet_list:
            bullet.move(0, -15)

    def draw_element(self):
        for bullet in self.bullet_list:
            bullet.draw_element()

    def shoot(self, start_x, start_y, shoot_number):
        """
        :param start_x: 飞机的位置
        :param start_y: 飞机的位置
        :param shoot_number: 发射子弹数量
        :return:
        """

        self.frame_index += 1
        if self.frame_index < self.frame_limit:
            return
        self.frame_index = 0

        # 计算子弹初始位置
        distance = 31
        middle = math.floor(shoot_number / 2)
        position_xs = [start_x + (index - middle) * distance for index in range(shoot_number)]

        # 选择子弹
        wait_for_shoot = []
        for bullet in  self.bullet_list:
            if not bullet.visible:
                wait_for_shoot.append(bullet)
            if len(wait_for_shoot) == shoot_number:
                break

        # 发射子弹
        if len(wait_for_shoot) == shoot_number:
            for bullet, x in zip(wait_for_shoot, position_xs):
                bullet.set_used(x - bullet.bbox[2]/2, start_y - bullet.bbox[3])


if __name__ == '__main__':

    # 1. 创建窗口
    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 2. 创建弹夹类
    bullets = BulletForHero(window)
    while True:

        window.fill((0, 0, 0))

        # 计算子弹坐标
        bullets.calc_position()
        # 绘制子弹
        bullets.draw_element()
        # 发射子弹
        bullets.shoot(200, 600, 3)

        # 读取所有事件并丢弃
        pygame.event.get()

        pygame.display.update()
        clock.tick(60)


