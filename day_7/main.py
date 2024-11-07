# Day 7 project
# This is the code for the Hangman game

import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False
guessed_letters = []
lives = 6

while not game_over:
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")

    guess = input("guess a letter: ")

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            guessed_letters.append(letter)
        elif letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"*********************** It was {chosen_word}!, YOU LOSE **********************")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    print(stages[lives])