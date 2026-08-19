import pygame
import tkinter as tk
from sys import exit
pygame.init()

root = tk.Tk()
pygame.display.set_caption("The Adventure.")
width = int(root.winfo_screenwidth()-50)
height = int(root.winfo_screenheight()-50)
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
#lunarian_room_bg = pygame.image.load("Graphics/Room2.jfif").convert()
plains_bg_mink = pygame.image.load('Graphics/path.jfif').convert()
plains = pygame.transform.scale(plains_bg_mink,(width,height))
#city_bg_human = pygame.image.load("")
#scrap_yard_giant = pygame.image.load("Graphics/scrapyard.jpg")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #screen.blit(plains,(0,0))
    pygame.display.update()
    clock.tick(60)