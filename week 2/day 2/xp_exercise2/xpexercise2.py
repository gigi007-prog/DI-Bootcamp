#Exercise 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_cat=Bengal("Ryan",4 )
charteux_cat=Chartreux("Poppy", 1)
siamese_cat=Siamese("Hannah", 8)

all_cats=[bengal_cat,charteux_cat,siamese_cat ]

saras_pets=Pets(all_cats)

saras_pets.walk()

#Exercise 2
class Dog():
    def __init__(self, name, age, weight ):
      self.name=name
      self.age=age
      self.weight=weight
        
