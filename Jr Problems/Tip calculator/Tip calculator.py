def calc():
    print("What's the total bill for today, please?")
    b = int(input())
    p = int(input('How many people pay for the bill?'))

    if p == 1:
        print(f'Perfect, total bill will be ${b} for you')
        at = input('Do you want to make a tip? Y/N')
        anst = at.lower()
        if anst == 'y':
            t = int(input('Thanks! What percentage of tip?\n'
                          '1) 18%\n'
                          '2) 20%\n'
                          '3) 25%\n'))
            if t == 1:
                tip = (b * 18) // 100
                bt = b + tip
                print(f'Your tip is {tip}, and total is {bt}')
            elif t == 2:
                tip = (b * 20) // 100
                bt = b + tip
                print(f'Your tip is {tip}, and total is {bt}')
            elif t == 3:
                tip = (b * 25) // 100
                bt = b + tip
                print(f'Your tip is {tip}, and total is {bt}')
            else:
                 print('Invalid answer')

        elif anst == 'n':
            print('Thanks for nothing, anyway... I spit on your food.')

    elif p > 1:
        bill = b // p
        print(f'Total will be ${bill} for {p} customers')
        at = input('Do you want to make a tip? Y/N')
        anst = at.lower()
        if anst == 'y':
            t = int(input('Thanks! What percentage of tip?\n'
                          '1) 18%\n'
                          '2) 20%\n'
                          '3) 25%\n'))
            if t == 1:
                tip = (bill * 18) // 100
                bt = bill + tip
                print(f'Your tip is {tip} for person, and total is {bt} for person\n'
                      f'Total for all is {tip * p} in tips and {bill * p} for services')
            elif t == 2:
                tip = (bill * 20) // 100
                bt = bill + tip
                print(f'Your tip is {tip} for person, and total is {bt} for person\n'
                      f'Total for all is {tip * p} in tips and {bill * p} for services')
            elif t == 3:
                tip = (bill * 25) // 100
                bt = bill + tip
                print(f'Your tip is {tip} for person, and total is {bt} for person\n'
                      f'Total for all is {tip * p} in tips and {b} for services')
            else:
                print('Invalid answer')

    else:
        print('Invalid answer')
        calc()


calc()