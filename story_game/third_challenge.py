import random 
import sys 
def hacker():#Hacker is such a good word to call this ig. It reminds me of the spy movies.
    hack_words = [ #words for hacker. Seven letter words and a hundred of them to prevent you from memorizing them all.
        "ACADEMY","AIRLINE", "AMAZING", "ANCIENT", "ANOTHER",
        "BALANCE","BEDROOM", "BENEFIT", "BICYCLE", "BOUNDED",
        "CAPTAIN","CENTURY", "CISTERN", "CHAPTER", "CIRCUIT", 
        "COMPANY","COMPLEX", "CONCERT", "CONNECT", "CONTROL", 
        "COOKING","CULTURE", "CURIOUS", "DESKTOP", "DIAMOND", 
        "DISPLAY","DISTANT", "EARNEST", "EASIEST", "ECONOMY", 
        "EMOTION","EVENING", "EXAMPLE", "EXPLAIN", "FACTORY", 
        "FANTASY","FEATURE", "FESTIVE", "FICTION", "FISHING", 
        "FORTUNE","FREEDOM", "GARBAGE", "GARDENS", "GENERAL", 
        "GENUINE","GRAVITY", "HAPPILY", "HARMONY", "HEALTHY", 
        "HISTORY","HOLIDAY", "HOUSING", "IMAGINE", "INCLUDE", 
        "INSTANT","JACKETS", "JOURNAL", "JOURNEY", "JUSTICE", 
        "KETCHUP","KINGDOM", "KITCHEN", "LEARNED", "LECTURE", 
        "LIBRARY","LICENSE", "MACHINE", "MANAGER", "MARBLES", 
        "MESSAGE","MINERAL", "MISSION", "MONSTER", "MORNING", 
        "MYSTERY","NATURAL", "NETWORK", "NOTHING", "OPINION", 
        "ORGANIC","OUTSIDE", "PACKAGE", "PAINFUL", "PARKING", 
        "PATIENT","PENCILS", "PICTURE", "PLASTIC", "POPULAR", 
        "PORTION","PROBLEM", "PROJECT", "PROMISE", "QUALITY", 
        "QUICKLY","RAINBOW", "READING", "REALIZE", "RESPECT", 
        "REVENUE","ROUTINE", "SUNRISE", "SCIENCE", "SEASONS", 
        "SERIOUS","SESSION", "SOCIETY", "SPECIAL", "STATION", 
        "STORAGE","STUDENT", "SUCCESS", "SUPPORT", "SURFACE", 
        "TEACHER","THEATER", "THOUGHT", "THUNDER", "TONIGHT",
        "TOURIST","TRAFFIC", "TRAVELS", "TRIUMPH", "TUESDAY", 
        "UNKNOWN","VACCINE", "VARIETY", "VEHICLE", "VERSION", 
        "VICTORY","VILLAGE", "VIRTUAL", "VISIBLE", "WARNING", 
        "WEATHER","WEEKEND", "WELCOME", "WITNESS", "WORKING"
    ]
 
    round_number_choice = ["1", "2", "3"]
    point = 0
    Loss = 0
    total_rounds = int(random.choice(round_number_choice)) #How many rounds to play based on your luck.
    max_guesses = 6 #Six guesses for a good challenge ig.
    print(f"Welcome! You'll play {total_rounds} round(s) of Word Guess.\n")
    round_num = 1
    while round_num <= total_rounds: #Play the specified number of rounds
        word = random.choice(hack_words) #Chooses a random word from the list of words each round.
        word_length = len(word)
        guesses_left = max_guesses #used as two seperate variable so when round ends, you get the same amount of guesses rather than using the previous round's guesses left.
        print(f"--- Round {round_num} ---")
        print(f"Guess the {word_length}-letter word. You have {max_guesses} tries.\n")
 
        won = False# later in loop
        while guesses_left > 0:
            guess = input(f"Guess ({guesses_left} left): ").strip().upper()
            if guess == "OBAMA":
                point = 100000000
                break
             #to make it easier for me and make it so that no spaces and no small letters.
            if len(guess) != word_length: #Pretty straightforward isn't it?
                print(f"Word must be exactly {word_length} letters. Try again.")
                continue
            if guess.isalpha() != True:
                print(f"Word must be exactly {word_length} letters. Try again.")
                continue
 
            if guess == word: #Ez
                print(" Correct! You guessed it!\n")
                point +=1
                won = True
                break

 
            feedback = ""
            for i, char in enumerate(guess): #Gets the value and index of the guess and compares it to the word. If the letter is in the right place, it gives a green square. If it's in the word but not in the right place, it gives a yellow square. If it's not in the word at all, it gives a white square.
                if guess == "OBAMA":
                    break
                if char == word[i]:
                    feedback += "🟩"
                elif char in word:
                    feedback += "🟨"
                else:
                    feedback += "⬜"
        if guess != "OBAMA":

            print(f"{guess}")
            print(f"{feedback}\n")
            guesses_left -= 1
 
        if not won and guess!= "OBAMA":#Losing in the first place is wild but makes it so that won makes u lose
            print(f"Out of guesses! The word was: {word} 🤪\n")
            Loss +=1
 
        round_num += 1
    if guess != "OBAMA":
        if round_num >= total_rounds and point > Loss and point != Loss and Loss == 0:
            print(f"You won with a flawless performance! You guessed {point} word(s) correctly and lost {Loss} round(s).")
            print("Thanks for playing!")
        elif round_num >= total_rounds and point > Loss and point != Loss and Loss != 0:
            print(f"You won! You guessed {point} word(s) correctly and lost {Loss} round(s).")
            print("Thanks for playing!")
            sys.exit()
        elif round_num >= total_rounds and point < Loss and point != Loss and point != 0:
            print(f"You lost! You guessed {point} word(s) correctly and lost {Loss} round(s).")
            print("Thanks for playing but better luck next time!")
        elif round_num >= total_rounds and point < Loss and point != Loss and point == 0:
            print(f"You failed every round! How did you even manage to do that? You guessed {point} word(s) correctly and lost {Loss} round(s).")
        elif point==Loss and round_num >= total_rounds:
            print(f"You tied! You guessed {point} word(s) correctly and lost {Loss} round(s).")
            print("Thanks for playing but a draw is not good enough! Better luck next time!")