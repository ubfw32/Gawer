# PASO 1
# input user text and lowercase 
texto = input("Write here any text with 30 characters or more: ")
texto = texto.lower()

# input user + letter counting + print appears
a = input("write a letter you want to search in text: ")
a = a.lower()
result1 = texto.count(a)
print(f"your letter appears: {result1} times")

b = input("write a second letter you want to search: ")
b = b.lower()
result2 = texto.count(b)
print(f"your second letter appears: {result2} times")

c = input("write a third letter you want to search: ")
c = c.lower()
result3 = texto.count(c)
print(f"your third letter appears: {result3} times")

# PASO 2
# text to list
separa = list(texto)

# word split
separa = texto.split()

# total words in text
print(f"total words in your text are: {len(separa)}")

# PASO 3
# first and last letter
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"first letter in your text is: {primera_letra}")
print(f"last letter in your text is: {ultima_letra} ")


# PASO 4
# list reverse
separa.reverse()

# unir lista con espacio ME COSTO MUCHO ESTA PARTE, NO DA + declaracion invertida
print("your text in reverse look like this: ")
print(" ".join(separa))

# PASO 5
# boolean de python en texto
# declaracion
control = "python" in texto
print("this word appear in text: 'Python'? ")

# lo mas dificil, un diccionario donde haya strings para cada respuesta
resp = {True: "YES IT APPEARS!", False: "NOT APPEAR!"}

# print del control desde el primer caracter hasta el ultimo y despedida
print(resp[control])
print("THANKS FOR TRY MY FIRST CODE")
