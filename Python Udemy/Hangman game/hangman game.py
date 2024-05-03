import random

# Available words for the game
library = ["carpenter", "fan", "elephant", "circle", "banana", "chocolate", "guitar", "computer",
           "screen", "curtain", "drum", "mirror", "fox", "book", "keyboard", "sock", "pepper", "ball",
           "shell", "lamp"]

# Definition of variables to use in the game
valid = list("abcdefghijklmnñopqrstuvwxyz")
incorrect = []
correct = []
chosen = random.choice(library)
word = list(chosen)
puzzle = ['_'] * len(word)
lives = 6

# Welcome message and instructions
input("Welcome to my Hangman game!! \nI invite you to play this wonderful game \n"
      "I have selected a word, \nyour challenge is to discover the letters that \n"
      "compose it without failing more than 5 times!! \nsince you only have 6 lives, or parts of the body \n"
      "Good luck!!!\n"
      "PRESS ENTER TO START")

print(f"I'll give you 6 lives to guess, don't waste them!\n")


# Main function, where the user chooses a letter, it is verified if it's correct or not
def check(puzzle):
    print(f"My word has {len(chosen)} letters \n")

    entry = input("Please, choose ONLY ONE LETTER and you'll find out \n"
                  "if it's in my secret word! ").lower()

    for i, letter in enumerate(word):
        if letter == entry:
            puzzle[i] = entry

    while True:
        if entry not in valid:
            print("You have selected an invalid character")
            check(puzzle)
        elif len(entry) < 1:
            print("\nYou must enter some letter\n")
            check(puzzle)
        elif entry.isdigit():
            print("\nYou selected a number, I only accept letters! \n")
            check(puzzle)
        elif len(entry) > 1:
            print(f"\nYou selected more than one character \n")
            check(puzzle)
        else:
            print(f"\nThe letter you selected is -----> {entry} ")
        return rightwrong(entry), entry


# Function to divide the code flow based on whether the letter is correct or not
def rightwrong(entry):
    if entry not in word:
        global lives
        lives -= 1
        print(f"\nYOU CHOSE WRONG\n")
        return life(entry), lives
    else:
        if entry not in correct:
            correct.append(entry)
            return correct_guess(), correct
        else:
            print(f"\nThe letter {entry} has already been selected as correct previously.")
            print(f"\nThe correct letters you have chosen are: {correct}\n")
            return check(puzzle)


# Function to determine the lives in each iteration of the program
def life(entry):
    while lives > 0:
        print(f"You have {lives} lives left!\n")
        if entry not in incorrect:
            incorrect.append(entry)
            print(f"The incorrect letters you have chosen are: {incorrect}\n")
            return incorrect, check(puzzle)
        elif entry in incorrect:
            print("You have already chosen that incorrect letter\n")
            print(f"The incorrect letters you have chosen are: {incorrect}\n")
            return check(puzzle)
    else:
        return print("YOU RAN OUT OF LIVES! YOU LOST AND THE GAME IS OVER :( ")


# Function to display winning message or continue if there are still letters to guess
def correct_guess():
    if "_" not in puzzle:
        banner = "*" * 30
        banner2 = "*" * 10
        correct_word = "".join(puzzle)
        print(f"THE CORRECT WORD WAS \n"
              f"{banner}\n{banner2}{correct_word.upper()}{banner2}\n{banner}")
        print(f"YOU WON!! AND YOU HAD {lives} LIVES LEFT!!")
        input("PRESS ENTER TO END THE GAME")

    else:
        print(f"The correct letters you have chosen are: {correct}\n")
        print(f"YOU CHOSE RIGHT, You still have {lives} lives!\n")
        print(puzzle)
        return check(puzzle)


# Initial function that starts the code chain
check(puzzle)