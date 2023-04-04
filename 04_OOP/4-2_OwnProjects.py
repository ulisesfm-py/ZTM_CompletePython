# OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age  # attributes

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Ulises', 29)
player2 = PlayerCharacter('Cristina', 27)

print(player1.age)
print(player1.name)

print(player2.name)

print(player1.run())
