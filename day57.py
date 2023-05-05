class Person:
    name = "Harry"
    occupation = "software Developer"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
a.name = "Shubhab"
a.occupation = "Accountant"
print(a.name)
b.name = "Nitika"
b.occupation = "HR"
a.info()
b.info()
