from animal_abstract import Animal
from bird_interface import Bird

class Duck(Animal):

    def __init__(self):
        super(Duck, self).__init__()
        self.food = None

    def add_food(self, food: str):
        self.food = food

