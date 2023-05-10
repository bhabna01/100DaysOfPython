import os
files = os.listdir("gerbage")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"gerbage/{file}", f"gerbage/{i}.png")
        i = i+1
