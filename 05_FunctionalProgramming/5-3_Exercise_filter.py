#Filter names with letter A

users = ['Andrew', 'Ulises', 'Javier', 'David', 'Quero', 'Yakata', 'Oliver']

def only_a(item):
    return 'a' in item

print(list(filter(only_a, users)))