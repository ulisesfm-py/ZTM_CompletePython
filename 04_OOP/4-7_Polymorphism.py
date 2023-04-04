# Polymorphism (4th Pillar of OOP)

class User():
    def sign_in(self):
        print('you are logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} attacks with a power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'{self.name} shoots an arrow. {self.num_arrows} arrows are left.')


wizard1 = Wizard('Harry', 20)
archer1 = Archer('Ulises', 29)

# attack does not mean the same for wizard and for archer.

for char in [wizard1, archer1]:
    char.attack()
