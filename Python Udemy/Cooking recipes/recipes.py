from pathlib import Path, PureWindowsPath
from os import system
import os


# Directory path to work with
dir = PureWindowsPath(Path(), "Recipes")


# Welcome message to the user and clear screen
input("Welcome to your recipe book. \nPress ENTER to start")
system("cls")

# Display the path where the recipes are located
input(f"Your recipes are located at {dir}")
system("cls")

# Available options in the menu
opt = [1, 2, 3, 4, 5, 6]


# Main menu of options and verification of input validity
def options():
    system("cls")
    print("Your recipes are as follows: \n")
    for txt in Path(dir).glob("**/*.txt"):
        print(f"-{txt.stem}")
    input("Press ENTER to continue to the MENU")
    system("cls")
    option = input("\nPlease choose one of the following options: \n"
                   "1- Read recipe \n"
                   "2- Add recipe \n"
                   "3- Add category \n"
                   "4- Delete recipe \n"
                   "5- Delete category \n"
                   "6- Close the recipe book \n")
    system("cls")
    if len(option) > 1:
        print("The entered option is incorrect \n")
        return options()
    elif option.isalpha():
        print("The entered option is incorrect \n")
        return options()
    elif option > "6":
        print("The entered option is incorrect \n")
        return options()
    else:
        return option, actions(option, dir)


# Direction to the corresponding function of the choice and program closure
def actions(option, dir):
    while option < "6":
        if option == "1":
            return action1(dir)
        elif option == "2":
            return action2(dir)
        elif option == "3":
            return action3(dir)
        elif option == "4":
            return action4(dir)
        elif option == "5":
            return action5(dir)
        else:
            break
    return print("BOOK CLOSED")


# Navigate through the directory to read recipes and return to the menu
def action1(dir):
    print("Recipe categories: \n")
    for category in os.listdir(dir):
        print(category)
    choice1 = input("Enter the category you want to see: \n")
    system("cls")
    if choice1 in os.listdir(dir):
        print(f"The recipes stored in {choice1} are: \n")
        for dish in Path(dir / choice1).glob("*.txt"):
            print(dish.stem)

        choice2 = input("Choose the recipe you want to see: \n")
        if choice2 + ".txt" in os.listdir(dir / choice1):
            path1 = str(dir / choice1 / (choice2 + ".txt"))
            read1 = open(path1, "r")
            content = read1.read()
            print(content + "\n")
            read1.close()
        return input("Press ENTER to continue to the MENU \n"), options()
    else:
        print("You have selected an incorrect category \n")
        return options()


# Add a recipe, navigating through directories
def action2(dir):
    print("Recipe categories: \n")
    for folder in Path(dir).iterdir():
        if folder.is_dir():
            print(folder.name)
    choice3 = input("Enter the category where to add a recipe: \n")
    system("cls")
    if choice3 in os.listdir(dir):
        print(f"The recipes stored in {choice3} are: \n")
        for dish in Path(dir / choice3).glob("*.txt"):
            print(dish.stem)
        choice4 = input("Choose the name of the new dish: \n")
        file = open(dir / choice3 / f"{choice4}.txt", "w")
        file.write(input("Write the recipe here: \n"))
        file.close()
        return options()
    else:
        print("You have selected an incorrect category \n")
        return options()


# Add recipe category, navigating through directories
def action3(dir):
    print("Recipe categories: \n")
    for folder in Path(dir).iterdir():
        if folder.is_dir():
            print(folder.name)
    category = input("Enter the category you want to add: \n")
    if category.isalpha():
        new_folder = dir / category
        os.makedirs(new_folder)
        input(f"The new category has been created successfully, Press ENTER \n")
        system("cls")
        print("Current categories: \n")
        for folder in Path(dir).iterdir():
            if folder.is_dir():
                print(folder.name)
    else:
        print("The category name is invalid \n")

    input("Press ENTER to continue to the menu.")
    return options()


# Delete recipe, navigating through directories
def action4(dir):
    print("Recipe categories: \n")
    for category in os.listdir(dir):
        print(category)
    choice5 = input("Enter the category you want to see: \n")
    system("cls")
    if choice5 in os.listdir(dir):
        print(f"The recipes stored in {choice5} are: \n")
        for dish in Path(dir / choice5).glob("*.txt"):
            print(dish.stem)

        choice6 = input("Choose the recipe you want to delete: \n")
        os.remove(dir/choice5/f"{choice6}.txt")

        print(f"The recipes stored in {choice5} are: \n")
        for dish in Path(dir/choice5).glob("*.txt"):
            print(dish.stem)
            return options()

    else:
        print("You have selected an incorrect category \n")
        return options()


# Delete category, navigating through directories
def action5(dir):
    print("Recipe categories: \n")
    for categories in os.listdir(dir):
        print(categories)

    choice7 = input("Enter the category you want to delete: \n")
    system("cls")
    if choice7.isalpha():
        delete_folder = dir / choice7
        os.rmdir(delete_folder)
        input(f"The new category has been deleted successfully, Press ENTER \n")
        system("cls")
        print("Current categories: \n")
        for folder in Path(dir).iterdir():
            if folder.is_dir():
                print(folder.name)
    else:
        print("The category name is invalid \n")

    input("Press ENTER to continue to the menu.")
    return options()


options()
