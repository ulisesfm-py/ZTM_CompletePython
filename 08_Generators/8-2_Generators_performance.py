from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} ms.')
        return result
    return wrapper


@performance
def long_time():
    print('1')
    for i in range(100000000):
        i*5


@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i*5


long_time()
long_time2()

# Example of a generator


def gen_fun(num):
    for i in range(num):
        yield i


for item in gen_fun(20):
    print(item)
