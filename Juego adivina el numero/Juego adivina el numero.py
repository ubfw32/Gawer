from random import randint

# se define el numero a adivinar y la cantidad de intentos disponibles
numero = randint(1, 100)
oportunidades = [1, 2, 3, 4, 5, 6, 7, 8]

# pide el nombre al usuario e informa como funciona el juego
nombre = input("Hola! bienvenido al juego de la adivinanza, para empezar dime tu nombre: \n")
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos "
      f"para adivinar, cuál crees que es el número?")

# por cada iteracion de oportunidades se detalla lo que pasa en cada caso
for op in oportunidades:
    if op == 8:
        print("ULTIMA OPORTINIDAD!!")

    res = input(f"Elige un numero del 1 al 100 a ver si tienes suerte, tienes {9 - op} intentos: \n")
    resp = int(res)

    if resp < 0 or resp > 101:
        print("INCORRECTO: \nelegiste un numero no valido. \n")
    elif resp < numero:
        print("INCORRECTO: \nel numero que elegiste es MENOR al numero ganador. \n")
    elif resp > numero:
        print("INCORRECTO: \nel numero que elegiste es MAYOR al numero ganador. \n")
    elif resp == numero:
        print(f"CORRECTO!!! HAS GANADOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!\n"
              f"Te ha llevado {op} intendos ganar!")
        break

    if op == 8:
        print(f"el numero secreto era: {numero}")

"""  
     elif resp not != numero:
  TAMBIEN SE PUEDE HACER CON WHILE"""

