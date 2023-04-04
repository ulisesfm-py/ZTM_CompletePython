# the proper way to work with files, which does not need the .close() is the following

with open('test.txt', mode='r') as my_file:
    print(my_file.readlines())

# the mode 'r' means read, and is by default
# if we want to write we will say mode 'w'
# and if we want to read and write then mode 'r+'

with open('test.txt', mode='r+') as my_file:
    text = my_file.write('hey it\'s me')
    print(text)
    print(my_file.readlines())

# if we want to write at the end of the file we can use append mode 'a'
with open('test.txt', mode='a') as my_file:
    text = my_file.write(':)')
    print(text)

# now let's write a new non existent file
with open('newfile.txt', mode='w') as my_file:
    text = my_file.write(':(')
    print(text)
