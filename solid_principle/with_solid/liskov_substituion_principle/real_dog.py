from real_dog_interface import RealDogInterface

class RealDog(RealDogInterface):

    def __init__(self):
        super(RealDog, self).__init__()

    def eat(self):
        print('Real dog is eating')

