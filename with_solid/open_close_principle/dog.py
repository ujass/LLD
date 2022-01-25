from animal_abstract import Animal
from mummal_interface import Mammal

class Dog(Animal):

    def __init__(self):
        super(Dog, self).__init__()
        self.food = None

    def add_food(self, food: str):
        self.food = food