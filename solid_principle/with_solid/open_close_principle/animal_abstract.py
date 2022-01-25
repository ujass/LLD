from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self):
        self.name = None
        self.food = None

    # by default every class has to adhere this method.
    def add_name(self, name: str):
        self.name = name

    # Must implement by the child class.
    @abstractmethod
    def add_food(self, food):
        pass



