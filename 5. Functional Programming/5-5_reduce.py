from functools import reduce

my_list = [1, 2, 3]

your_list = [10, 20, 30]

email_list = ['h@gmail', 'u@gmail', 'l@gmail']


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))

# Reduce is a bit hard to explain
# It uses a function, a list and a starting value
# The function must have the initial value as an input and the iterable
# It updates the input value with the returned value

# Let's try it

sentence_list = ['hello', 'my', 'name', 'is', 'Javier', '!']


def write_sentence(word, item):
    return word + ' ' + item


print(reduce(write_sentence, sentence_list, '¡'))
