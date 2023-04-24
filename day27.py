question = ["What is the national flower of Bangladesh?",
            "What is the national animal of bangladesh?", "what is the national fruit of bangladesh"]
ans1 = ["Waterliliy", "jesmine", "rose", "pitunia"]
ans2 = ["tiger", "lion", "dog", "Chicken"]
ans3 = ["jackfruit", "mango", "apple", "banana"]
sum = 0

print(question[0])
for i in ans1:
    print(i)
correctAnswer1 = input("Enter your answer:")
if correctAnswer1 == "Waterliliy":
    print("you are correct")
    sum = sum+1000
else:
    print("you are incorrect")
    sum = sum+0


print(question[1])
for i in ans2:
    print(i)
correctAnswer2 = input("Enter your answer:")
if correctAnswer2 == "tiger":
    print("you are correct")
    sum = sum+1000
else:
    print("you are incorrect")
    sum = sum+0

print(question[2])
for i in ans3:
    print(i)
correctAnswer3 = input("Enter your answer:")
if correctAnswer3 == "jackfruit":
    print("you are correct")
    sum = sum+1000
else:
    print("you are incorrect")
    sum = sum+0
print("You won ", sum)
