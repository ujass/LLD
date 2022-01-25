from dog_interface import DogInterface


class RealDog(DogInterface):

    def __init__(self):
        pass

    def make_noise(self):
        print('real dog is barking')

    def eat(self):
        print('real dog is eating...')

