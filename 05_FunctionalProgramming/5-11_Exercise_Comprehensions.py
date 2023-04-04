# Exercise Comprehensions

some_list = ['a', 'b', 'c', 'b', 'x', 'x', 'b', 'm']

# a few lessons ago we found duplicates in some_list using the following

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# now we want to do this using comprehensions

duplicates = list(set([char for char in some_list if some_list.count(
    char) > 1]))

print(duplicates)
