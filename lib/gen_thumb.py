from moviepy.editor import *
import os
from . import gen_text

from PIL import Image, ImageFilter
import PIL

'''
THIS NEEDS TO BE MOVED TO THE RADIO THEME FOLDER
Only reason it is not is because I just want themeing to be
working for the video first before I even think about making it work for the thumbnails
'''



from . import gen_art

sys.path.append(
    os.path.abspath(
        os.pardir
    ) + '/Music2Video/themes/radio'
)
import gen_background

def make(text, file_name='thumb', is_album=False, debug_mode=False, blur=100, gradient_opacity=100):

    # makes background for thumbnail
    if debug_mode:
        print('Thumbnail blur: ' + str(blur))
    gen_background.make(resolution=(1280,720), blur=blur, file_name='background_thumb', debug_mode=debug_mode)

    # makes clip, set position
    temp = Image.open('lib/temp/background_thumb.png')

    temp.thumbnail((1280,720), PIL.Image.ANTIALIAS)
    temp.save('lib/temp/background_thumb.png', 'PNG')
    background = ImageClip('lib/temp/background_thumb.png')
    background = background.set_position('center')

    # adds drop shadow to the ark, if it hasnt already
    gen_art.make(debug_mode=debug_mode)

    # make clip, gets size, sets position
    art_clip = ImageClip('lib/temp/art_with_drop.png', transparent = True)
    art_clip = art_clip.resize(height = 650)
    art_clip = art_clip.set_position((.005, 'center'), relative = True)

    # makes text, dif depending if it is making it for the album
    if is_album:
        text_clip = gen_text.thumb(text + '\n(FULL ALBUM)', debug_mode=debug_mode)
    else:
        text_clip = gen_text.thumb(text, debug_mode=debug_mode)

    # sets text position
    text_clip = text_clip.set_position((0.52, 'center'), relative = True)

    thumbnail = CompositeVideoClip([background, art_clip, text_clip])
    thumbnail.save_frame(file_name + '.png')
