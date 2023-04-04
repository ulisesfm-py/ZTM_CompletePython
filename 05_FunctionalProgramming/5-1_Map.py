#map, filter, zip and reduce
def multiply_by2(li):  # This function iterates with item, map() iterates itself too, so does not need this kind of function
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


def multiply_2(item):
    return item*2

# map(multiply_by2, [1, 2 ,3]) #it uses a function(action) and an iterable (data [1,2,3])


print(multiply_by2([1, 2, 3]))

print(list(map(multiply_2, [1, 2, 3])))

# if we create my_list, map() does not modify it
# that is functional's programming philosophy, do not affect external variables

my_list = [1, 2, 3]

print(map(multiply_2, my_list))

print(my_list)  # it stays the same
