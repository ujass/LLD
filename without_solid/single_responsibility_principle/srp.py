

class Trainer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Feature - 1
    def send_schedual(self):
        print("sending schedule")

    # Feature - 2
    def diet_sender(self):
        print("sending diet plan")

    # Feature - 3
    def reward_calculator(self):
        print("Your reward is being calculated")

    # str is called when we print the object
    def __str__(self):
        return f'your trainer is {self.name} and he is {self.age} years old'

    # repr called when pass object in another data structure.
    # Ex object_list = [obj1, obj2] and when we print object_list
    # then, we see repr representation of object in the list.
    def __repr__(self):
        return f'{self.name}'


"""
What is the issue in this class?
    1. Trainer class is doing everything from creating the object to the serving the service. 
    2. what if in future more service we want to add ?
    3. what if other different types of trainers also using the same service? 
        - do we copy paste the all service of the trainer? 
"""




