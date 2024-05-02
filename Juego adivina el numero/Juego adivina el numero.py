from random import randint

# define number and amount of tries
number = randint(1, 100)
tries = [1, 2, 3, 4, 5, 6, 7, 8]

# ask the user name and explain the game
name = input("Hello! Welcome to the guessing game. To start, tell me your name: \n")
print(f"Well, {name}, I have thought of a number between 1 and 100. " 
      f"You have only eight attempts to guess. What do you think the number is?")

# for any iteration of tries
for op in tries:
    if op == 8:
        print("LAST CHANCE!!")

    ans = input(f"Elige un numero del 1 al 100 a ver si tienes suerte, tienes {9 - op} intentos: \n")
    ans2 = int(ans)

    if ans2 < 0 or ans2 > 101:
        print("INCORRECT: \nYou chose an invalid number. \n")
    elif ans2 < number:
        print("INCORRECT: \nThe number you chose is LESS than the winning number. \n")
    elif ans2 > number:
        print("INCORRECT: \nThe number you chose is GREATER than the winning number. \n")
    elif ans2 == number:
        print(f"YEEEEES!!! YOU WIIIIIIIIIIIIIIIIIIIIN!!!\n"
              f"You took {op} tries to win!")
        break

    if op == 8:
        print(f"el numero secreto era: {number}")

"""  
     elif resp not != numero:
  TAMBIEN SE PUEDE HACER CON WHILE"""

