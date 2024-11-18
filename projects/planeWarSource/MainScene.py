import pygame
from Config import *
from GameMap import GameMap
from HeroPlane import HeroPlane
from EnemyManager import EnemyManager
import sys

class MainScene:

    def __init__(self):
        # 初始化 PyGame
        pygame.init()
        # 初始化窗口
        self.scene = pygame.display.set_mode([SCREEN_W, SCREEN_H])
        # 设置窗口标题
        pygame.display.set_caption('飞机大战 v1.0')
        # 初始化时钟
        self.clock = pygame.time.Clock()
        # 初始化元素
        self.init_elements()
        # 统计战斗数据
        self.defeat_count = 0  # 击中飞机数量
        self.damage_count = 0  # 被击中的次数
        self.impact_count = 0  # 被撞击的次数
        # 背景音乐加载
        pygame.mixer.music.load('source/music/bg.wav')
        pygame.mixer.music.set_volume(VOLUME)
        pygame.mixer.music.play(-1)
        # 按键状态字典
        self.keys_pressed = {}

    # 绘制战斗数据
    def draw_battle_data(self):
        # 加载一个字体
        font = pygame.font.Font('source/fonts/SimHei.ttf', 16)
        text = f'击毁数: {self.defeat_count} 被击中: {self.damage_count} 被撞击: {self.impact_count}'
        # 第一个参数: 渲染的文字
        # 第二个参数: 抗锯齿
        # 第三个参数: 颜色
        text = font.render(text, True, (255, 255, 255))
        # 将文字绘制到窗口上
        self.scene.blit(text, (150, 20))

    # 初始化场景元素
    def init_elements(self):
        # 初始化地图
        self.map = GameMap(self.scene)
        # 初始化英雄飞机
        self.hero = HeroPlane(self.scene)
        # 初始化敌机
        self.enemy = EnemyManager(self.scene)

    # 碰撞检测
    def detect_colision(self):
        # 英雄飞机子弹和敌机是否碰撞
        for bullet in self.hero.bullets.bullet_list:
            if not bullet.visible:
                continue
            for enemy in self.enemy.enemies:
                if not enemy.visible:
                    continue
                if pygame.Rect.colliderect(bullet.bbox, enemy.bbox):
                    bullet.set_unused()
                    # 播放爆炸效果
                    enemy.bomb.set_used(enemy.bbox[0], enemy.bbox[1])
                    enemy.set_unused()
                    self.defeat_count += 1

        # 英雄飞机子弹和敌机子弹是否碰撞
        for bullet in self.hero.bullets.bullet_list:
            if not bullet.visible:
                continue

            for enemy in self.enemy.enemies:
                if not enemy.bullet.visible:
                    continue
                if pygame.Rect.colliderect(bullet.bbox, enemy.bullet.bbox):
                    bullet.set_unused()
                    enemy.bullet.set_unused()

        # 英雄飞机和敌机是否发生相撞
        for enemy in self.enemy.enemies:
            if not enemy.visible:
                continue
            if pygame.Rect.colliderect(self.hero.bbox, enemy.bbox):
                # 播放爆炸效果
                enemy.bomb.set_used(enemy.bbox[0], enemy.bbox[1])
                enemy.set_unused()
                self.impact_count += 1

        # 英雄飞机和敌机的子弹是否发生碰撞
        for enemy in self.enemy.enemies:
            if not enemy.bullet.visible:
                continue
            if pygame.Rect.colliderect(self.hero.bbox, enemy.bullet.bbox):
                enemy.bullet.set_unused()
                self.damage_count += 1

    # 坐标计算
    def calc_position(self):
        # 地图位置计算
        self.map.calc_position()
        # 飞机子弹坐标计算
        self.hero.calc_position()
        # 敌机坐标计算
        self.enemy.calc_position()

    # 绘制图像
    def draw_elements(self):
        # 地图图像绘制
        self.map.draw_element()
        # 绘制飞机和子弹
        self.hero.draw_element()
        # 绘制敌机
        self.enemy.draw_element()
        # 绘制战斗数据
        self.draw_battle_data()

    # 事件处理
    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            # 窗口关闭事件
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            # 处理敌机出发事件
            if event.type == EnemyManager.ENEMY_START_EVNET:
                self.enemy.set_out()
            # 处理敌机发射子弹事件
            if event.type == EnemyManager.ENEMY_SHOOT_EVNET:
                self.enemy.shoot()
            # 键盘按下事件
            if event.type == pygame.KEYDOWN:
                self.keys_pressed[event.key] = True
            # 键盘释放事件
            if event.type == pygame.KEYUP:
                self.keys_pressed[event.key] = False

    # 更新飞机位置
    def update_hero_position(self):
        if self.keys_pressed.get(pygame.K_UP):
            self.hero.top()
        if self.keys_pressed.get(pygame.K_DOWN):
            self.hero.bottom()
        if self.keys_pressed.get(pygame.K_LEFT):
            self.hero.left()
        if self.keys_pressed.get(pygame.K_RIGHT):
            self.hero.right()

    # 持续发射子弹
    def continuous_shoot(self):
        if self.keys_pressed.get(pygame.K_1):
            self.hero.shoot(1)
        if self.keys_pressed.get(pygame.K_2):
            self.hero.shoot(3)
        if self.keys_pressed.get(pygame.K_3):
            self.hero.shoot(5)

    def run(self):
        while True:
            # 碰撞检测
            self.detect_colision()
            # 坐标计算
            self.calc_position()
            # 绘制图像
            self.draw_elements()
            # 事件处理
            self.handle_events()
            # 更新飞机位置
            self.update_hero_position()
            # 持续发射子弹
            self.continuous_shoot()
            # 窗口刷新
            pygame.display.update()
            self.clock.tick(60)
