# PASO 1
# input texto user y lowercase para simplificar
texto = input("escribe aqui cualquier parrafo mayor a 30 caracteres: ")
texto = texto.lower()

# input user + conteo de letras + declaraciones de result
a = input("escribe una letra que quieras buscar en el texto: ")
a = a.lower()
result1 = texto.count(a)
print("la cantidad de veces que aparece tu 1ra letra es: ")
print(result1)

b = input("escribe una segunda letra que quieras buscar en el texto: ")
b = b.lower()
result2 = texto.count(b)
print("la cantidad de veces que aparece tu 2da letra es: ")
print(result2)

c = input("escribe la tercera letra que quieras buscar en el texto: ")
c = c.lower()
result3 = texto.count(c)
print("la cantidad de veces que aparece tu 3ra letra es: ")
print(result3)

# PASO 2
# texto a lista en otra variable
separa = list(texto)

# separacion de palabras
separa = texto.split()

# declaracion de total palabras
print("el total de palabras de tu texto es de: ")
print(len(separa))

# PASO 3
# primera y ultima letra
primera_letra = texto[0]
ultima_letra = texto[-1]
print("la primera letra de tu texto es: ")
print(primera_letra)
print("la ultima letra de tu texto es: ")
print(ultima_letra)

# PASO 4
# invertir lista
separa.reverse()

# unir lista con espacio ME COSTO MUCHO ESTA PARTE, NO DA + declaracion invertida
print("Tu texto invertido se veria asi: ")
print(" ".join(separa))

# PASO 5
# boolean de python en texto
# declaracion
control = "python" in texto
print("Aparece la palabra 'Python' en el texto? ")

# lo mas dificil, un diccionario donde haya strings para cada respuesta
resp = {True: "SI APARECE!", False: "NO APARECE!"}

# print del control desde el primer caracter hasta el ultimo y despedida
print(resp[control])
print("GRACIAS POR PROBAR MI PRIMER CODIGO!")
