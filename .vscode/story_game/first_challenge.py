import random
import sys
import time
from typing import List
def first_challenge():
            simon_says = ["Up","Down","Left","Right"]
            round_number_choice = ["1","2","3","4","5","6","7","8","9","10","11"]
            i = int(random.choice(round_number_choice))
            round_number = 1
            
            print("The rules of this game are:\n Everything Simon says will disappear after 1.0 seconds. Make sure to memorize the direction")

            while i > 0:
                chosen_list = random.choices(simon_says, k=3)
                simon_says_output = " ".join(chosen_list).strip().lower()
                print("You will have", i, "rounds to play. The number of rounds you have to play are random.")
                time.sleep(5.0)
                print("Simon says: ", simon_says_output)
                time.sleep(1.0)
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
                sys.stdout.flush()
                i= i - 1
                round_number += 1
                answer = input("Enter the direction Simon said: ").strip().lower()

                if answer == "obama":
                      i = 0
                      
                if answer != "obama":
                    if answer == simon_says_output.lower() and i>0:
                        print("Correct! Time for round ", round_number)
                    elif answer == simon_says_output.lower() and i==0:
                        print("Correct! You have passed this challenge")
                    else:
                        print("Incorrect! The correct answer was: ", simon_says_output)
                        print("You were truly not worthy of the king's task. You have failed the challenge and must start over.")
                        alive = False
                        sys.exit()
                        break