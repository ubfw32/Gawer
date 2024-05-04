def transform():
    inp = input('Choose a phrase to show the Acronym: ')
    words = list(inp.split())
    a = []
    for w in words:
        for l in w[0]:
            a.append(l)
    acr = ".".join(a)
    print(acr.upper())
    return acr


transform()

