import random


def game(comp, user):
    if (user == comp):
        return 0
    elif ((user == 0) and (comp == 1)):
        return 1
    elif ((user == 1) and (comp == 2)):
        return 1
    elif ((user == 2) and (comp == 0)):
        return 1
    else:
        return -1


computer = random.randint(0, 2)
user = int(input("0 for Snake,1 for water and 2 for gun:"))
print("The input for the computer", computer)
value = game(computer, user)
if (value == 0):
    print("Draw")
elif (value == 1):
    print("Win")
else:
    print("lose")
