
class Trainer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # name = property(get_name, set_name)

    def get_age(self):
        return self.age

    def set_age(self, age):
        # Can put some validation to set the age.
        self.age = age

    # Remember never set the values of getter & setter in init otherwise,
    # recursion depth reach error will raise.
    # to, know more, uncomment below property and run this module.
    # age = property(get_age, set_age)



