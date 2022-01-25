




if __name__ == '__main__':

    from cat import Cat
    from dog import Dog
    from foster_home import FosterHome

    foster_home = FosterHome()
    dog = Dog()
    dog.add_name('puppy')
    cat = Cat()
    cat.add_name('catty')

    foster_home.add_dog(dog)
    foster_home.add_cat(cat)

    """
    What if Foster Home is becoming popular and want to accommodate more animals into it. 
    """

