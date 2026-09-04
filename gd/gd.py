import pygame
import time
import sys
from music import BackgroundMusicPlayer
from Cube import CubeManager
pygame.init()
pygame.font.init()
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

playlist = [
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Supernova.mp3",
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Dimension.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Ricochet_Love.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Nuke_Powder.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Epilogue.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/At_the_Speed_of_Light.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Sphere.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Isolation.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Sonic_Blaster.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Screamroom.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Monody.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Time_Leaper.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Isolation2.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Sine_Wavs.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Shiawase.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Explorers.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Thermodynamix.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Dark_Dragon_Fire.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Society_Remix.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/10000.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Surface.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Operation_Evolution.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Infernoplex.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/The_Falling_Mysts.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Realms.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Skystrike.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Outbreaker.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Duality.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Menace.mp3",  
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/The_Beginning_Of_Time.mp3",
]
music = BackgroundMusicPlayer(playlist, volume=0.2) 

# Initialize screen
Screen_width = 1800
Screen_height = 1200
Sprite_height, Sprite_width = 160, 220
screen = pygame.display.set_mode((Screen_width, Screen_height))
clock = pygame.time.Clock()

# Initialize Background and ground
background = pygame.image.load("gd/Sprites/Background.jpg").convert()
background = pygame.transform.scale(background, (Screen_width, Screen_height))
ground = pygame.image.load("gd/Sprites/ground.jpeg").convert()
ground = pygame.transform.scale(ground, (Screen_width, int(Screen_height / 5)))

# Initialize Sprites
Cube = pygame.image.load("gd/Sprites/Cube.png")
Cube = pygame.transform.scale(Cube, (Sprite_width, Sprite_height))
Spike = pygame.image.load("gd/Sprites/Spike.png")
Spike = pygame.transform.scale(Spike, (Sprite_width, Sprite_height))

cube_manager = CubeManager(Cube)

# Physics Variables
cube_x = 100
ground_y = Screen_height - ground.get_height()
cube_y = ground_y - Sprite_height  # Starting position on the floor
vel_y = 0
spike_y = ground_y - Spike.get_height()
is_grounded = True

# Physics Constants (Adjust these to fit your high 1200px resolution)
GRAVITY = 2.0        
JUMP_POWER = -38       

# Makes background move to make it seem like the cube is moving thru the level
bg_move = 0
g_move = 0
#Defines font cuz why not
ui_font = pygame.font.Font("gd/pusab/PUSAB___.otf", 32)
pygame.display.set_caption("Geometry Dash")

# Level / game state stuff for the percent bar, win screen, pause screen and losing
LEVEL_LENGTH = 9000      # how far (same units g_move scrolls) you need to go to win, tweak to taste
distance_traveled = 0.0  # how far we've scrolled so far, drives the percent bar + win check
game_state = "playing"   # "playing", "paused", "win", "lose"

# g_move resets to 0 on spawn/respawn, which momentarily puts the looping spike copy
# right on top of the cube's start position. This grace timer skips collision for a
# few frames right after (re)spawning so that copy has time to scroll clear first.
SPAWN_GRACE_FRAMES = 30
spawn_grace = SPAWN_GRACE_FRAMES

big_font = pygame.font.Font("gd/pusab/PUSAB___.otf", 72)    # for the WIN / LOSE / PAUSED message
small_font = pygame.font.Font("gd/pusab/PUSAB___.otf", 28)  # for the percent bar's number

