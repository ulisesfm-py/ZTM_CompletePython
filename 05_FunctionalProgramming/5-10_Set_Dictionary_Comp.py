# Set and Dictionary Comprehensions
# for Set comprehensions, we can do the same as for lists, but changing [] for {}
# sets only allow unique items, no duplicates

my_set = {char for char in 'Hello'}
print(my_set)
my_set2 = {num for num in range(0, 100, 5) if num < 50 or num > 75}
print(my_set2)

# what about dictionaries
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}
print(my_dict)

my_dict2 = {k: k*2 for k in [1, 2, 3]}
print(my_dict2)
