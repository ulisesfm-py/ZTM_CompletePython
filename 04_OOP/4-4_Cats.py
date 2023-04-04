# Given the below class:
class Cat:
    species = 'mammal'  # class object attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats


Cat1 = Cat('Miau', 4)
Cat2 = Cat('Meow', 8)
Cat3 = Cat('Jack', 1)

# 2 Create a function that finds the oldest cat

Cat_list = [Cat1, Cat2, Cat3]
print(type(Cat_list))


def find_oldest_cat(Cats):
    oldest_age = 0
    for i in range(len(Cats)):
        if Cats[i].age > oldest_age:
            oldest_age = Cats[i].age
            oldest_cat = Cats[i].name
    return oldest_cat, oldest_age

# 3 Print out: 'the oldest cat is x years old'


oldest_cat_name, oldest_cat_age = find_oldest_cat(Cat_list)
print(
    f'The oldest cat is {oldest_cat_age} years old. Its name is {oldest_cat_name}.')
