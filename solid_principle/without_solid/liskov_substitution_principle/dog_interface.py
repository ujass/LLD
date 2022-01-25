from abc import ABC, abstractmethod


class DogInterface(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass
