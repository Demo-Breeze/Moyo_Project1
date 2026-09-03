import pygame
import time
import sys
from music import BackgroundMusicPlayer
from Cube import CubeManager
pygame.init()
pygame.font.init()
playlist = [
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Supernova.mp3",#"BY Xtrullor",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Dimension.mp3",  # BY Creo
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Ricochet_Love.mp3",  # BY Waterflame
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Nuke_Powder.mp3",  # BY Maeloux
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Epilogue.mp3",  # BY Creo
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/At_the_Speed_of_Light.mp3",  # BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Sphere.mp3",  # BY Creo
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Isolation.mp3",  # BY DJVI
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Sonic_Blaster.mp3",  # BY F-777
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Screamroom.mp3",  # BY Xtrullor
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Monody.mp3",  # BY TheFatRat
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Time_Leaper.mp3",  # BY Hinkik
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Isolation2.mp3",  # BY Nighthawk22
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Sine_Wavs.mp3",  # BY NK/RUkkus
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Shiawase.mp3",  # BY Dion Timmer
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Explorers.mp3",  # BY Hinkik
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Thermodynamix.mp3",  # BY Dj-Nate
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Dark_Dragon_Fire.mp3",  # BY F-777
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Society_Remix.mp3",  # By HelliXScream, original by Pathetic.
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/10000.mp3",  # BY Colbreakz
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Surface.mp3",  # BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Operation_Evolution.mp3",  # BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Infernoplex.mp3",  # BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/The_Falling_Mysts.mp3",  # BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Realms.mp3",  # BY Hinkik
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Skystrike.mp3",  # BY Hinkik
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Outbreaker.mp3",  # BY Hinkik
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Duality.mp3",  # BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Menace.mp3",  # BY TheRealMannyHeffley
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/The_Beginning_Of_Time.mp3",#BY Dj-Nate
]
music = BackgroundMusicPlayer(playlist, volume=0.2) 

# I have to have a start screen,
# A lose screen
# A win Screen
# A percentage bar with percent
# A gd cube sprtie I have four sprites now so should be fine.
# A background DONE
# Music DONE Also made it sure updates what music u r playing
# A play button
# A music button
# Drawn the spike sprites but now i need to make them random and maybe even spawn together:p
# A pasue button
# and for the cube i need velocity, jump height, gravity and maybe speed. rotations as wel

#initalize screen
Screen_width = 1800
Screen_height = 1200
Sprite_height,Sprite_width = 160,220
screen = pygame.display.set_mode((Screen_width, Screen_height))
#Initialize clock that controls ticks per second
clock  = pygame.time.Clock()
#Initialize Background and ground
background =pygame.image.load("gd/Sprites/Background.jpg").convert()
background = pygame.transform.scale(background, (Screen_width, Screen_height))
ground =pygame.image.load("gd/Sprites/ground.jpeg").convert()
ground = pygame.transform.scale(ground, (Screen_width, Screen_height/5))
#Initialize Sprites e.g my cube and my spikes
Cube = pygame.image.load("gd/Sprites/Cube.png")
Cube = pygame.transform.scale(Cube, (Sprite_width, Sprite_height))
"""Angry = pygame.image.load("gd/Sprites/Angry.png")
Angry = pygame.transform.scale(Angry, (Sprite_width, Sprite_height))
Normal = pygame.image.load("gd/Sprites/Normal.png")
Normal = pygame.transform.scale(Normal, (Sprite_width, Sprite_height))
Monkey = pygame.image.load("gd/Sprites/Cube.png")
Monkey= pygame.transform.scale(Monkey, (Sprite_width, Sprite_height))

Clubstep = pygame.image.load("gd/Sprites/Cubstep.png")
Clubstep = pygame.transform.scale(Clubstep, (Sprite_width, Sprite_height))"""
Spike = pygame.image.load("gd/Sprites/Spike.png")
Spike= pygame.transform.scale(Spike, (Sprite_width, Sprite_height))
cube_manager = CubeManager(Cube)

#Makes the background move so as to give illusion ur moving
bg_move,g_move = Screen_width,Screen_width
ui_font = pygame.font.Font("gd/pusab/PUSAB___.otf", 32)
#Title
pygame.display.set_caption("Geometry Dash")
#Initializes game loop
running  = True
while running:
    # Get delta time in seconds (approx 0.0166s at 60 FPS)
    dt = clock.tick(60) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        # Trigger the 0.525s rotation whenever Spacebar is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                cube_manager.start_rotation()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_p:
                pass

    #makes bg move and if it goes off screen it will make it come back
    song_text = f"Now Playing: {music.currentsong}"
    ground_y = Screen_height - ground.get_height()
    spike_y = ground_y - Spike.get_height()
    text_surface = ui_font.render(song_text, True, (255, 255, 255))
    
    bg_move-=0.3
    g_move -=5
    if bg_move <= 0:
        bg_move = Screen_width
    if g_move <= 0:
        g_move = Screen_width

    # Update the animation progress
    cube_manager.update(dt)

    screen.blit(background,(int(bg_move),0))
    screen.blit(background,(int(bg_move)-Screen_width,0))
    screen.blit(text_surface, (0, 0))
    screen.blit(ground, (int(g_move), ground_y))
    screen.blit(ground, (int(g_move) - Screen_width, ground_y))
    screen.blit(Spike, (int(g_move), spike_y))
    screen.blit(Spike, (int(g_move) - Screen_width, spike_y))

    # Fetch the cleanly centered, rotated image and its rect
    draw_cube, draw_rect = cube_manager.get_rotated_surface_and_rect(100, ground_y - 160)
    screen.blit(draw_cube, draw_rect)

# Updates the screen
    pygame.display.update()
