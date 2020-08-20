from PIL import Image, ImageFilter
import numpy as np
import cv2

def hexToRGBA(hex, opacity):
    hex = hex.strip('#')
    newRBG = tuple(int(hex[i:i + len(hex) // 3], 16) for i in range(0, len(hex), len(hex) // 3))
    return (str(newRBG)[:-1] + ', ' + opacity + ')')

def make(image, blurAmount=25, dropOffset=(5,5), shadowColor=(000000), shadowOpacity=1):
    # Did they give a file path or a PIL image object?
   # if isinstance(image, str):
    #    image = Image.open(image)
    # Assmuing they are either giving a file name/ path or a pil image object
    if str(type(image)) == '<class \'str\'>':   # just making sure if i pass an image object
        image = Image.open(image)

    drop_width, drop_height = image.size
    offset = (int((((drop_width*1.5) - drop_width) / 2) + dropOffset[0]), int((((drop_height*1.5) - drop_height) / 2)+dropOffset[1]))

    image = image.convert("RGBA")
    datas = image.getdata()
    newData = []

    for item in datas:
        newData.append((0, 0, 0, item[3]))

    image.putdata(newData)

    newImage = Image.new(mode="RGBA", size=((round(drop_width*1.5)), (round(drop_height*1.5))))
    newImage.paste(image, (offset))

    newImage.save("temp/halp", "PNG")   # for legacy use

    return newImage.filter(ImageFilter.GaussianBlur(blurAmount))

#dropShadow('cat.png')
