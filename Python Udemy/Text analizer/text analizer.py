# step 1
# input user text and lowercase
txt = input("Write here any text with 30 characters or more: ")
txt = txt.lower()

# input user + letter counting + print appears
a = input("write a letter you want to search in text: ")
a = a.lower()
ans1 = txt.count(a)
print(f"your letter appears: {ans1} times")

b = input("write a second letter you want to search: ")
b = b.lower()
ans2 = txt.count(b)
print(f"your second letter appears: {ans2} times")

c = input("write a third letter you want to search: ")
c = c.lower()
ans3 = txt.count(c)
print(f"your third letter appears: {ans3} times")

# step 2
# text to list
spl = list(txt)

# word split
spl = txt.split()

# total words in text
print(f"total words in your text are: {len(spl)}")

# PASO 3
# first and last letter
first_l = txt[0]
last_l = txt[-1:]
print(f"first character in your text is: {first_l}")
print(f"last character in your text is: {last_l} ")


# step 4
# list reverse
spl.reverse()

# unir lista con espacio ME COSTO MUCHO ESTA PARTE, NO DA + declaracion invertida
print("your text in reverse look like this: ")
print(" ".join(spl))

# step 5
# boolean in text
# declaration
control = "python" in txt
print("this word appear in text: 'Python'? ")

# dictionary to print in both cases
ans4 = {True: "YES IT APPEARS!", False: "NOT APPEAR!"}

# print control from last to first character
print(ans4[control])
print("THANKS FOR TRY MY FIRST CODE")