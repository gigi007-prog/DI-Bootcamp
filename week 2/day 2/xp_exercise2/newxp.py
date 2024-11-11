#Exercise 3
import random
from xpexercise2 import Dog

class PetDog(Dog):
    def __init__(self,name, age, weight, trained=False):
        self.trained=trained 
        super().__init__(name, age, weight)
    def train(self):
        print(self.bark())  
        self.trained = True  
        print(f'{self.name} is now trained!')
    def play(self, *args):
        dog_names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(dog_names)} all play together")
    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."]
            trick = random.choice(tricks)
            print(trick)
        else:
            print(f"{self.name} is not trained yet and can't do a trick.")
            


