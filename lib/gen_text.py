from moviepy.editor import *
import sys
import unicode_search
import math

'''
Needs to be updated to accept more than just Noto fonts

needs to be updated to work nice with more than just radio theme
'''

# makes text clips in the artist theme
def artist(text, color='white', method='caption', font_size=None, resolution=(0,0), align='north-west', font=None, stroke_width=None, stroke_color=None,debug_mode=False):
    if font_size == None:
        font_size = int(resolution[1]/18)
    size = (int(resolution[1]* 0.917592593), int(resolution[1]*0.138888889))

    # you may need to edit unicode_search font names if your version of Noto has diffrent names
    if font == None:
        font = unicode_search.search(text)
    #font = 'NotoSansCJKjp'
    #print('Searched Font: ' + font)

        if 'Emoji' not in font and 'CJK' not in font:
            font += 'I'
        elif 'CJK' in font:
            font += '-Medium'

    if debug_mode:
        print('Artist Font: ' + font)

    return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align, stroke_color=stroke_color, stroke_width=stroke_width)


# makes text clips in the album theme
def album(text, color='white', method='caption', resolution=(0,0), make_4k=True, align='north-west', font=None, debug_mode=False):
    font_size = int(resolution[1] * 0.0417)
    size = (int(resolution[1] * 0.917592593), int(resolution[1] * 0.138888889))

    if font == None:
        font = unicode_search.search(text)

        if 'Emoji' not in font and 'CJK' not in font:
            font += 'I'
        elif 'CJK' in font:
            font += '-Medium'

    if debug_mode:
        print('Album Font: ' + font)

    return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)


# makes text clips in the track title theme
def track(text, color='white', method='caption', font_size=None, resolution=(0,0), box_size=None, make_4k=True, align='north-west', font=None, debug_mode=False):
    if font_size == None:
        font_size = int(resolution[1] * 0.092592593)

    if box_size == None:
        size = (int(resolution[1] * 0.87962963), int(resolution[1] * 0.611111111))
    else:
        size = box_size     # i know, this is dumb, but gotta do it unless i wanna break legacy stuff
    
    if font == None:
        font = unicode_search.search(text)

        if 'CJK' in font:
            font += '-Black'
        elif 'Emoji' not in font:
            font += 'DisplayBk'

    if debug_mode:
        print('Track Font: ' + font)

    return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)


# makes text clips in the thumbnail theme
def thumb(text, color='white', method='caption', resolution=(0,0), make_4k=True, align='north-west', font = None,debug_mode=False):

    size = (550, 570)

    if font == None:
        font = unicode_search.search(text)

        if 'Emoji' not in font:
            if font == 'NotoSans':
                font += 'CB'
            else:
                font += '-Black'

    if debug_mode:
        print('Tumbnail Font: ' + font)

    return TextClip(text, size=size, color=color, font=font, method=method)
