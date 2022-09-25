from PIL import Image, ImageFilter

pokemon_img = Image.open('image_processing/pokemon_images/pikachu.jpg')
print(dir(pokemon_img))
filtered_image = pokemon_img.filter(ImageFilter.BLUR)
filtered_image.save('blurred_pikachu.png', 'png')
