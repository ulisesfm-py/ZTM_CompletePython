# Lambda expressions
# they are used for those ocasions when you have a function that you only want to use once
# they are anonymous functions, no need for a name

from functools import reduce
my_list = [1, 2, 3]

#lambda param: action(param)

# Let's imagine I don't want to save this functions in memory, and only use them once


# def multiply_2(item):
#    return item*2


# def only_odd(item):
#    return item % 2 != 0


# def accumulator(acc, item):
#    print(acc, item)
#    return acc + item


print(list(map(lambda item: item*2, my_list)))
# here we create a lambda function that receives an iterable (my_list) an applies an action into every item

# we can do the same for only_odd and filter
print(list(filter(lambda item: item % 2 != 0, my_list)))

# now let's try reduce an accumulator and reduce
print(reduce(lambda acc, item: acc + item, my_list, 4))
