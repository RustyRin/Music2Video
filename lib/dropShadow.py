from PIL import Image, ImageFilter
import numpy as np
import cv2

# custom functions
# from . import myFunctions # dont need now, but might in the future

'''
NEED TO IMPLEMENT THE OPACITY FUNCTIONALITY
'''

def hexToRGBA(hex, opacity=1):
    hex = hex.strip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def apply(image, blurAmount=25, dropOffset=(5,5), shadowColor=('#000000'), shadowOpacity=1, dropZoom=1.5, returnImage=False):
    if str(type(image)) == '<class \'str\'>':   # was a sting to the file passed, or a PIL image object
        image = Image.open(image)

    # get size
    drop_width, drop_height = image.size
    # calculate the offset to center the art and shadow, apply the desired offset as well
    #offset = (int((((drop_width*1.5) - drop_width) / 2)), int((((drop_height*1.5) - drop_height) / 2)))    # OLD WAY, IF USING ZOOM WORKS, DELETE THIS
    offset = (int((((drop_width*dropZoom) - drop_width) / 2)), int((((drop_height*dropZoom) - drop_height) / 2)))

    # just making sure it has alpha channel
    image = image.convert("RGBA")

    # get raw data
    datas = image.getdata()
    newData = []

    # get the rgb from the color hex given
    red, green, blue = str(hexToRGBA(shadowColor)).strip('()').split(', ')

    # take the raw data, changes the color to the desired color of drop shadow, keeps the transparency
    for item in datas:
        newData.append((int(red), int(green), int(blue), item[3]))

    # make new image for the drop shadow
    dropImage = Image.new(mode="RGBA", size = (drop_width, drop_height))
    dropImage.putdata(newData)

    # make a transparent background, size it bigger than the image (gotta be larger for the blur)
    newImage = Image.new(mode="RGBA", size=((round(drop_width*1.5)), (round(drop_height*1.5))))

    # paste the drop shadow on the with the desired the offset
    newImage.paste(dropImage, (offset[0] + dropOffset[0], offset[1] + dropOffset[1]))

    # apply blur
    newImage = newImage.filter(ImageFilter.GaussianBlur(blurAmount))

    # paste the art on the drop shadow
    newImage.paste(image, offset, image)

    if returnImage:
        return newImage
    else:
        newImage.save('lib/temp/art_with_drop.png', format='PNG')
        # mainly so i can have one like of code in gen_art
        return 'lib/temp/art_with_drop.png'
