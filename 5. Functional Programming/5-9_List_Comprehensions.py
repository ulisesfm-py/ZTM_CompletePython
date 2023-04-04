# list comprehensions

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# this is a way to loop and append each letter in 'hello' to my_list
# there is a faster and cleaner way using list comprehensions in Python

#my_list = [parameter for parameter in iterable]
my_list = [char for char in 'hello']

print(my_list)

my_list2 = [num for num in range(0, 100)]

print(my_list2)

# now the same but multiplied by 2

my_list3 = [num*2 for num in range(0, 100)]
print(my_list3)

# now in my_list i want to square nums and only keep the even numbers

my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list4)
