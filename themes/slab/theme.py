from typing import Text
from numpy.core.fromnumeric import clip

from numpy.lib.function_base import angle
from themes.radio import gen_background
from moviepy.editor import *

# object that hold all the song info
from lib import song

# makes the text clips
from lib import gen_text

# takes in the art and adds a drop shadow
from lib import gen_art

# removes illegal or problematic chars for uploading
from lib import string_clean

# if there are any custom things from the slab theme folder, they go here
# import xyz

# my functions
from lib import myFunctions

# makes thumbnails
# this theme needs to make its own thumbnails in the same style of the theme
from lib import gen_thumb

'''
This theme is assuming that the art
is at a perfect 1:1 ratio
so if youre giving it a tall or wide art, it might
look off

Use the radio theme as it is the most accepting
of weird things
'''

def make(songObject=None, resolution=(3840, 2160), debug_mode=False):

    # slab options
    slab_color = '#9b42f5'
    slab_rotate = 75

    # text options
    text_clip_artist_font_size = 100
    text_clip_artist_font_color = '#c20010'
    text_clip_title_font_size = 250
    text_clip_title_font_color = slab_color

    # art / drop shadow options
    # messing with some of the drop shadow setting
    # will mess with the placment of the art
    drop_shadow_blur = 33
    drop_shadow_offset = (0,0)
    drop_shadow_color = ('#000000')
    drop_shadow_opacity = 0.5
    drop_shadow_zoom = 1.30

    # the color clip needs rgb and not hex, so convert
    slab_color = myFunctions.hex_to_rgb(slab_color)
    slab_color_background = myFunctions.hex_to_rgb('#FFFFFF')

    # make the art with a drop shadow, then move it
    clip_art = gen_art.make(
        debug_mode=debug_mode,
        artLocation='lib/temp/art.png',
        drop_shadow_blur=drop_shadow_blur,
        drop_shadow_offset=drop_shadow_offset,
        drop_shadow_color=drop_shadow_color,
        drop_shadow_opacity=drop_shadow_opacity,
        drop_shadow_zoom=drop_shadow_zoom)
    clip_art = clip_art.set_position((-0.05, -0.04), relative=True)
    clip_art = clip_art.resize(width=resolution[0]*.70)

    # make the color slap, and then rotate it, then move it
    clip_color_slab = ColorClip(
        size=resolution,
        color=slab_color)
    clip_color_slab = clip_color_slab.add_mask().rotate(slab_rotate)
    clip_color_slab = clip_color_slab.set_position((-0.25, 'center'), relative=True)

    # making the bg white with a white color slab
    clip_color_background = ColorClip(
        size=resolution,
        color=slab_color_background)
    
    # artist text clip
    clip_artist = gen_text.artist(
        text=songObject.trackArtist, 
        color=text_clip_artist_font_color, 
        font_size=text_clip_artist_font_size, 
        resolution=resolution, 
        debug_mode=debug_mode)
    clip_artist = clip_artist.set_position((0.52, 0.07), relative=True)

    # track title text clip
    clip_title = gen_text.track(
        text=songObject.trackTitle,
        color=text_clip_title_font_color,
        resolution=resolution,
        font_size=text_clip_title_font_size,
        box_size=(1882, 1080),
        debug_mode=debug_mode)
    clip_title = clip_title.set_position((0.51, 0.1), relative=True)
    
    # making the transparent clip that will force the resolution
    clip_transparent = ImageClip('lib/transparent.png')
    clip_transparent = clip_transparent.resize(resolution)

    return CompositeVideoClip([clip_transparent, clip_color_background, clip_color_slab, clip_art, clip_artist, clip_title])
