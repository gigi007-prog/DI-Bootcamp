#Exercise 1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# bengal_cat=Bengal("Ryan",4 )
# charteux_cat=Chartreux("Poppy", 1)
# siamese_cat=Siamese("Hannah", 8)

# all_cats=[bengal_cat,charteux_cat,siamese_cat ]

# saras_pets=Pets(all_cats)

# saras_pets.walk()

#Exercise 2
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f'{self.name} is barking'
    def run(self):
        return (self.weight / self.age) * 10
    def fight(self, other_dog):
        self_power = self.run() * self.weight 
        other_dog_power = other_dog.run() * other_dog.weight  
        
        if self_power > other_dog_power:
            return f"{self.name} wins the fight!"
        elif self_power < other_dog_power:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie"


dog1 = Dog("Shmulik", 5, 40)
dog2 = Dog("Nes", 8, 20)
dog3 = Dog("Winston", 2, 7)

#barking
print(dog1.bark())  
#running
print(f"Shmulik's running speed: {dog1.run()}")  

print(dog2.bark())  
print(f"Nes's running speed: {dog2.run()}")  

print(dog3.bark()) 
print(f"Winston's running speed: {dog3.run()}") 

print(dog1.fight(dog2))  
print(dog2.fight(dog3))  
print(dog1.fight(dog3))  

#Exercise 4
class Family:
    def __init__(self, last_name, members=None):
        if members is None:
            members = []
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f"Congratulations! The {self.last_name} family just welcomed a new member, {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False  

    def family_presentation(self):
        print(f"Welcome to the {self.last_name} family!")
        for member in self.members:
            print(f"{member['name']} ({member['gender']}, {member['age']} years old, Child: {member['is_child']})")


the_dahmer_family = Family("Dahmer", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

the_dahmer_family.family_presentation()

the_dahmer_family.born(name="Jeffrey", age=17, gender="Male")

print(f"Is Michael 18 or older? {the_dahmer_family.is_18('Michael')}")
print(f"Is Sarah 18 or older? {the_dahmer_family.is_18('Sarah')}")
print(f"Is Jeffrey 18 or older? {the_dahmer_family.is_18('Jeffrey')}")

#Exercise 5
class TheIncredibles(Family):
    def __init__(self, last_name, members=None):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']} uses their power: {member['power']}!")
                    return
                else:
                    raise ValueError(f"{member['name']} is not over 18 years old and cannot use their power.")
        print(f"{name} is not a member of the family.")

    def incredible_presentation(self):
        print(f"*Here is our powerful family*")
        print(f"The {self.last_name} family:")
        super().family_presentation()
        for member in self.members:
            print(f"Incredible name: {member['incredible_name']}, Power: {member['power']}")


the_incredibles_and_dahmers = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

the_incredibles_and_dahmers.incredible_presentation()
the_incredibles_and_dahmers.born(name="Baby Jeffrey Dahmer", age=1, gender="Male", power="Unknown Power", incredible_name="BabyJeffrey")
the_incredibles_and_dahmers.incredible_presentation()

the_incredibles_and_dahmers.use_power('Michael')  
try:
    the_incredibles_and_dahmers.use_power('Baby Jeffrey Dahmer') 
except ValueError as e:
    print(e)
