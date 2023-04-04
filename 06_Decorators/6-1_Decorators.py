# Decorators

# functions can be used as parameters of another function
# we could do something like this

def greet():
    print('hello')


def sayHello(func):
    func()


print(sayHello(greet))  # this works, because greet can be a parameter of sayHello

# a High Order Function is one that accepts or returns a function


def greet2():
    def func():
        return 5
    return func

# this one returns an internal function, pretty useless but works as an example

# let's write our own decorator
# a decorator is a function that wraps another function, and it enhances it


def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('*******')
    return wrap_func


@my_decorator
def hello():
    print('heeeelloooo')


@my_decorator
def bye():
    print('see ya later')


hello()
bye()

# personally, it is weird to me that hello and bye functions are modified permanently by my_decorator


# why have we created a decorator? isn't it useless? it hasn't changed anything
# however, it allows us to add new functionality
# let's edit the my_decorator to provide new functionality
# what if we want to add variables into hello and bye functions?

# this is the Decorator Pattern
def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('*******')
    return wrap_func


@my_decorator2
def hello2(word, emoji, age):
    print(word, emoji, age)


hello2('hi dude ', ':(', 34)
