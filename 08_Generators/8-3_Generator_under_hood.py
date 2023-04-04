def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(type(iterator))
            print(next(iterator)*2)
        except StopIteration:
            break


special_for([1, 2, 3])

# let's create our own range generator


class MyGen():
    # class atribute
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)
