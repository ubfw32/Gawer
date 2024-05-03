import operator

num1 = int(input('Inser a number: \n'))
num2 = int(input('Inser a second number: \n'))
ans = int(input('What operation do you want? \n1)ADD \n2)SUBTRACT \n3)MULTIPLY \n4)DIVIDE'))


def calc(num1, ans, num2):
    if ans == 1:
        ans1 = operator.add(num1, num2)
        return ans1

    elif ans == 2:
        ans2 = operator.sub(num1, num2)
        return ans2

    elif ans == 3:
        ans3 = operator.mul(num1, num2)
        return ans3

    elif ans == 4:
        ans4 = operator.floordiv(num1, num2)
        return ans4

    else:
        print('Invalid answer')
        calc(num1, ans, num2)


resp = calc(num1, ans, num2)

print(resp)




