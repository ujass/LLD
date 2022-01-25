from dog_interface import DogInterface

class CanNotEatError(Exception):
    """This exception is raised when dog can not eat"""
    pass

class DummyDog(DogInterface):

    def __init__(self):
        pass

    def make_noise(self):
        print('dummy dog making noise')

    """
    This is the issue. 
    - dummy dog can not eat, we have to implement it just because we have use the DogInterface. 
    """
    def eat(self):
        raise CanNotEatError