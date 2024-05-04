def pal():
    word = input('Inser a word to see if its a palindrom: \n')
    if word[::-1] == word:
        print(f'{word} IS a palindrome')
        pal()
    elif word[::-1] != word:
        print(f'{word} IS NOT a palindrome')
        pal()
    elif word.isalpha():
        print('Numbers are not allowed')
        pal()
    else:
        print('Error, try again')
        pal()

pal()