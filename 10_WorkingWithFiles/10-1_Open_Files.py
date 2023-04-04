my_file = open('test.txt')

'''print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)'''
print(my_file.readline())  # reads first line
print(my_file.readline())  # reads second line
print(my_file.readline())  # reads third line

# I need to use .seek(0) to set the cursor to the beginning again
my_file.seek(0)

# to read all lines you can also do
print(my_file.readlines())  # reads all lines

# we need to close the file we were reading at the end
my_file.close()
