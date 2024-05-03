import decimal

num = float(input('Choose a decimal number under 1,024\n'))


def dec(num):
    bi = ''
    i = int(num)
    integ = bin(i)[2:]
    bi += integ
    bi += '.'
    f = int(num * 1024)
    flo = bin(f)[2:]
    bi += flo
    return bi


dec(num)

bi = dec(num)

print(f"Binary representation of {num} is: {bi}")
