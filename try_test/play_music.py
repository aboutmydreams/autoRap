import pygame
from PIL import Image



def play_voice(voice_file_path):
    '''用 pygame 库播放语音文件

    '''
    pygame.init()
    pygame.mixer.init()
    
    track = pygame.mixer.music.load(voice_file_path)
    pygame.mixer.music.play(loops=0,start=0)
    screen = pygame.display.set_mode([300,300])


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

# play_voice("try_test/me.wav")