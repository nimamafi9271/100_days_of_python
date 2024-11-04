# This is the code for day 4 project

import random
from signs_module import rock, paper, scissors
signs = [rock, paper, scissors]
player_choice = signs[int(input("What do you choose? Type 0 for rock, 1 for Paper, or 2 for Scissors.\n"))]
print(f"Your choice:\n{player_choice}")
computer_choice = random.choice(signs)
print(f"Computer choice:\n{computer_choice}")

winning_cases = {rock:scissors, scissors:paper, paper:rock}

if player_choice == computer_choice:
    print("It's a draw")
elif winning_cases[player_choice] == computer_choice:
    print("You Win!")
else:
    print("You Lose!")