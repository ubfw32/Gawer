from numeros import *


# menu principal, segun la eleccion del usuario se ejecuta el generador decorado correspondiente
def sacar_turno():
    print("Bienvenido a su comercio de confianza\n")
    eleccion = int(input("Elija un sector para sacar su turno: "
                         "\n 1)Perfumeria\n 2)Farmacia\n 3)Cosmetica\n 4)SALIR\n"))

    while eleccion != 4:
        if eleccion == 1:
            d1()
            return sacar_turno()

        if eleccion == 2:
            d2()
            return sacar_turno()

        if eleccion == 3:
            d3()
            return sacar_turno()

        elif eleccion not in [1, 2, 3]:
            print("Eleccion invalida")
            return sacar_turno()
    else:
        print("Gracias por venir")


sacar_turno()
