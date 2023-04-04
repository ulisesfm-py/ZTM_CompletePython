# let's continue with more image processing with Python

from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
print(img.size)
new_img = img.resize((400, 200))
new_img.save('new_img.jpg')

# by doing this, we lose the aspect ratio of the image
img.thumbnail((400, 200))
# we don't assign the output of .thumbnail to a variable, because it does not return anything, it modifies img
img.save('thumbnail.jpg')
