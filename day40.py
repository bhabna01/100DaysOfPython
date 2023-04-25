
import string
import random

letters = string.ascii_lowercase
word = input("Enter a word:")
# Encode
# if (len(word) >= 3):
#     a = (word[1:]+word[0])
#     b = ''
#     c = ''
#     for i in range(3):
#         b = b+random.choice(string.ascii_letters).lower()
#         c = c+random.choice(string.ascii_letters).lower()

#     print(c+a+b)

# else:
#     print(word[::-1])
# decode
if (len(word) < 3):
    print(word[::-1])
else:
    result = word[3:-3]
    a = result[4:]+result[:-1]
    print(a)
