class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"The name is {self.name}"


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        return f"The name is {self.name}"


class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name


o = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
print(o.show())
print(DancerEmployee.mro())
