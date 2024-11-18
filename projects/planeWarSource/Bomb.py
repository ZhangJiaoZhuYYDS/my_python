import pygame.image
from Config import *

class Bomb:

    def __init__(self, scene):
        # 持有场景对象
        self.scene = scene
        # 加载爆炸素材
        self.images = [pygame.image.load(f'source/bomb/bomb-{index}.png') for index in range(1, 7)]
        # 爆炸位置
        self.position = [0, 0]
        # 是否可见
        self.visible = False
        # 当前绘制的图像
        self.draw_index = 0
        # 播放间隔
        self.interval = 5  # 5 帧
        self.interval_index = 0
        # 加载音效
        self.sound = pygame.mixer.Sound('source/music/bomb.wav')
        self.sound.set_volume(VOLUME)

    def set_used(self, start_x, start_y):
        self.visible = True
        self.draw_index = 0
        self.position[0] = start_x
        self.position[1] = start_y
        # 开始播放音效
        self.sound.play()

    def set_unused(self):
        self.visible = False
        self.draw_index = 0
        self.position[0] = -1000
        self.position[1] = -1000


    def switch_frame(self):
        # 当前必须是可见状态
        if not self.visible:
            return

        # 控制两张图片绘制的间隔
        self.interval_index += 1
        if self.interval_index < self.interval:
            return
        self.interval_index = 0

        # 切换到下一张图片
        self.draw_index += 1
        if self.draw_index >= len(self.images):
            # 停止爆炸
            self.set_unused()


    def draw_element(self):
        if not self.visible:
            return
        self.scene.blit(self.images[self.draw_index], self.position)


if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 初始化爆炸对象
    bomb = Bomb(window)
    bomb.set_used(300, 400)


    while True:
        window.fill((0, 0, 0))

        # 切换爆炸图片
        bomb.switch_frame()
        # 绘制爆炸图片
        bomb.draw_element()

        if not bomb.visible:
            bomb.set_used(300, 400)

        pygame.event.get()
        pygame.display.update()
        clock.tick(60)


