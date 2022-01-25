

if __name__ == '__main__':

    from realdog import RealDog
    from dummydog import DummyDog

    realdog = RealDog()
    realdog.eat()
    realdog.make_noise()

    dumydog = DummyDog()
    dumydog.eat()       # dummy dog can not eat
    dumydog.make_noise()


    """
    Issue : 
        - dummy dog can not eat, still we have to implement it's method as we had only one interface.
        
    Solution: 
        - liskov substitution principle
        - child class should be replaceable by the parent class. 
    """