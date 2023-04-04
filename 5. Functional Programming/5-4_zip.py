# Zip()

my_list = [1, 2, 3]

your_list = [10, 20, 30]

email_list = ['h@gmail', 'u@gmail', 'l@gmail']


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


print(list(zip(my_list, your_list, email_list)))

# The zip() function zips the two iterables together
# In this case it zips two lists together, but i can zip a list with a tuple
# list(zip(iterable1, iterable 2)) creates a list of tuples

print(my_list)
