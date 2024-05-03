'''Odd or even
Welcome a user then ask them for a number between 1 and 1000.

When the user gives you the number, you check if it's odd or even and then you
print a message letting them know.

Example:

Prompt: What number are you thinking?
Input: 25
Output: That's an odd number! Have another?  '''


def ooe():
    num = int(input('Hello! please select a number between 1 and 1000'))

    if num > 1000 or num < 1:
        print('Invalid number')
        ooe()

    num2 = bin(num)[-1]

    if num2 == '0':
        print("That's an even number!")
        ooe()

    elif num2 == '1':
        print("That's an odd number!")
        ooe()


ooe()
