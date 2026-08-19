import time
import sys
import pygame
from pathlib import Path
from Math import Math
from music import BackgroundMusicPlayer
pygame.mixer.init()
playlist = [
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Supernova.mp3", # BY Xtrullor
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Dimension.mp3", # BY Creo
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Ricochet_Love.mp3", # BY Waterflame
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Nuke_Powder.mp3", # BY Maeloux
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Epilogue.mp3", # BY Creo
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/At_the_Speed_of_Light.mp3", # BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Sphere.mp3", # BY Creo
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Isolation.mp3", # BY DJVI
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Sonic_Blaster.mp3", # BY F-777
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Screamroom.mp3", # BY Xtrullor
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Monody.mp3", # BY TheFatRat
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Time_Leaper.mp3", # BY Hinkik
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Isolation2.mp3", # BY Nighthawk22
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Sine_Wavs.mp3", # BY NK/RUkkus
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Shiawase.mp3", # BY Dion Timmer
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Explorers.mp3", # BY Hinkik
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Thermodynamix.mp3", # BY Dj-Nate
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Dark_Dragon_Fire.mp3", # BY F-777
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Society_Remix.mp3",  #By HelliXScream Original by Pathetic.
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/10000.mp3",#BY Colbreakz
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Surface.mp3",#BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Operation_Evolution.mp3", #BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Infernoplex.mp3",#BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/The_Falling_Mysts.mp3", #BY Dimrain47
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Realms.mp3",#BY Hinkik
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Skystrike.mp3", #BY Hinkik
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Outbreaker.mp3", #BY Hinkik
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Duality.mp3", #BY Dimrain47

]
music = BackgroundMusicPlayer(playlist, volume=0.4)                        
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping music player...")
    sys.exit()
numbers = [0,1,2,3,4,5,6,7,8,9]
arithmetic = ["+","=","/","**","//","*","-","=","%"]