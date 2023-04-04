import random
from collections import Counter, defaultdict, OrderedDict
import datetime
from time import time
from array import array

# random
print(random.randint(1, 100))

print(random.choice(range(100)))

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# collections
# Counter
li = [1, 2, 3, 3, 4, 3, 1, 5]
sentence = 'blah blah blah thinking about Python'
print(Counter(li))
print(Counter(sentence))
# defaultdict
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['c'])
# OrderedDict
# from python 3.7 ALL dictionaries are ordered by default

# datetime
print(datetime.time(5, 45, 2))
print(datetime.date.today())

# time


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
    for i in range(100000000):
        i*5


# array
arr = array('i', [1, 2, 3])

# arrays have better performance than lists, but you can access them like lists
# we defined the type of data 'i' int.
print(arr[0])
