class Employee:
    companyName = "Apple"
    noOfEmployee = 0

    def __init__(self, name):
        self.name = name
        self.raise_Amount = 0.02
        Employee.noOfEmployee += 1

    def showDetails(self):
        print(
            f"The name of the Employee is {self.name} and the company name {self.companyName} the raise amount is {self.raise_Amount}")


ep1 = Employee("Harry")
ep1.raise_Amount = 0.3
ep1.companyName = "Apple India"
ep1.showDetails()
ep2 = Employee("Bhabna")

ep2.showDetails()
print(Employee.companyName)
print(Employee.noOfEmployee)
