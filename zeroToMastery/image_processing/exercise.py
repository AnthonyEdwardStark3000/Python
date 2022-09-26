from email.mime import image
import sys
import os
from PIL import Image

###
# grab first, second cla
# check for new folder if not create a folder named new
# loop through pokemon_images
# convert the images in there to png
# save the images to the new folder created
#  ###

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    image = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    image.save(f'{output_folder}{clean_name}.png', 'png')
    print('done')
