#map, filter, zip and reduce

my_list = [1, 2, 3]


def multiply_2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
