banner = "*" * 10


# Decoration for generators
def decorate(gen):
    def turn():
        print(f"Your turn is: \n{banner*2}")
        print(f"---->    {next(gen)}    <----")
        print(f"{banner*2}\nPlease wait to be attended \n")
    return turn

# Simulated turns for testing
t1 = 65
t2 = 3
t3 = 113


# Generator for turns 1
def gen1(t1):
    while True:
        t1 += 1
        yield t1


# Generator for turns 2
def gen2(t2):
    while True:
        t2 += 1
        yield t2


# Generator for turns 3
def gen3(t3):
    while True:
        t3 += 1
        yield t3


# The generator function (gen(t)) is stored in a variable (genx)
gen1 = gen1(t1)
gen2 = gen2(t2)
gen3 = gen3(t3)

# The generator variable (genx) with its decorator (decorate()) is stored in another variable (dx)
d1 = decorate(gen1)
d2 = decorate(gen2)
d3 = decorate(gen3)
