
if __name__ == '__main__':
    from dummy_dog import DummyDog
    from real_dog import RealDog

    real_dog = RealDog()
    real_dog.eat()
    real_dog.make_noise()

    # Now, as we have separate interface for each (dummy, real) dog.
    # dummy & real dog interface can replace the actual dog.  (This can be very clear in java with strict datatype)
    dummy_dog = DummyDog()
    dummy_dog.make_noise()