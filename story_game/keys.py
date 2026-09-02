import pygame
from story_game.music import BackgroundMusicPlayer
pygame.init()
class Keys:
    def __init__(self):
        self.pygame.init() = pygame.init()
    def __key_down__(self, key):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE and pygame.key.get_mods() & pygame.KMOD_Alt: 
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                if event.key == pygame.K_UP and pygame.key.get_mods() & pygame.KMOD_Alt:
                    current_volume = pygame.mixer.music.get_volume()
                    new_volume = min(1.0, current_volume + 0.1)
                    pygame.mixer.music.set_volume(new_volume)
                if event.key == pygame.K_DOWN and pygame.key.get_mods() & pygame.KMOD_Alt:
                    current_volume = pygame.mixer.music.get_volume()
                    new_volume = max(0.0, current_volume - 0.1)
                    pygame.mixer.music.set_volume(new_volume)
    def __key_up__(self, key):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()