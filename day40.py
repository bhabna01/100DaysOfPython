
import string
import random

letters = string.ascii_lowercase

# Encode


def encoding(w):
    if (len(w) >= 3):
        a = (w[1:]+word[0])
        b = ''
        c = ''
        for i in range(3):
            b = b+random.choice(string.ascii_letters).lower()
            c = c+random.choice(string.ascii_letters).lower()

        print(c+a+b)

    else:
        print(w[::-1])
# decode


def decoding(w):
    if (len(w) < 3):
        print(w[::-1])
    else:
        result = w[3:-3]
        a = result[4:]+result[:-1]
        print(a)


word = input("Enter a word:")
option = int(input("Enter option 1.encoding 2.Decoding"))
if (option == 1):
    encoding(word)
elif (option == 2):
    decoding(word)
else:
    print("Enter 1 or 2")
