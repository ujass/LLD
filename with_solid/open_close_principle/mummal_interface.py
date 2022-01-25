from animal_abstract import Animal

class Mammal(Animal):

    def __init__(self):
        super(Mammal, self).__init__()
        self.type = 'mammal'    # can be enum or constant as well.