from PIL import Image, ImageFilter

image = Image.open('.\pokedex\pikachu.jpg')

# print(image)
# print(image.format)
# print(image.size)
# print(image.mode)
# print(dir(image))
# help(image)
# ---------------------
filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('blur.png', 'png')
