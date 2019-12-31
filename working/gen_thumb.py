from moviepy.editor import *
import os
import gen_text

from PIL import Image, ImageFilter
import PIL

import gen_art
import gen_background

def make(text, file_name='thumb', is_album=False, debug_mode=False):

    # makes background for thumbnail
    gen_background.make(resolution=(1280,720), blur=100, file_name='background_thumb', debug_mode=debug_mode)

    # makes clip, set position
    temp = Image.open('temp/background_video.png')
    temp.thumbnail((1280,720), PIL.Image.ANTIALIAS)
    temp.save('temp/background_thumb.png', 'PNG')
    background = ImageClip('temp/background_thumb.png')
    background = background.set_position('center')

    # adds drop shadow to the ark, if it hasnt already
    gen_art.make(debug_mode=debug_mode)

    # make clip, gets size, sets position
    art_clip = ImageClip('temp/art_with_drop.png', transparent = True)
    art_clip = art_clip.resize(height = 725)
    art_clip = art_clip.set_position((-0.035, 'center'), relative = True)

    # makes text, dif depending if it is making it for the album
    if is_album:
        text_clip = gen_text.thumb(text + '\n(FULL ALBUM)')
    else:
        text_clip = gen_text.thumb(text)

    # sets text position
    text_clip = text_clip.set_position((0.5, 'center'), relative = True)

    thumbnail = CompositeVideoClip([background, art_clip, text_clip])
    thumbnail.save_frame(os.path.abspath(os.pardir) + '/thumb/' + file_name + '.png')
