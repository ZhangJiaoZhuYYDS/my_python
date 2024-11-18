import pygame

# 1. 音乐播放
def test01():

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 1. 音乐加载
    pygame.mixer.music.load('bg.wav')
    # 2. 设置音量
    pygame.mixer.music.set_volume(0.1)
    # 3. 播放音乐
    pygame.mixer.music.play(-1)

    while True:
        clock.tick(60)


# 2. 音效播放
def test02():

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 1. 音效加载
    bomb = pygame.mixer.Sound('bomb.wav')
    # 2. 设置音量
    bomb.set_volume(0.1)

    while True:

        # 3. 播放音效
        # pygame.mixer.Sound.play(bomb)
        bomb.play()

        clock.tick(1)


if __name__ == '__main__':
    test02()