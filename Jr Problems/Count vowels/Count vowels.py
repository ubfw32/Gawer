

word = input('Enter some word to analize: \n')
w = word.lower()

def count(w):
    l = ['a', 'e', 'i', 'o', 'u']
    w = word.lower()

    n = 0
    for le in w:
        if le in l:
            n += 1

    print(f'Your word have {n} vowels')
    return n


count(w)


