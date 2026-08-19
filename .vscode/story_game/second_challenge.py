""" brainstorm so like what could a second challenge . Hmm. Lwk So I'd like smth like the simon says but not necessarily like the simon says yk
ugh i hate brainstorming. Oh i could lwk do riddles but how would that work, maybe i could be like """
import random 
import time
import sys
def Roshambo():
    rock = "rock"
    scissors =  "scissors"
    paper = "paper"
    gun = "gun"#😉
    Options = ["scissors","paper","rock"] #Where the advisor chooses from
    round_number_choice = ["1","2","3","4","5","6","7","8","9","10","11"]# Amount of rounds to play.
    i = int(random.choice(round_number_choice))#amount of rounds. NOT dependent on loops.
    round_number = 0
    player_points =  0
    advisor_points = 0
    Draw = True
    Tries = 1
    print(f"For your second challenge, you will be playing Rock, Paper, Scissors.\n You will choose either Rock, Paper or Scissors as a valid option.\n Rock Beats Scissors.\n Scissors Beats Paper.\n Paper Beats Rock.\n You will have {i} rounds to play.\n You will only win if you win more rounds than the advisor. Good luck. You will need it.")
    while Draw == True:
        time.sleep(5)
        while i > 0:
            Options_chosen = str(random.choice(Options))#Advisor choosing from list of options. Dependent on loop so that it is not the same everytime.
            live = input("Choose an Option.\n 1. Rock\n 2. Paper \n 3. Scissors\n Input them by name(Check for Spelling as well.):").lower().strip() #To make sure that input is not case sensitive.
            if live == "gun":
                print("I see what you did there.") #Free skip so you don't have to play the game. 
                break
            #Could use match case but it would be too much work and I don't want to do that. So if elif statements it is.
            if live == Options_chosen:
                print (f"You chose {live} and The Advisor chose the same as you neither of you will gain a point.")
            elif live == "scissors" and Options_chosen == "rock":
                print(f"You have chosen {live} and The Advisor chose {Options_chosen}. You lost. The Advisor gains a point")
                advisor_points += 1
            elif live == "scissors" and Options_chosen == "paper":
                print(f"You have chosen {live} and The Advisor chose {Options_chosen}. You won. You gain a point")
                player_points += 1
            elif live == "paper" and Options_chosen == "rock":
                print(f"You have chosen {live} and The Advisor chose {Options_chosen}. You won. You gain a point")
                player_points += 1
            elif live == "paper" and Options_chosen == "scissors":
                print(f"You have chosen {live} and The Advisor chose {Options_chosen}. You lost. The Advisor gains a point")
                advisor_points += 1
            elif live == "rock" and Options_chosen == "scissors":
                print(f"You have chosen {live} and The Advisor chose {Options_chosen}. You won. You gain a point")
                player_points += 1
            elif live == "rock" and Options_chosen == "paper":
                print(f"You have chosen {live} and The Advisor chose {Options_chosen}. You lost. The Advisor gains a point")
                advisor_points += 1
            else:
                print("Invalid Choice.\n If only you had listened. As your punishment, you will be starting from the beginning.")
                sys.exit()
            i-=1
            round_number+=1
            print(f"You have played {round_number} rounds. You have {i} rounds remaining.")
            time.sleep(2.5)
        
        if player_points > advisor_points:
            print(f"You gained {player_points} points and the advisor gained... DRUMROLL")
            time.sleep(1)
            print(f"{advisor_points} points")
            print("Congratulations. You won the second challenge")
            print(f"It took you {Tries} attempts. Good job.")
            Draw = False
        elif player_points < advisor_points:
            print(f"You gained {player_points} points and the advisor gained... DRUMROLL")
            time.sleep(1)
            print(f"{advisor_points} points")
            print("You lost. Do better next time.")
            Draw = True
            Tries +=1
        elif player_points == advisor_points and live != "gun":
            print(f"You gained {player_points} points and the advisor gained... DRUMROLL")
            time.sleep(1)
            print(f"{advisor_points} points")
            print("Sadly, you drawed with The Advisor. Try Again.")
            Draw = True
            Tries +=1
        elif live == "gun":
            Draw = False
        else:
            ValueError

        
