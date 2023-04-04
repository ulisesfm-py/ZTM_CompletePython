from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print(img)
print(img.format)  # JPG
print(img.size)  # 640x640
print(img.mode)  # RGB

# print(dir(img))

# We can also use .SHARPEN or .SMOOTH
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')

# We can also convert to different formats
converted_img = img.convert('L')
converted_img.save('grey.png', 'png')

filtered_img.show()
crooked = converted_img.rotate(90)
crooked.show()

# We can also resize (accepts tuple as input of dimensions)
resize = crooked.resize((300, 300))
resize.save('resized.png', 'png')

# How can we crop? giving the position of the corner pixels
box = (100, 100, 400, 400)
cropped = filtered_img.crop(box)
cropped.save('cropped.png', 'png')
