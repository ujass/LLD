from dog import Dog
from cat import Cat

class FosterHome:

    def add_dog(self, dog : Dog):
        print(f"{dog.name} Dog added in foster home")

    def add_cat(self, cat: Cat):
        print(f"{cat.name} Cat added in foster home")

    """
    Issue : Every time any new animal is accepting by the foster home. we have to create it's method for that.
            I am not breaking the existing functionality, but it is adding redundant code.
            
    Solution: Use Interface & abstraction for that.
    """