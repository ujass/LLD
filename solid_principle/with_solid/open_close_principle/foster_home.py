from animal_abstract import Animal
from bird_interface import Bird
from mummal_interface import Mammal

class FosterHome:
    """
    Now, Foster home do not need to add individual animal anymore.
    They have created one 'add_animal' method which can add any type of animal.

    Now, we just need to add another service in foster home.
    """

    def __init__(self):
        self.animals = []

    def add_animal(self, animals: [Animal]):
        for animal in animals:
            self.animals.append(animal)
            print(f'Animal {animal.name} added in foster home')

    # service - 1
    def feed_animal(self):
        for animal in self.animals:
            print(f'Animal {animal.name} is being fed {animal.food}')


