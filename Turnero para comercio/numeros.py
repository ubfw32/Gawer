cartel = "*" * 10


# decoracion para generadores
def decorar(gen):
    def turn():
        print(f"su turno es: \n{cartel*2}")
        print(f"---->    {next(gen)}    <----")
        print(f"{cartel*2}\nAguarde y será atendido \n")
    return turn

# turnos simulados para testeo
t1 = 65
t2 = 3
t3 = 113


# generador de turnos 1
def gen1(t1):
    while True:
        t1 += 1
        yield t1


# generador de turnos 2
def gen2(t2):
    while True:
        t2 += 1
        yield t2


# generador de turnos 3
def gen3(t3):
    while True:
        t3 += 1
        yield t3


# se guarda la funcion generadora(gen(t)) en una variable(genx)
gen1 = gen1(t1)
gen2 = gen2(t2)
gen3 = gen3(t3)

# se guarda la variable generadora(genx) con su decorador(decorar()) en otra variable(dx)
d1 = decorar(gen1)
d2 = decorar(gen2)
d3 = decorar(gen3)
