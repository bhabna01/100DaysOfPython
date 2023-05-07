class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of the Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


e1 = Employee("ROhan Das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4200)
e2.showLanguage()
