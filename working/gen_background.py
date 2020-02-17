# for image manipulation
from PIL import Image, ImageFilter

# for rounding up
import math

# see if the art (/temp/art.png) is dark
import is_dark

# using ImageClip cause it has an easy to use opacity function that keeps the gradient
from moviepy.editor import ImageClip
from moviepy.editor import CompositeVideoClip

# this should intake the art (/temp/art.png), blow it up, blur it, add gradient
# should be able to take in any resolution
# saves as png in

def make(resolution=(3840,2160), blur=0, debug_mode=False,gradient_opacity=1, file_name=''):

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

    art_image.save('temp/' + file_name + '.png', 'PNG')
    art_image.close()

    # determines if the art is dark with is_dark
    if is_dark.calc(debug_mode=debug_mode):
        if debug_mode:
            print('Detected dark art; using white gradient')
        gradient_clip = ImageClip('gradient_white.png', transparent=True).set_opacity(gradient_opacity)
    else:
        if debug_mode:
            print('Detected light art; using black gradient')
        gradient_clip = ImageClip('gradient_black.png', transparent=True).set_opacity(gradient_opacity)

    gradient_clip.resize(resolution)
    art_clip = ImageClip('temp/' + file_name + '.png', transparent=True)
    transparent = ImageClip('transparent.png').resize(resolution)

    background_clip = CompositeVideoClip([transparent, art_clip, gradient_clip])
    background_clip.save_frame('temp/' + file_name + '.png')
