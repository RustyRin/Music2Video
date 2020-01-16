# for image manipulation
from PIL import Image, ImageFilter

# for rounding up
import math

# see if the art (/temp/art.png) is dark
import is_dark

# this should intake the art (/temp/art.png), blow it up, blur it, add gradient
# should be able to take in any resolution
# saves as png in

def make(resolution=(3840,2160), blur=0, debug_mode=False, file_name=''):

    # opens art, then adds blur, then blows up
    art_image = Image.open('temp/art.png')
    art_image = art_image.filter(ImageFilter.GaussianBlur(radius=blur))
    if(resolution > art_image.size):
        if debug_mode:
            print('Art smaller than background needed')
        art_image = art_image.resize((math.ceil(resolution[0] * 1.05), math.ceil(resolution[0] * 1.05)), Image.ANTIALIAS)
    else:
        if debug_mode:
            print('Art larger than background needed')
    if debug_mode:
        print('Background size before crop: ' + str(art_image.size))

    # cropping the blurred art
    width, height = art_image.size

    left = (width - resolution[0])/2
    top  = (height - resolution[1])/2
    right = (width + resolution[0])/2
    bottom = (height + resolution[1])/2

    # crop
    art_image = art_image.crop((left, top, right, bottom))

    # determines if the art is dark with is_dark
    if is_dark.calc(debug_mode=debug_mode):
        if debug_mode:
            print('Detected dark art; using white gradient')
        gradient_image = Image.open('gradient_white.png')
    else:
        if debug_mode:
            print('Detected light art; using black gradient')
        gradient_image = Image.open('gradient_black.png')

    # resize gradient
    gradient_image = gradient_image.resize(resolution)

    # put the
    art_image.paste(gradient_image, (0,0), gradient_image)
    art_image = art_image.resize(resolution)
    art_image.save('temp/' + file_name + '.png', 'PNG')

    # closing
    art_image.close()
    gradient_image.close()
