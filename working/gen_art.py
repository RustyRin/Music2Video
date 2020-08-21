# from moviepy.editor import *
from PIL import Image, ImageFilter
import sys
import cv2
import numpy as np

import resize_art
import dropShadow
from moviepy.editor import *
#import gausVideoBlur

# applies drop shadow in the same shape as the album art
# should not care what aspect ratio the art is
# saves the composite of the art and shadow into temp as png
# sadly seems like i cant use relative position with a transparent clip
# without losing it or having it butcher the art
# this seems to be a problem with moviepy, not my shit code

# image attached to the variable names is to remind me that these are open in
# PIL and that they are not moviepy clips
def make(debug_mode=False):
    artClip = ImageClip(str(dropShadow.apply('temp/art.png')), transparent=True)
    return artClip




    '''
    # open
    #resize_art.maintain_ratio('temp/art.png', (1000, 1000))

    art_image = Image.open('temp/art.png').convert('RGBA')

    # get size, then calc the aspect ratio
    art_width, art_height = art_image.size

    #dropShadow.make('temp/art.png')
    drop_shadow_image = dropShadow.make('temp/art.png').convert('RGBA')

    #drop_shadow_image = Image.open('drop_square.png').convert('RGBA')

    # open drop shadow and resize it to the dimensions of the art
    drop_shadow_image = drop_shadow_image.resize((int(art_width*dropZoom), int(art_height*dropZoom)), Image.ANTIALIAS)

    # save the resized drop shadow
    drop_shadow_image.save('temp/art_drop_shadow.png', 'PNG')
    drop_shadow_image.close()
    drop_shadow_image = Image.open('temp/art_drop_shadow.png').convert('RGBA')
    drop_width, drop_height = drop_shadow_image.size

    # x > 1 taller
    # x < 1 wider
    # x = 1 square
    art_ratio = art_height / art_width

    # making offset
    offset = (int((drop_width - art_width) / 2), int((drop_height - art_height) / 2))

    # debug prints
    if debug_mode:
        print('Art dimensions: (' + str(art_width) + ', ' + str(art_height) + ')')
        print('Art ratio: ' + str(art_ratio))

    # pastes the art onto the drop shadow, with 10 px offset on both axises(?)
    drop_shadow_image.paste(art_image, offset)

    # saves
    drop_shadow_image.save('temp/art_with_drop.png', 'PNG')

    # closing
    art_image.close()
    drop_shadow_image.close()
    '''
