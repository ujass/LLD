from animal_abstract import Animal

class Bird(Animal):

    def __init__(self):
        super(Bird, self).__init__()
        self.type = 'bird'
