from pathlib import Path, PureWindowsPath
from os import system
import os

# ruta del directorio a trabajar
dir = PureWindowsPath(Path.home(), "Recetas")

# bienvenida al usuario y clear screen
input("Bienvenido a tu libro de recetas. \nPulsa ENTER para comenzar")
system("cls")

# muestra la ruta donde se encuentran las recetas
input(f"Tus recetas se encuentran en {dir}")
system("cls")

# opciones disponibles del menu
opt = [1, 2, 3, 4, 5, 6]


# menu principal de opciones y verificacion de validez del ingreso
def opciones():
    system("cls")
    print("Tus recetas son las siguientes: \n")
    for txt in Path(dir).glob("**/*.txt"):
        print(f"-{txt.stem}")
    input("Pulse ENTER para continuar al MENU")
    system("cls")
    opcion = input("\nPor favor elige una de las siguientes opciones: \n"
                   "1- Leer receta \n"  
                   "2- Agregar receta \n" 
                   "3- Agregar categoría \n" 
                   "4- Eliminar receta \n" 
                   "5- Eliminar categoría \n" 
                   "6- Cerrar el libro de recetas \n")
    system("cls")
    if len(opcion) > 1:
        print("La opción ingresada es incorrecta \n")
        return opciones()
    elif opcion.isalpha():
        print("La opción ingresada es incorrecta \n")
        return opciones()
    elif opcion > "6":
        print("La opción ingresada es incorrecta \n")
        return opciones()
    else:
        return opcion, acciones(opcion, dir)


# direccionamiento a la funcion correspondiente de la eleccion y cierre del programa
def acciones(opcion, dir):
    while opcion < "6":
        if opcion == "1":
            return accion1(dir)
        elif opcion == "2":
            return accion2(dir)
        elif opcion == "3":
            return accion3(dir)
        elif opcion == "4":
            return accion4(dir)
        elif opcion == "5":
            return accion5(dir)
        else:
            break
    return print("LIBRO CERRADO")


# navegar por el directorio para leer recetas y volver al menu
def accion1(dir):
    print("Categoria de recetas: \n")
    for categoria in os.listdir(dir):
        print(categoria)
    eleccion1 = input("Ingrese la categoria que quiera ver: \n")
    system("cls")
    if eleccion1 in os.listdir(dir):
        print(f"Las recetas guardadas en {eleccion1} son: \n")
        for plato in Path(dir / eleccion1).glob("*.txt"):
            print(plato.stem)

        eleccion2 = input("Elija la receta que quiera ver: \n")
        if eleccion2 + ".txt" in os.listdir(dir / eleccion1):
            ruta1 = str(dir / eleccion1 / (eleccion2 + ".txt"))
            leer1 = open(ruta1, "r")
            cont = leer1.read()
            print(cont + "\n")
            leer1.close()
        return input("Pulse ENTER para continuar al MENU \n"), opciones()
    else:
        print("Ha seleccionado una categoria incorrecta \n")
        return opciones()


# agregar una receta, navegando por los directorios
def accion2(dir):
    print("Categorias de recetas: \n")
    for carpeta in Path(dir).iterdir():
        if carpeta.is_dir():
            print(carpeta.name)
    eleccion3 = input("Ingrese la categoria donde agregar una receta: \n")
    system("cls")
    if eleccion3 in os.listdir(dir):
        print(f"Las recetas guardadas en {eleccion3} son: \n")
        for plato in Path(dir / eleccion3).glob("*.txt"):
            print(plato.stem)
        eleccion4 = input("Elija el nombre del nuevo plato: \n")
        archivo = open(dir / eleccion3 / f"{eleccion4}.txt", "w")
        archivo.write(input("Escriba la receta aqui: \n"))
        archivo.close()
        return opciones()
    else:
        print("Ha seleccionado una categoria incorrecta \n")
        return opciones()


# agregar categoria de recetas, navegando por los directorios
def accion3(dir):
    print("Categorias de recetas: \n")
    for carpeta in Path(dir).iterdir():
        if carpeta.is_dir():
            print(carpeta.name)
    categoria = input("Ingrese la categoria que desea agregar: \n")
    if categoria.isalpha():
        nueva_carpeta = dir / categoria
        os.makedirs(nueva_carpeta)
        input(f"La nueva categoría se ha creado con éxito, Pulse ENTER \n")
        system("cls")
        print("Categorías actuales: \n")
        for carpeta in Path(dir).iterdir():
            if carpeta.is_dir():
                print(carpeta.name)
    else:
        print("El nombre de la categoria es invalido \n")

    input("Presione ENTER para continuar al menú.")
    return opciones()


# eliminar receta, navegando por los directorios
def accion4(dir):
    print("Categoria de recetas: \n")
    for categoria in os.listdir(dir):
        print(categoria)
    eleccion5 = input("Ingrese la categoria que quiera ver: \n")
    system("cls")
    if eleccion5 in os.listdir(dir):
        print(f"Las recetas guardadas en {eleccion5} son: \n")
        for plato in Path(dir / eleccion5).glob("*.txt"):
            print(plato.stem)

        eleccion6 = input("Elija la receta que desea eliminar: \n")
        os.remove(dir/eleccion5/f"{eleccion6}.txt")

        print(f"Las recetas guardadas en {eleccion5} son: \n")
        for plato in Path(dir/eleccion5).glob("*.txt"):
            print(plato.stem)
            return opciones()

    else:
        print("Ha seleccionado una categoria incorrecta \n")
        return opciones()


# eliminar categoria, navegando por los directorios
def accion5(dir):
    print("Categoria de recetas: \n")
    for categorias in os.listdir(dir):
        print(categorias)

    eleccion7 = input("Ingrese la categoria que quiera eliminar: \n")
    system("cls")
    if eleccion7.isalpha():
        borrar_carpeta = dir / eleccion7
        os.rmdir(borrar_carpeta)
        input(f"La nueva categoría se ha borrado con éxito, Pulse ENTER \n")
        system("cls")
        print("Categorías actuales: \n")
        for carpeta in Path(dir).iterdir():
            if carpeta.is_dir():
                print(carpeta.name)
    else:
        print("El nombre de la categoria es invalido \n")

    input("Presione ENTER para continuar al menú.")
    return opciones()


opciones()
