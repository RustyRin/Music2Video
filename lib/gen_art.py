from moviepy.editor import *
from PIL import Image, ImageFilter
import sys
import cv2
import numpy as np

from . import dropShadow

# need to add in funtionality to set art location
def make(
    debug_mode=False, 
    artLocation=None, 
    drop_shadow_blur=25,
    drop_shadow_offset=(5,5),
    drop_shadow_color=('#000000'),
    drop_shadow_opacity=1,
    drop_shadow_zoom=1.5):

    if artLocation == None:     # no location for the art is given, assuming in temp
        artLocation = 'lib/temp/art.png'

    artClip = ImageClip(str(dropShadow.apply(
        image=artLocation,           # passing droip shadow vars
        blurAmount=drop_shadow_blur,
        dropOffset=drop_shadow_offset,
        shadowColor=drop_shadow_color,
        shadowOpacity=drop_shadow_opacity,
        dropZoom=drop_shadow_zoom)), transparent=True)
    return artClip
