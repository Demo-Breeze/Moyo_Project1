#One edge case multiple dots, another is arrow notation is allwowed math error can easily fix this,i should also maybe confine the amount of digits u can input, any thing can be typed but it returns an error if nto allowed

import re
import math
import ast
import operator
import customtkinter as ctk
import pygame
from music import BackgroundMusicPlayer

pygame.mixer.init()

playlist = [
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/Supernova.mp3",  # BY Xtrullor
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
]

#Using eval make it so that if i typed in something other than numbers like a command to get in my system, it would work therefore i have to use normal func rather than using eval. 1st Edge case.
music = BackgroundMusicPlayer(playlist, volume=0.4)    

FUNCTIONS = {
    "sin": lambda x: math.sin(math.radians(x)), #Lambda is an anonymous func, prevents from running immediately. Dict is used so as to beal to call the key later e.g sin or log. Math module is used here we convert the degrees to turn them into radians cuz that is what the math module uses rather than degrees. Same for the rest
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "asin": lambda x: math.degrees(math.asin(x)),
    "acos": lambda x: math.degrees(math.acos(x)),
    "atan": lambda x: math.degrees(math.atan(x)),
    "sqrt": math.sqrt,
    "log": math.log10,
    "exp": math.exp,
    "factorial": lambda x: math.factorial(int(x)),
    "cbrt": math.cbrt,
}
CONSTANTS = {"pi": math.pi, "e": math.e}
OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, #This is used to declare my operation signs as strings so i can use in the text box of my output. Uses the Abstract Syntax Module(weird name ig.)
    ast.Div: operator.truediv, ast.Mod: operator.mod, ast.Pow: operator.pow,
    ast.UAdd: operator.pos, ast.USub: operator.neg,
}


def safe_eval(expr):
    expr = re.sub(r"(\d+(?:\.\d+)?)\s*!", r"factorial(\1)", expr)  # Switches ! to a factorial as python does not ineherently understand ! as a factorial(Searched this up cuz why not.)
    expr += ")" * max(0, expr.count("(") - expr.count(")"))        # If someone opens a brac ket this autocloses it by counting the amount of ( they are verses the amount of ) they are.
    return eval_node(ast.parse(expr, mode="eval").body)    #converts the text into a safe structural syntax tree (AST), and evaluates it.


