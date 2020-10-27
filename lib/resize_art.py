from PIL import Image

'''
Should be updated to have the ability
to also take in a PIL object
'''

def maintain_ratio (image_name, desired_size):

    # opening image
    image_input = Image.open(image_name).convert('RGBA')

    # getting old size
    old_width = image_input.size[0]
    old_height = image_input.size[1]

    # getting new size. doing this because it is more readable
    new_width, new_height = desired_size

    new_width = int(new_width * (old_height / old_width))
    new_height = int(new_height * (old_width / old_height))

    image_input = image_input.resize((new_width, new_height), Image.ANTIALIAS)
    image_input.save(image_name, "PNG")
