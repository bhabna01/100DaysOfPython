class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")


class cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="dog")
        self.breed = breed

    def make_sound(self):
        print("meow!")


d = dog("Dog", "DOggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()
c = cat("cat", "persian")
c.make_sound()
