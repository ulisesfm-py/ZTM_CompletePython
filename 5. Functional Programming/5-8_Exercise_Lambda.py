# square the following list using lambda expressions
my_list = [5, 4, 3]

print(list(map(lambda item: item**2, my_list)))

# list sorting
# sort this list of tuples based on the second number of each tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a1, a2 = list(zip(*a))
print(a1)
print(a2)

a = sorted(list(zip(a2, a1)))
print(a)

# now do the same using lambda expressions
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
#a.sort(key=lambda x: x[1])
print(sorted(a, key=lambda x: x[1]))
