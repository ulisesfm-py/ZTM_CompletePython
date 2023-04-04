class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        return print(f'attacking with a power of {self.power}.')


Wizard1 = Wizard('Ulises', 100, 'Uli@gmail.com')

print(Wizard1.email)
print(Wizard1.attack())
print(Wizard1.sign_in())
print(Wizard1.name)
print(Wizard1.power)