def eval_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](eval_node(node.left), eval_node(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
        return OPS[type(node.op)](eval_node(node.operand))
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in FUNCTIONS:
        return FUNCTIONS[node.func.id](*[eval_node(a) for a in node.args])
    if isinstance(node, ast.Name) and node.id in CONSTANTS:
        return CONSTANTS[node.id]
    raise ValueError("not a valid expression")


window = ctk.CTk()# Define screen size
window.title("Calculator")
window.configure(fg_color="#5FC0E0")
window.geometry("340x480")
window.resizable(False, False)

entry_var = ctk.StringVar(value="0")
shift_active = False
mode_var = ctk.IntVar(value=0)  # 0 = Standard, 1 = Scientific

#To be able to see what you type on screen
def append(text):
    current = entry_var.get()
    if current in ("0", "Error"):
        current = ""
    entry_var.set(current + text)


def clear():
    entry_var.set("0")


def backspace():
    entry_var.set(entry_var.get()[:-1] or "0")


def negate():
    current = entry_var.get()
    if current.startswith("-"):
        entry_var.set(current[1:])
    elif current not in ("0", ""):
        entry_var.set("-" + current)


def evaluate():
    expr = entry_var.get().replace("×", "*").replace("÷", "/") #python doesnt know what x or ÷ so it replaces them with what python does know
    try:
        result = safe_eval(expr)
    except Exception:
        entry_var.set("Error")
        return
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    entry_var.set(str(result))

#when shift is active make it so that the buttons have reverse functions
def toggle_shift():
    global shift_active
    shift_active = not shift_active
    shift_btn.configure(fg_color="#1e538d" if shift_active else "#e4dfdf")
    sin_btn.configure(text="asin" if shift_active else "sin")
    cos_btn.configure(text="acos" if shift_active else "cos")
    tan_btn.configure(text="atan" if shift_active else "tan")
    sqrt_btn.configure(text="³√ " if shift_active else "√")


def press_sin():# sin and sin-1 function to text box
    append("asin(" if shift_active else "sin(")


def press_cos(): # cos and cos-1 function to text box
    append("acos(" if shift_active else "cos(")


def press_tan(): # taN and tan-1 function to text box
    append("atan(" if shift_active else "tan(")
def press_sqrt():
    append("cbrt(" if shift_active else "sqrt(")


def apply_mode(): #Switching the window size for different modes so as not to overflow.
    if mode_var.get() == 1:
        scientific_frame.pack(fill="both", expand=True, padx=10, before=standard_frame)
        window.geometry("340x620")
    else:
        scientific_frame.pack_forget()
        window.geometry("340x480")

# USed PYUIBUILDER FOR THIS PART
top_bar = ctk.CTkFrame(window, fg_color="#0cf1f1")
top_bar.pack(fill="x", padx=10, pady=(10, 0))

ctk.CTkRadioButton(top_bar, text="Standard", variable=mode_var, value=0,
                    command=apply_mode).pack(side="left", expand=True, padx=5, pady=8)
ctk.CTkRadioButton(top_bar, text="Scientific", variable=mode_var, value=1,
                    command=apply_mode).pack(side="left", expand=True, padx=5, pady=8)
display = ctk.CTkEntry(window, textvariable=entry_var, font=ctk.CTkFont(size=26),
                        justify="right", height=56)
display.pack(fill="x", padx=10, pady=10)


def btn(parent, text, command, row, col, colspan=1, light=False):
    b = ctk.CTkButton(parent, text=text, command=command, corner_radius=5,
                       fg_color="#ececec" if light else "#e4dfdf",
                       hover_color="#1e538d", text_color="#000000")
    b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=4, pady=4)
    return b


#this is for standard as in simple calc it draws the screen again so if scientific it resets. it also drawws in all the numbers so i dont hv to waste lines by inputing them one by one
standard_frame = ctk.CTkFrame(window, fg_color="#5FC0E0")
standard_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
for i in range(4):
    standard_frame.grid_columnconfigure(i, weight=1)
for i in range(6):
    standard_frame.grid_rowconfigure(i, weight=1)

btn(standard_frame, "(", lambda: append("("), 0, 0)
btn(standard_frame, ")", lambda: append(")"), 0, 1)
btn(standard_frame, "CE", clear, 0, 2)
btn(standard_frame, "C", clear, 0, 3)

btn(standard_frame, "7", lambda: append("7"), 1, 0, light=True)
btn(standard_frame, "8", lambda: append("8"), 1, 1, light=True)
btn(standard_frame, "9", lambda: append("9"), 1, 2, light=True)
btn(standard_frame, "÷", lambda: append("÷"), 1, 3)

btn(standard_frame, "4", lambda: append("4"), 2, 0, light=True)
btn(standard_frame, "5", lambda: append("5"), 2, 1, light=True)
btn(standard_frame, "6", lambda: append("6"), 2, 2, light=True)
btn(standard_frame, "×", lambda: append("×"), 2, 3)

btn(standard_frame, "1", lambda: append("1"), 3, 0, light=True)
btn(standard_frame, "2", lambda: append("2"), 3, 1, light=True)
btn(standard_frame, "3", lambda: append("3"), 3, 2, light=True)
btn(standard_frame, "-", lambda: append("-"), 3, 3)

btn(standard_frame, "±", negate, 4, 0)
btn(standard_frame, "0", lambda: append("0"), 4, 1, light=True)
btn(standard_frame, ".", lambda: append("."), 4, 2, light=True)
btn(standard_frame, "+", lambda: append("+"), 4, 3)

btn(standard_frame, "⌫", backspace, 5, 0)
btn(standard_frame, "Mod", lambda: append("%"), 5, 1)
btn(standard_frame, "=", evaluate, 5, 2, colspan=2)

# for a 4 by 3 u1 style. and scrientific buttons
scientific_frame = ctk.CTkFrame(window, fg_color="#5FC0E0")
for i in range(4):
    scientific_frame.grid_columnconfigure(i, weight=1)
for i in range(3):
    scientific_frame.grid_rowconfigure(i, weight=1)

shift_btn = btn(scientific_frame, "2nd", toggle_shift, 0, 0)
sin_btn = btn(scientific_frame, "sin", press_sin, 0, 1)
cos_btn = btn(scientific_frame, "cos", press_cos, 0, 2)
tan_btn = btn(scientific_frame, "tan", press_tan, 0, 3)


btn(scientific_frame, "x²", lambda: append("**2"), 1, 0)
btn(scientific_frame, "xʸ", lambda: append("**"), 1, 1)
btn(scientific_frame, "10ˣ", lambda: append("10**("), 1, 2)
sqrt_btn = btn(scientific_frame, "√", press_sqrt, 1, 3)

btn(scientific_frame, "log", lambda: append("log("), 2, 0)
btn(scientific_frame, "n!", lambda: append("!"), 2, 1)
btn(scientific_frame, "EXP", lambda: append("exp("), 2, 2)
btn(scientific_frame, "π", lambda: append("pi"), 2, 3)

window.bind("<Return>", lambda e: evaluate())
window.bind("<KP_Enter>", lambda e: evaluate())
window.bind("<Escape>", lambda e: clear())

apply_mode()# draws screen
window.mainloop() # updates screen
