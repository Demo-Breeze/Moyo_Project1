import random
import string

scrabble_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

Player1_score = 0
Player2_score = 0

# Get rounds first so we can loop properly
rounds = int(input("Enter the number of rounds you want to play: "))

for r in range(rounds):
    print(f"\n--- Round {r + 1} ---")
    
    # 1. Generate uppercase letter racks for the round
    letters1 = random.choices(string.ascii_uppercase, k=7)
    letters2 = random.choices(string.ascii_uppercase, k=7)
    
    print(f"Player 1 Rack: {letters1}")
    player1_word = input("Enter Player 1 word: ").upper()
    
    print(f"Player 2 Rack: {letters2}")
    player2_word = input("Enter Player 2 word: ").upper()
    
    # 2. Validate Player 1
    p1_valid = True
    # Copy rack to safely track used letters
    rack1_copy = letters1.copy() 
    
    if len(player1_word) > 7 or len(player1_word) == 0:
        p1_valid = False
    else:
        for letter in player1_word:
            if letter in rack1_copy:
                rack1_copy.remove(letter) # Remove letter so it can't be reused
            else:
                p1_valid = False
                break
                
    # 3. Validate Player 2
    p2_valid = True
    rack2_copy = letters2.copy()
    
    if len(player2_word) > 7 or len(player2_word) == 0:
        p2_valid = False
    else:
        for letter in player2_word:
            if letter in rack2_copy:
                rack2_copy.remove(letter)
            else:
                p2_valid = False
                break

    # 4. Score the round if words are valid
    if p1_valid:
        round1_score = sum(scrabble_scores.get(char, 0) for char in player1_word)
        Player1_score += round1_score
        print(f"Player 1 score this round: {round1_score}")
    else:
        print(f"Player 1 played an invalid word! 0 points.")
        
    if p2_valid:
        round2_score = sum(scrabble_scores.get(char, 0) for char in player2_word)
        Player2_score += round2_score
        print(f"Player 2 score this round: {round2_score}")
    else:
        print(f"Player 2 played an invalid word! 0 points.")

# 5. Declare final winner
print("\n=== FINAL GAME OVER ===")
if Player1_score > Player2_score:
    print(f"Player 1 wins the game with a final score of {Player1_score} to {Player2_score}!")
elif Player2_score > Player1_score:
    print(f"Player 2 wins the game with a final score of {Player2_score} to {Player1_score}!")
else:
    print(f"It's a tie game! Both players scored {Player1_score}.")
