from abc import ABC, abstractmethod

class DogInterface(ABC):

    @abstractmethod
    def make_noise(self):
        pass

