''' Count Vowels in a String

In Python, you can create a function that counts the number of vowels
in a given word. Vowels are the letters A, E, I, O, and U, both uppercase and lowercase.
The function takes a single word as its parameter and returns the number
 of vowels present in the word.

To achieve this, you can use a for loop to iterate through each character in the word.
Then, you can check if the character is a vowel using a conditional statement.
If the character is a vowel, you increment a counter variable. Finally,
you return the counter variable as the result.'''

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


