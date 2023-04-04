# what if this script and the txt file are in different folders?
# we created a newfile in a folder called app

with open('app/newfile.txt', mode='r') as my_file:
    text = my_file.readlines()
    print(text)
