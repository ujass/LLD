from dog_interface import DogInterface

class DummyDogInterface(DogInterface):

    def __init__(self):
        pass

    def make_noise(self):
        print('Dummy dog is making the noise')

