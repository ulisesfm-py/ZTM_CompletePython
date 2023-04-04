# range is a generator
'''range(100)
list(range(100))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)'''

# a generator is always an iterable, but an iterable is not always a generator
# range is a generator and it is iterable, but a list is iterable but not a generator

# let's define our own generator


def generator_function(num):
    for i in range(num):
        yield i*2


g = generator_function(100)
next(g)
print(next(g))

# yield pauses the loop, returns the current step result and goes back to looping after seeing next()
# if the input to generator_function is lower than the times I call next() it will return a StopIteration Error
