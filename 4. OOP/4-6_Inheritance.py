# Inheritance (3rd Pillar of OOP)

class User():
    def sign_in(self):
        print('you are logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} attacks with a power of {self.power}')


wizard1 = Wizard('Harry', 20)
print(isinstance(wizard1, User))  # Is wizard 1 an object of class User?

# and here is the interesting part, everything is object
print(isinstance(wizard1, object))  # it is true
