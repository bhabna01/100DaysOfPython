class Employee:
    def __init__(self):
        self.__name = "Harry"


a = Employee()
# print(a.__name)cannot be accessed directly
# name mangling
print(a._Employee__name)
