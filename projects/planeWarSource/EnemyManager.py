import random
import pygame.time
from Config import *
from EnemyPlane import EnemyPlane


class EnemyManager:

    # 敌机出发事件
    ENEMY_START_EVNET = pygame.USEREVENT + 1
    ENEMY_SHOOT_EVNET = pygame.USEREVENT + 2

    def __init__(self, scene):
        # 初始化多个敌机对象
        self.enemies = [EnemyPlane(scene) for _ in range(8)]

        # 定时器(2秒调用一次 set_out, 1秒钟调用一次 shoot)
        # 第一个参数事件类型，第二个参数事件发生的事件
        pygame.time.set_timer(EnemyManager.ENEMY_START_EVNET, 2000)
        pygame.time.set_timer(EnemyManager.ENEMY_SHOOT_EVNET, 1000)

    def calc_position(self):
        for enemy in self.enemies:
            enemy.calc_position()

    def draw_element(self):
        for enemy in self.enemies:
            enemy.draw_element()

    def set_out(self):
        """敌机出发逻辑"""

        # 1. 确定飞机的数量
        number = random.randint(1, 4)

        # 2. 挑选候选飞机(目前 visible 处于 False 状态)
        wait_for_out = []
        for enemy in self.enemies:
            if not enemy.visible:
                wait_for_out.append(enemy)
            if len(wait_for_out) == number:
                break

        # 3. 敌机出发(敌机位置)
        if len(wait_for_out) == number:
            # 敌机位置计算
            position_xs = []
            range_distance = int((SCREEN_W - 100) / number)
            for index in range(number):
                x = random.randint(index * range_distance, index * range_distance + range_distance - 100)
                position_xs.append(x)
            # 敌机飞行
            for enemy, x in zip(wait_for_out, position_xs):
                enemy.set_used(x, -enemy.bbox[3])


    def shoot(self):
        """多个敌机子弹发射"""

        for enemy in self.enemies:
            if not enemy.visible:
                continue

            if random.randint(1, 100) > 50 and enemy.bbox[1] < 500:
                enemy.shoot()


if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 初始化敌机管理对象
    enemies = EnemyManager(window)

    while True:

        # 清空窗口
        window.fill((0, 0, 0))
        # 敌机位置
        enemies.calc_position()
        # 敌机绘制
        enemies.draw_element()

        # 处理定时器事件
        events = pygame.event.get()
        for event in events:
            if event.type == EnemyManager.ENEMY_START_EVNET:
                enemies.set_out()
            if event.type == EnemyManager.ENEMY_SHOOT_EVNET:
                enemies.shoot()

        pygame.display.update()
        clock.tick(60)


