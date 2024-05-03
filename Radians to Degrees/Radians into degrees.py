import numpy as np

input('Insert to start')


def convertir():
    opt = input('Choice one option: \n1)Degrees to radians \n2)Radians to Degrees')
    if int(opt) == 1:
        return opt1()
    elif int(opt) == 2:
        return opt2()
    else:
        print('Invalid option')
        convertir()


def opt1():
    res1 = int(input('Insert degrees to convert into radians'))
    rad = np.radians
    print(f'{res1}° Degrees are {round(rad(res1), 5)} Radians')


def opt2():
    res2 = int(input('Insert radians into converto to degrees '))
    deg = np.degrees
    print(f'{res2}° Radians are {round(deg(res2), 4)} Degrees')


convertir()
