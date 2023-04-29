# reading a file

# f = open('myfile.txt', 'r')

# text = f.read()
# print(text)
# f.close()
# writing a file
# f = open('myfile.txt', 'a')
# f.write('Hello world')
# f.close()
with open('myfile.txt', 'a') as f:
    f.write("Hey i am inside with")
