import random

# palabras disponibles para el juego
biblioteca = ["carpintero", "ventilador", "elefante", "circulo", "banano", "chocolate", "guitarra", "computadora",
              "pantalla", "cortina", "tambor", "espejo", "zorro", "libro", "teclado", "calcetin", "pimienta", "balon",
              "cascara", "lampara"]

# definicion de las variables a usar en el juego
validas = list("abcdefghijklmnñopqrstuv")
incorrectas = []
correctas = []
elegida = random.choice(biblioteca)
palabra = list(elegida)
enigma = ['_'] * len(palabra)
vidas = 6

# bienvenida al juego y explicacion
input("Bienvenid@ a mi juego del ahorcad@!! \nte invito a jugar a este maravilloso juego \n"
      "He seleccionado una palabra, \ntu desafío es descubrir las letras que \n"
      "la componen sin fallar más de 5 veces!! \nya que solo tienes 6 vidas, o partes del cuerpo \n"
      "Mucha suerte!!!\n"
      "ENTER PARA EMPEZAR")

print(f"Te voy a dar 6 vidas para que adivines, no las desperdicies!\n")


# funcion principal, donde el usuario elige una letra, se verifica que sea correcta o no
def verif(enigma):
    print(f"Mi palabra tiene {len(elegida)} letras \n")

    ingreso = input("Por favor, elige SOLO UNA LETRA y podrás descubrir \n"
                    "si se encuentra en mi palabra secreta! ").lower()

    for i, letra in enumerate(palabra):
        if letra == ingreso:
            enigma[i] = ingreso

    while True:
        if ingreso not in validas:
            print("Has seleccionado un caracter invalido")
            verif(enigma)
        elif len(ingreso) < 1:
            print("\nDebe ingresar alguna letra\n")
            verif(enigma)
        elif ingreso.isdigit():
            print("\nHas seleccionado un número, solo acepto letras! \n")
            verif(enigma)
        elif len(ingreso) > 1:
            print(f"\nHas seleccionado más de un caracter \n")
            verif(enigma)
        else:
            print(f"\nLa letra que seleccionaste es -----> {ingreso} ")
        return bienmal(ingreso), ingreso


# funcion para dividir el trayecto del codigo en funcion si la letra es correcta o no
def bienmal(ingreso):
    if ingreso not in palabra:
        global vidas
        vidas -= 1
        print(f"\nHAS ELEGIDO MAL\n")
        return vida(ingreso), vidas
    else:
        if ingreso not in correctas:
            correctas.append(ingreso)
            return correcto(), correctas
        else:
            print(f"\nLa letra {ingreso} ya ha sido seleccionada como correcta previamente.")
            print(f"\nlas letras correctas que has elegido son: {correctas}\n")
            return verif(enigma)


# funcion para determinar las vidas en cada iteracion del programa
def vida(ingreso):
    while vidas > 0:
        print(f"Te quedan {vidas} vidas!\n")
        if ingreso not in incorrectas:
            incorrectas.append(ingreso)
            print(f"las letras incorrectas que has elegido son: {incorrectas}\n")
            return incorrectas, verif(enigma)
        elif ingreso in incorrectas:
            print("ya has elegido esa letra incorrecta\n")
            print(f"las letras incorrectas que has elegido son: {incorrectas}\n")
            return verif(enigma)
    else:
        return print("TE HAS QUEDADO SIN VIDAS! HAS PERDIDO Y EL JUEGO SE HA ACABADO :( ")


# funcion para mostrar cartel de ganar o continuar si aun quedan letras por adivinar
def correcto():
    if "_" not in enigma:
        cartel = "*" * 30
        cartel2 = "*" * 10
        correcta = "".join(enigma)
        print(f"LA PALABRA CORRECTA ERA \n"
              f"{cartel}\n{cartel2}{correcta.upper()}{cartel2}\n{cartel}")
        print(f"HAS GANADO!! Y TE QUEDABAN {vidas} VIDAS!!")
        input("DALE ENTER PARA TERMINAR EL JUEGO")

    else:
        print(f"las letras correctas que has elegido son: {correctas}\n")
        print(f"HAS ELEGIDO BIEN, Aún te quedan {vidas} vidas!\n")
        print(enigma)
        return verif(enigma)


# funcion inicial que inicia la cadena de codigo
verif(enigma)
