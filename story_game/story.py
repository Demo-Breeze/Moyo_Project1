import time
import sys
import pygame
from pathlib import Path
from Character import Character
from second_challenge import Roshambo
from music import BackgroundMusicPlayer
from first_challenge import first_challenge
from third_challenge import hacker

#importing all the necessary modules and classes for the game. This includes time for delays, sys for system exit, random for random choices and, pygame for music pla

pygame.mixer.init()
#My playlist for music for you(me not you) to enjoy while playing the game.
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
    r"/home/sparky/Desktop/Moyo_Project1/Music/Mp3/The_Beginning_Of_Time.mp3",#BY Dj-Nate
]
music = BackgroundMusicPlayer(playlist, volume=0.4)                        

character = input("Choose A character from the following list: \n 1. Giant. \n 2. Mink. \n 3. Human. \n 4. Lunarian.\n 1,2,3,4: ")
alive = True
# Declaring you are alive in case I decide to use a different type o
while alive:
        # main game loop starts here, keeps running until you die or quit
        if alive!=True:
            print("Dead")
            sys.exit()
        match character:
            case  "1":
                print("Congratulations.You have chosen Giant")
                time.sleep(0.5)
                print ("As a Giant, you gain an immense size along with insane levels of strength and durability. However, you are slow and clumsy, making it difficult to dodge attacks. Your size also makes it hard to fit into tight spaces.")
            case "2":
                print("Congratulations.You have chosen Mink")
                time.sleep(0.5)
                print("As a Mink, you are small and agile, allowing you to move quickly and avoid attacks. However, you lack the strength and durability of larger characters.")
            case   "3":
                print("Congratulations.You have chosen Human")
                time.sleep(0.5)
                print("As a Human, you have a balanced set of abilities, making you versatile in different situations. You are neither the strongest nor the fastest, but you can adapt to various challenges.")
            case "4":
                print("Congratulations.You have chosen Lunarian")
                time.sleep(0.5)
                print("As a Lunarian, you possess a flame on your back and an increased size. You have increased speed, agililty and strength.\n However, these effects only apply while the flames on your back are burning. After a period of five minutes, the flames will go out and your abilites will be placed on cooldown as well as your speed, durabilty and strength will be half of a normal human.")
            case _:
                print("Invalid choice. Please choose a valid character.")
                alive = False
        time.sleep(2)
        # Loading and choosing based on which character was chosen.
        print("Loading...")
        # route descriptions for each character path
        Route_1 = "As you toil in the scrap yard, you come across a hidden trapdoor concealed by the ruins of a collapsed building. Curiosity piqued, you decide to investigate further. As you descend into the darkness, you find yourself in a dimly lit underground chamber. The air is thick with dust and the scent of decay. You notice a faint glimmer of light coming from a corner of the room. \n 1. Approach the light. \n 2. Explore the chamber further. \n"
        Route_2 = "You arise to find yourself in a plain. The sun is shining and the birds are singing. You take a deep breath and feel a sense of peace and tranquility. You look around and see a path leading into the distance. \n 1. Follow the path. \n 2. Stay in the field. \n "
        Route_3 = "You open your eyes to find yourself at the heart of a bustling city. The streets are filled with people going about their daily lives, and the sounds of traffic and chatter fill the air. You take a moment to gather your bearings and decide where to go next. \n 1. Explore the city. \n 2. Find a place to rest. \n"
        Route_4 = "You wake up in a dark room. As you look around, you notice the obscene smell radiating in the room. Would you like to investigate the room or leave the room? \n 1. Investigate the room. \n 2. Leave the room. \n "
        time.sleep(2.5)
        match character:
            case "1":
                print(Route_1)
            case "2":
                print(Route_2)
            case "3":
                print(Route_3)
            case "4":
                print(Route_4)
            case _:
                print("Invalid choice. Please choose a valid character.")
                sys.exit()
        first_choice = input("Enter your choice 1|2: ")
        time.sleep(1.5) # Lore for character and depends on which character was chosen as well as a 50-50 on whether you die or not.
        # branching story logic based on character and first choice
        match character:
            case "1":
                match first_choice:
                    case "1":
                        print("You approach the light and find a hidden treasure chest filled with gold and jewels. However, to your right you see rusty chains attached to a rusty set of armor. You can either take the treasure or take the armor. \n 1. Take the treasure. \n 2. Take the armor. \n  ")
                    case "2":
                        alive = False
                        print("As you explore the chamber further, you trigger a trap and fall into a pit impaled with poisonous spears that don't immediately kill you but drag out death to be as painful as possible. Game over.")
                        sys.exit()
                    case _:
                        print("Invalid choice. Please choose a valid option.")
                        sys.exit()
            case "2":
                match first_choice:
                    case "1":
                        alive = False
                        print("You follow the path and come across a small village. The villagers welcome you and offer you food and shelter. You decide to stay in the village not knowing that the village is actually a front for a cult who sacrifice you to their god. Game over.")
                        sys.exit()
                    case "2":
                        print("You decide to wander around the fields. As you wander around, you are attacked by poachers who view you as another head on their trophy road. Will you fight back or run away? \n 1. Fight back. \n 2. Run away. \n ")
                    case _:
                        print("Invalid choice. Please choose a valid option.")
                        sys.exit()
            case "3":
                match first_choice:
                    case "1":
                        print("As you explore the city, you stumble upon a hidden underground market. You are approached by a mysterious figure who offers you a dangerous deal. Will you accept or decline? \n 1. Accept. \n 2. Decline. \n  ")
                    case "2":
                        alive = False
                        print("You find a nearby hotel. You check in for the night with the little money that you have. Unknown to you, the city is undergoing revolts and your building is lit on fire and you burn to death. Game over.")
                        sys.exit()
                    case _:
                        print("Invalid choice. Please choose a valid option.")
                        sys.exit()
            case "4":
                match first_choice:
                    case "1":
                        print("You investigate the room and find a hidden passage leading to a secret laboratory. Inside, you discover two artifacts, side by side, red and blue. One is a powerful artifact that can grant you the ability to awaken your race.The other will will kill you. Will you take the blue or red artifact? \n 1. Take the blue artifact. \n 2. Take the red artifact. \n ")
                    case "2":
                        alive = False
                        print("You leave the room and find yourself in a desolate wasteland. You struggle to survive and eventually succumb to the harsh conditions. Game over.")
                        sys.exit()
                    case _:
                        print("Invalid choice. Please choose a valid option.")
                        sys.exit()
            case _:
                print("Invalid choice. Please choose a valid character.")
                sys.exit()
        time.sleep(2.5)
    
        second_choice = input("Enter your choice 1|2: ")
        # second branch of story based on previous choices
        match(second_choice,character):
            case ("1","1"):
                print(" As your greedy self touches the treasure, it begins to glow with an otherworldly light. Suddenly, the ground shakes and both the treasure and armor disappears in a flash of light. Your greediness has cost you everything. Game over.")
                alive = False
                sys.exit()
            case ("2","1"):
                print("As you don the suit of armor, you feel a surge of power. You hear glass shattering and the sound of footsteps approaching. You quickly realize that you are not alone in the chamber. A group of bandits has entered, seeking to claim the treasure for themselves. You must defend yourself and the treasure. \n 1. Fight the bandits. \n 2. Attempt to negotiate with them. \n ")
            case ("1","2"):
                print("As you run with your increased speed, you easily escape the poachers and make it to a town. As you take a breath, you are brutally shot by a poacher who was stationed at the town's entrance. Game over.")
                alive = False
            case ("2","2"):
                print("After a terribly close battle, you narrowly defeat the poachers and as you loot their corspes for healing items, you find a horn. Will you blow the horn or keep it for later? \n 1. Blow the horn. \n 2. Keep it for later. \n ")
            case ("1","3"):
                print("As you accept the deal, the dealer gives u a potion to drink. As you drink it, the dealer begins to laugh at you for your stupidity as you die.\n As a last ditch attempt, you reach for the box of cargo. In it you find a healing potion and a sword. You can only choose one.\n 1. Healing potion. \n 2. Sword. \n  ")
            case ("2","3"):
                print("You politely decline the deal and walk away. As you leave, you hear the dealer's laughter echoing behind you. You turn back one last time only to see a horror entity looking at back at you. As you try to escape, it's too late and you are killed by the entity. Game over.")
                alive = False
                sys.exit()
            case ("1","4"):
                print("You take the blue artifact and instantly, you feel a dread in your gut. You start to puke and feel intense fatigue. As you are about to die, you suddenly feel a surge of energy and your body begins to change. You have awakened your Lunarian powers and are now stronger than ever.")
            case ("2","4"):
                print("You take the red artifact and immediately feel a surge of power. As you prepare to leave the laboratory, you suddenly feel a sharp pain in your chest. You look down to see a dark energy consuming your body, and you realize too late that the red artifact was cursed. Game over.")
                alive = False

            case _:
                print("Invalid choice. Please choose a valid option.")
                sys.exit()
        match(character,second_choice):
            case ("3","1"):
                time.sleep(2)
                third_choice = input( "1|2: ")
                match(third_choice):
                    case "1":
                        alive = False
                        print("You drink the healing potion and feel rejuvenated. As you prepare to escape from the underground market, you suddenly feel fatigued and realize that the potion was tainted. You collapse to the ground and succumb to the poison. Game over.")
                        sys.exit()
                    case "2":
                        print("You take the sword as a way to get a last bit of revenge on the dealer before you die. Unbeknownst to you, the sword is a holy sword and as you pick it up, you are healed of the poison. You stand up and as the dealer looks at you in horror, you merely smirk and in a burst of speed decapitate him.")
                    case _:
                        print("Invalid choice. Please choose a valid option.")
                        sys.exit()
            case ("2","1"):
                time.sleep(2)
                third_choice = input( "1|2: ")
                match(third_choice):
                    case "1":
                        alive = False
                        print("You decide to blow the horn. As you blow the horn, you hear the sound of a chopper coming to save you,. As the chopper lands next to you, you are swiftly arrested as you are being falsely accused of killing the unicorn the horn came from. Game over.")
                        sys.exit()
                    case "2":
                        print("You decide to keep it for later as you may need it. ")
                    case _:
                        print("Invalid choice. Please choose a valid option.")
                        sys.exit()
            case("1","1"):
                time.sleep(2)
                third_choice = input( "1|2: ")
                match(third_choice):
                    case "1":
                        alive = False
                        print("As you try negotiating with the bandits, you say you will give them half of the treasure if they let you leave. They initially agree to this offer and as you make your way out of the tunnel, they ambush you and steal the other 50 percent as well as strip you of your armor. Game Over!!!")
                        sys.exit()
                    case "2":
                        print("You tell them you won't be intimidated by a measly gang of bandits.Enraged, the bandits charge at you but you're newly acquired armor set proves its worth and all their attacks feel to not even exist. You quickly overpower them and move on.")
                    case _:
                        print("Invalid choice. Please choose a valid option.")
                        sys.exit()
        print("Loading...")
        time.sleep(3)
        lore = "In light of your achievements, the king has summoned you to the castle to reward you for your bravery and skill. As you enter the grand hall, you are greeted by the king himself, who commends you for your heroic deeds. He presents you with a task to undertake, one that will test your abilities and courage to the fullest. The king explains that a great evil has arisen in the land, threatening the peace and prosperity of the kingdom. He entrusts you with the mission to confront this evil and restore balance to the realm.\n As you ponder on this task, the king informs you that should you agree to this assignment, you will have to fulfill another task." 
        lore_part_2 = "You will need to meet up with the king's trusted advisor, who will provide you with the necessary information and resources to complete your mission. The advisor is known for their wisdom and knowledge of the land, however his knowledge comes at a price. The advisor is known to be a shrewd negotiator, and he will not give away his secrets easily. You will need to prove your worth and demonstrate your skills in order to gain his trust and access the information you need."
        lore_part_3 = "The advisor will present you with a series of challenges and tests, designed to assess your abilities and determine if you are worthy of the task at hand. You will need to use your wits, strength, and cunning to overcome these obstacles and prove yourself as a capable hero. Only then will you be granted the knowledge and resources necessary to confront the great evil that threatens the kingdom."
        print(lore)
        time.sleep(12.5)
        print(lore_part_2)
        time.sleep(10.5)
        print(lore_part_3)
        time.sleep(7)
        start_adventure = input("Will you accept the king's task? (yes/no): ").strip()
        match start_adventure.lower():
            case "yes" | "y"|"yep"|"yeah"|"yup"|"yea":
                print("Loading...")
                time.sleep(2)
                print("You have accepted the king's task and are ready to embark on your adventure. You traverse the kingdom for a period of 20 days all to meet the advisor who is not even guaranteed to grant you the information. As you arrive at the advisor's tower, you are greeted by a series of challenges and tests. You must prove your worth and demonstrate your skills in order to gain his trust and access the information you need.")
        
            case "no" | "n"|"nope"|"nah"|"nay":
                print("You decide not to accept the task. Game Over!")
                alive = False
                sys.exit()
        print("Loading...")
        time.sleep(4.5)
        print("\n Your First Challenge")
        # start the first challenge after the story events
        first_challenge()
        time.sleep(5)
        if alive == True:
            Roshambo()#Second challenge. Roshambo is another term for rock, paper, scissors.
        else:
            break
        time.sleep(5)
        hacker()#The last challenge. It is a basically wordle but renamed better imo.
        print("You have successfully defeated the advisor in his trials. More will be brought to you in part two.")
        alive =  False