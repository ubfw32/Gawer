from numbers import *


# Main menu, according to the user's choice, the corresponding decorated generator is executed
def take_turn():
    print("Welcome to your trusted store\n")
    choice = int(input("Choose a sector to take your turn: "
                       "\n 1) Perfumery\n 2) Pharmacy\n 3) Cosmetics\n 4) EXIT\n"))

    while choice != 4:
        if choice == 1:
            d1()
            return take_turn()

        if choice == 2:
            d2()
            return take_turn()

        if choice == 3:
            d3()
            return take_turn()

        elif choice not in [1, 2, 3]:
            print("Invalid choice")
            return take_turn()
    else:
        print("Thank you for coming")


take_turn()
