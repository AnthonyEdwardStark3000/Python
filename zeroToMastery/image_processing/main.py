from PIL import Image, ImageFilter

pokemon_img = Image.open('image_processing/pokemon_images/pikachu.jpg')
astronaut_img = Image.open('image_processing/pokemon_images/astro.jpg')

print('showing the image selected')

pokemon_img.show()
filtered_image = pokemon_img.filter(ImageFilter.BLUR)
filtered_image.save('blurred_pikachu.png', 'png')
print('showing the blurred image')
filtered_image.show()
# converting it into black and white
converted_image = pokemon_img.convert('L')
converted_image.save('grey_scale.png', 'png')
print('showing the grey version of the selected image')
converted_image.show()

# rotating the image

new_converted_image = converted_image.rotate(180)
print('showing the 180 rotated version of the selected image')
new_converted_image.show()

# resizing
resized_image = pokemon_img.resize((7800, 7800))
resized_image.save('resized_version.png', 'png')
print('showing the resized version of the selected image')
resized_image.show()

# cropping the image
cropped_image = pokemon_img.crop((10, 20, 30, 40))
cropped_image.show()

# compressing the image for thumbnail
print(astronaut_img.size)
astronaut_img.thumbnail((400, 400))
astronaut_img.save('new_thumbnail.jpg')
astronaut_img.show()
print(astronaut_img.size)
