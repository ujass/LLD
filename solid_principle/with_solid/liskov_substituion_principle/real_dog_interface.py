from dog_interface import DogInterface
from abc import abstractmethod

class RealDogInterface(DogInterface):

    def make_noise(self):
        print('Real dog is making noise')

    @abstractmethod
    def eat(self):
        pass

