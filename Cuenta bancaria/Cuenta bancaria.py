class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        return f"{self.nombre} {self.apellido} \n Su N° de cuenta es {self.cuenta} \n Su balance es {self.balance}"

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"{self.nombre} {self.apellido} \n Se han depositado {cantidad}$ \n"
              f"En su cuenta N°{self.cuenta} y su total es de: {self.balance}$")

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"{self.nombre} {self.apellido} \n Se han retirado {cantidad}$ \n"
                  f"De su cuenta N°{self.cuenta} y su total es de: {self.balance}")
        else:
            print("No es posible retirar el monto ingresado")


def cliente_nuevo():
    nombre_c = input("Ingrese su nombre: \n")
    apellido_c = input("Ingrese su apellido: \n")
    cuenta_c = input("Ingrese su numero de 4 digitos: \n")
    client = Cliente(nombre_c, apellido_c, cuenta_c)
    return client


def inicio():
    mi_cliente = cliente_nuevo()
    print(mi_cliente)
    resp = 0

    while resp != "4":
        resp = input("Elija una opcion: \n1) DEPOSITAR \n2) RETIRAR \n3)SALIR \n")

        if resp == "1":
            monto_d = int(input("Ingrese la cantidad a depositar: \n"))
            mi_cliente.depositar(monto_d)

        elif resp == "2":
            monto_r = int(input("Ingrese la cantidad a retirar: \n"))
            mi_cliente.retirar(monto_r)

        elif resp == "3":
            print("Gracias por utilizar nuestro servicio.")
            break
        else:
            print("Opcion invalida")


inicio()
