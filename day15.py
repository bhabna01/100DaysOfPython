import time

timestamp = int(time.strftime('%H'))
if (timestamp > 5 and timestamp < 12):
    print("good morning")
elif (timestamp > 12 and timestamp < 17):
    print("good afternoon")
elif (timestamp > 17 and timestamp < 20):
    print("good evening")
else:
    print("good night")
