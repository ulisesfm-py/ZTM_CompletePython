# in this exercise we want to be able to write in the terminal the following
# python nameofscript.py OldFolder/ NewFolder/

import sys
import os
from PIL import Image

# grab first and second argument
old = sys.argv[1]
old_path = '../image-playground/' + old
new = sys.argv[2]
new_path = '../JPG-PNG-converter/' + new

print(f'old folder: {old}, new folder: {new}.')
print(old_path)
print(new_path)

# check if OldFolder/ exists

if os.path.exists(old_path):
    print(f'the folder {old} exists')
else:
    print('The old folder does not exist')

# check if NewFolder/ exists, if not create

if os.path.exists(new_path):
    print(f'the folder {new} exists')
else:
    os.makedirs(new_path)
    print('New folder created successfully')


# loop through OldFolder/
for filename in os.listdir(old_path):
    if filename.endswith('.jpg'):
        # open the image using PIL
        image = Image.open(os.path.join(old_path, filename))

        # convert images to png and save to the new folder
        new_filename = os.path.splitext(filename)[0] + '.png'
        image.save(os.path.join(new_path, new_filename), 'png')

        print(f'{filename} converted to {new_filename} in folder {new_path}')
