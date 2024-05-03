'''7. Repeat Characters

Create a function that accepts strings. The function thus created should be able to
return a string where each character is doubled in the original string.

For instance, if the parameter of the function is “now”, then it should return “nnooww”. '''


str = input('Enter a word: \n')

def double(str):
    str2 = ''
    for s in str:
        str2 += s * 2
    print(str2)
    return str2


str2 = double(str)