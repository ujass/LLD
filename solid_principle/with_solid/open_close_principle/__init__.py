


if __name__ == '__main__':
    from dog import Dog
    from duck import Duck
    from foster_home import FosterHome

    foster_home = FosterHome()

    duck = Duck()
    duck.add_name('dukky')
    duck.add_food('flour')

    dog = Dog()
    dog.add_name('doggy')
    dog.add_food('bones')

    # add any amimals
    foster_home.add_animal([dog, duck])

    # use service
    foster_home.feed_animal()

