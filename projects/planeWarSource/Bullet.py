from Config import *
import pygame

class Bullet:

    def __init__(self, scene, is_enemy=False):

        # 持有窗口对象
        self.scene = scene
        # 子弹的状态
        self.visible = False
        # 加载子弹资源
        bullet_index = ENEMY_BULLET_INDEX if is_enemy else HERO_BULLET_INDEX
        bullet_filename = f'source/bullet/bullet_{bullet_index}.png'
        self.image = pygame.image.load(bullet_filename)
        if is_enemy:
            # 第二个参数表示是否对 X 轴做翻转
            # 第三个参数表示是否对 Y 轴做翻转
            self.image = pygame.transform.flip(self.image, False, True)
        # 子弹位置尺寸
        self.bbox = self.image.get_rect()


    def draw_element(self):
        """负责子弹图像绘制"""
        if not self.visible:
            return
        self.scene.blit(self.image, self.bbox)

    def move(self, dx, dy):
        """
        根据 dx dy 确定的方向和速度移动子弹
        :param dx: 相对于子弹上一次的位置，所移动的偏移量
        :param dy: 相对于子弹上一次的位置，所移动的偏移量
        :return:
        """

        if not self.visible:
            return
        self.bbox.move_ip(dx, dy)
        if self.bbox[1] < 0 or self.bbox[1] > SCREEN_H:
            self.set_unused()

    def set_used(self, start_x, start_y):
        """子弹发射：将子弹设置可见，初始子弹位置"""
        self.visible = True
        self.bbox[0] = start_x
        self.bbox[1] = start_y

    def set_unused(self):
        """设置子弹不可用"""
        self.visible = False
        self.bbox[0] = -1000
        self.bbox[1] = -1000


if __name__ == '__main__':
    # 1. 创建一个窗口
    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 2. 窗口内部子弹坐标计算 子弹绘制，从而实现子弹的运动效果

    bullet1 = Bullet(scene=window)
    bullet1.set_used(100, 600)

    bullet2 = Bullet(scene=window)
    bullet2.set_used(400, 600)

    while True:

        window.fill((0, 0, 0))

        # 子弹坐标计算
        bullet1.move(0, -5)
        bullet2.move(0, -10)

        # 子弹图像绘制
        bullet1.draw_element()
        bullet2.draw_element()

        if not bullet1.visible:
            bullet1.set_used(100, 600)

        if not bullet2.visible:
            bullet2.set_used(400, 600)

        # 读取所有的事件并丢弃
        pygame.event.get()

        pygame.display.update()
        clock.tick(60)




