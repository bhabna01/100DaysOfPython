import random
comp = random.randint(0, 2)
user = int(input("0 for Snake,1 for water and 2 for gun:"))
print(comp)
if (user == comp):
    print("draw")
elif ((user == 0) and (comp == 1)):
    print("Win")
elif ((user == 1) and (comp == 2)):
    print("Win")
elif ((user == 2) and (comp == 0)):
    print("Win")
elif ((user == 1) and (comp == 0)):
    print("Loss")
elif ((user == 0) and (comp == 2)):
    print("Lose")
elif ((user == 2) and (comp == 1)):
    print("Lose")