running = True
while running:
    # Get delta time in seconds
    dt = clock.tick(60) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                # Only jump if currently standing on the floor and actually playing
                if is_grounded and game_state == "playing":
                    vel_y = JUMP_POWER
                    is_grounded = False
                    cube_manager.start_rotation()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_p:
                # Toggle pause (only makes sense while playing or already paused)
                if game_state == "playing":
                    game_state = "paused"
                elif game_state == "paused":
                    game_state = "playing"
            if event.key == pygame.K_r:
                # Restart the run from the win/lose screens
                if game_state in ("win", "lose"):
                    cube_y = ground_y - Sprite_height
                    vel_y = 0
                    is_grounded = True
                    distance_traveled = 0.0
                    bg_move = 0
                    g_move = 0
                    spawn_grace = SPAWN_GRACE_FRAMES
                    cube_manager.reset()
                    game_state = "playing"

    # Only advance physics/scroll/collision while actually playing (pause/win/lose freeze the action)
    if game_state == "playing":
        #Gravity
        if not is_grounded:
            vel_y += GRAVITY  # Pull down
        
        cube_y += vel_y  # Move cube vertically no horizontal

        # Floor Collision detection
        if cube_y >= ground_y - Sprite_height:
            cube_y = ground_y - Sprite_height
            vel_y = 0
            is_grounded = True

        # Update movement positions continuously
        bg_move -= 0.3
        g_move -= 15
        distance_traveled += 15  # tracks total scroll distance for the percent bar / win check
        
        # Loop values seamlessly once they exit the screen boundaries
        if bg_move <= -Screen_width:
            bg_move = 0
        if g_move <= -Screen_width:
            g_move = 0

        # Update the animation progress
        cube_manager.update(dt)

        # Spike collision detection (checks both looping copies of the spike sprite)
        if spawn_grace > 0:
            spawn_grace -= 1
        else:
            cube_hitbox = pygame.Rect(cube_x, int(cube_y), Sprite_width, Sprite_height).inflate(-40, -40)
            spike_hitbox_1 = pygame.Rect(int(g_move), spike_y, Sprite_width, Sprite_height).inflate(-50, -30)
            spike_hitbox_2 = pygame.Rect(int(g_move) + Screen_width, spike_y, Sprite_width, Sprite_height).inflate(-50, -30)
            if cube_hitbox.colliderect(spike_hitbox_1) or cube_hitbox.colliderect(spike_hitbox_2):
                game_state = "lose"

        # Win check once we've scrolled the full level length
        if distance_traveled >= LEVEL_LENGTH:
            game_state = "win"

    #Shows song that is playing at current moment
    song_text = f"Now Playing: {music.currentsong}"
    text_surface = ui_font.render(song_text, True, (255, 255, 255))

    # Rendering
    screen.blit(background, (int(bg_move), 0))
    screen.blit(background, (int(bg_move) + Screen_width, 0))
    screen.blit(text_surface, (0, 0))
    
    screen.blit(ground, (int(g_move), ground_y))
    screen.blit(ground, (int(g_move) + Screen_width, ground_y))
    
    screen.blit(Spike, (int(g_move), spike_y))
    screen.blit(Spike, (int(g_move) + Screen_width, spike_y))

    # Fetch the cleanly centered, rotated image and its rect relative to our dynamic physics Y
    draw_cube, draw_rect = cube_manager.get_rotated_surface_and_rect(cube_x, int(cube_y))
    screen.blit(draw_cube, draw_rect)

    # Percentage bar, showing how far through the level we are
    percent = min(distance_traveled / LEVEL_LENGTH, 1.0) * 100
    bar_x, bar_y = 50, 50
    bar_width, bar_height = 400, 30
    pygame.draw.rect(screen, (60, 60, 60), (bar_x, bar_y, bar_width, bar_height))
    pygame.draw.rect(screen, (0, 220, 100), (bar_x, bar_y, int(bar_width * (percent / 100)), bar_height))
    pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 3)
    percent_text = small_font.render(f"{int(percent)}%", True, (255, 255, 255))
    screen.blit(percent_text, (bar_x + bar_width + 15, bar_y))

    # Pause / win / lose overlays
    if game_state != "playing":
        overlay = pygame.Surface((Screen_width, Screen_height))
        overlay.set_alpha(160)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        if game_state == "paused":
            message, color = "PAUSED - Press P to Resume", (255, 255, 255)
        elif game_state == "win":
            message, color = "LEVEL COMPLETE! - Press R to Restart", (0, 220, 100)
        elif game_state == "lose":
            message, color = "YOU DIED - Press R to Restart", (220, 50, 50)

        message_surface = big_font.render(message, True, color)
        message_rect = message_surface.get_rect(center=(Screen_width // 2, Screen_height // 2))
        screen.blit(message_surface, message_rect)

    pygame.display.update()