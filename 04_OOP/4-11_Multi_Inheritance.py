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

    def check_arrows(self):
        print(f'{self.name} shoots an arrow. {self.num_arrows} arrows are left.')

    def run(self):
        print('run really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard1 = Wizard('Harry', 20)
archer1 = Archer('Ulises', 29)

hb1 = HybridBorg('Weird', 50, 100)
print(hb1.attack())
