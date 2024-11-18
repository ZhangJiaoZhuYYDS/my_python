import random
from Config import *
import pygame
from Bullet import Bullet
from Bomb import Bomb

class EnemyPlane:

    def __init__(self, scene, speed=10):
        # 持有场景对象
        self.scene = scene
        # 加载资源
        self.image = pygame.image.load(f'source/plane/enemy-{random.randint(1, 7)}.png')
        # 敌机边框
        self.bbox = self.image.get_rect()
        # 移动速度
        self.speed = speed
        # 是否可见
        self.visible = False
        # 子弹对象
        self.bullet = Bullet(scene, True)
        # 初始化爆炸对象
        self.bomb = Bomb(scene)


    def calc_position(self):
        # 计算飞机位置
        if self.visible:
            self.bbox.move_ip(0, self.speed)
            if self.bbox[1] > SCREEN_H:
                self.set_unused()

        # 计算子弹位置
        if self.bullet.visible:
            self.bullet.move(0, self.speed + 5)

        # 爆炸图片切换
        self.bomb.switch_frame()

    def draw_element(self):
        # 绘制飞机
        if self.visible:
            self.scene.blit(self.image, self.bbox)

        # 绘制子弹
        if self.bullet.visible:
            self.bullet.draw_element()

        # 绘制爆炸图片
        self.bomb.draw_element()

    def set_unused(self):
        self.visible = False
        self.bbox[0] = -1000
        self.bbox[1] = -1000

    def set_used(self, start_x, start_y):
        self.visible = True
        self.bbox[0] = start_x
        self.bbox[1] = start_y
        self.speed = random.randint(4, 8)

    def shoot(self):
        if self.bullet.visible:
            return
        start_x = self.bbox[0] + self.bbox[2]/2 - self.bullet.bbox[2]/2
        start_y = self.bbox[1] + self.bbox[3] - 10
        self.bullet.set_used(start_x, start_y)


if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 初始化敌机对象
    enemy = EnemyPlane(window)
    enemy.set_used(random.randint(0, SCREEN_W - enemy.bbox[2]), -enemy.bbox[3])
    index = 0

    while True:

        # 清空窗口
        window.fill((0, 0, 0))
        # 计算位置
        enemy.calc_position()
        # 绘制图像
        enemy.draw_element()

        # 发射子弹
        index += 1
        if index > 120 and random.randint(1, 100) > 80 and enemy.bbox[1] < 300:
            enemy.shoot()
            index = 0

        # 敌机复活
        if not enemy.visible:
            enemy.set_used(random.randint(0, SCREEN_W - enemy.bbox[2]), -enemy.bbox[3])

        pygame.event.get()
        pygame.display.update()
        clock.tick(60)










