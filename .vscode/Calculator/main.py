# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import customtkinter as ctk
from PIL import Image, ImageTk
import time
import sys
import pygame
from pathlib import Path
import math
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
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Menace.mp3",#BY TheRealMannyHeffley
]
music = BackgroundMusicPlayer(playlist, volume=0.4)      

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


main = ctk.CTk()
main.configure(fg_color="#5FC0E0")
main.title("Calculator")
main.geometry("449x650")
main.update_idletasks()

geometryX = 0
geometryY = 0
π = math.pi


frame = ctk.CTkFrame(master=main)
frame.configure(fg_color="#EDECEC", width=1, height=100)
frame.place(x=54, y=0)
frame.pack_propagate(False),frame.grid_propagate(False)

radio_button_var = ctk.IntVar()

modulo = ctk.CTkButton(master=main, text="Mod")
modulo.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
modulo.place(x=362, y=378)

divide = ctk.CTkButton(master=main, text="÷")
divide.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
divide.place(x=362, y=424)

multiply = ctk.CTkButton(master=main, text="×")
multiply.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
multiply.place(x=362, y=468)

add = ctk.CTkButton(master=main, text="+")
add.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
add.place(x=362, y=561)

equals_to = ctk.CTkButton(master=main, text="=")
equals_to.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
equals_to.place(x=362, y=606)

cosine = ctk.CTkButton(master=main, text="cos")
cosine.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
cosine.place(x=277, y=334)

sine = ctk.CTkButton(master=main, text="sin")
sine.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
sine.place(x=192, y=334)

exponent = ctk.CTkButton(master=main, text="xʸ")
exponent.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
exponent.place(x=108, y=334)

square = ctk.CTkButton(master=main, text="  x²")
square.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
square.place(x=22, y=334)

ten_to_the_power_of = ctk.CTkButton(master=main, text="10ˣ")
ten_to_the_power_of.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
ten_to_the_power_of.place(x=111, y=378)

root = ctk.CTkButton(master=main, text="√")
root.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
root.place(x=22, y=378)

tangent = ctk.CTkButton(master=main, text="   tan")
tangent.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
tangent.place(x=362, y=334)

exponent_function = ctk.CTkButton(master=main, text="EXP")
exponent_function.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
exponent_function.place(x=277, y=378)

delete = ctk.CTkButton(master=main, text="⌫")
delete.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
delete.place(x=277, y=424)

nine = ctk.CTkButton(master=main, text="9")
nine.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
nine.place(x=277, y=468)

clear = ctk.CTkButton(master=main, text="C")
clear.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
clear.place(x=192, y=422)

eight = ctk.CTkButton(master=main, text="8")
eight.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
eight.place(x=192, y=468)

six = ctk.CTkButton(master=main, text="6")
six.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
six.place(x=277, y=516)

subtract = ctk.CTkButton(master=main, text="-")
subtract.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
subtract.place(x=361, y=516)

five = ctk.CTkButton(master=main, text="5")
five.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
five.place(x=192, y=516)

two = ctk.CTkButton(master=main, text="2")
two.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
two.place(x=192, y=561)

three = ctk.CTkButton(master=main, text="3")
three.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
three.place(x=275, y=561)

zero = ctk.CTkButton(master=main, text="0")
zero.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
zero.place(x=192, y=606)

decimal_point = ctk.CTkButton(master=main, text=".")
decimal_point.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
decimal_point.place(x=276, y=606)

one = ctk.CTkButton(master=main, text="1")
one.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
one.place(x=108, y=561)

seven = ctk.CTkButton(master=main, text="7")
seven.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
seven.place(x=108, y=468)

four = ctk.CTkButton(master=main, text="4")
four.configure(fg_color="#ececec", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
four.place(x=108, y=516)

bracketclosed = ctk.CTkButton(master=main, text=")")
bracketclosed.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
bracketclosed.place(x=108, y=606)

pi = ctk.CTkButton(master=main, text="π")
pi.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
pi.place(x=22, y=468)

factorial = ctk.CTkButton(master=main, text="n!")
factorial.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
factorial.place(x=22, y=516)

bracketopen = ctk.CTkButton(master=main, text="(")
bracketopen.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
bracketopen.place(x=22, y=606)

plusminus = ctk.CTkButton(master=main, text="±")
plusminus.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
plusminus.place(x=22, y=561)

shift = ctk.CTkButton(master=main, text="2nd")
shift.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
shift.place(x=22, y=424)

ce = ctk.CTkButton(master=main, text="CE")
ce.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
ce.place(x=108, y=424)

logarithm = ctk.CTkButton(master=main, text="log")
logarithm.configure(fg_color="#e4dfdf", hover_color="#1e538d", width=80, height=40, text_color="#000000", corner_radius=5)
logarithm.place(x=192, y=378)


main.mainloop()