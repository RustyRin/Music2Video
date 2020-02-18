from moviepy.editor import *
import sys
import unicode_search
import math

# makes text clips in the artist theme
def artist(text, color='white', method='caption', resolution=(0,0), align='north-west'):
    font_size = int(resolution[1]/18)
    size = (int(resolution[1]* 0.917592593), int(resolution[1]*0.138888889))

    # you may need to edit unicode_search font names if your version of Noto has diffrent names
    font = unicode_search.search(text)
    #font = 'NotoSansCJKjp'

    if 'Emoji' not in font or 'CJK' not in font:
        font += 'I'

    return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)


# makes text clips in the album theme
def album(text, color='white', method='caption', resolution=(0,0), make_4k=True, align='north-west'):
    font_size = int(resolution[1] * 0.0417)
    size = (int(resolution[1] * 0.917592593), int(resolution[1] * 0.138888889))

    font = unicode_search.search(text)
    #font = 'NotoSansCJKjp'
    #print('Album Font: ' + font)

    if 'Emoji' not in font or 'CJK' not in font:
        font += 'I'
    elif 'CJK' in font:
        font += '-Medium'

    return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)


# makes text clips in the track title theme
def track(text, color='white', method='caption', resolution=(0,0), make_4k=True, align='north-west'):
    font_size = int(resolution[1] * 0.092592593)
    size = (int(resolution[1] * 0.87962963), int(resolution[1] * 0.611111111))

    font = unicode_search.search(text)
    #font = 'SF-Pro-Display-Black'3


    if 'CJK' in font:
        font += '-Black'
    elif 'Emoji' not in font:
        font += 'DisplayBk'
    #font = 'NotoSansBk'

    return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)


# makes text clips in the thumbnail theme
def thumb(text, color='white', method='caption', resolution=(0,0), make_4k=True, align='north-west'):

    size = (550, 570)

    font = unicode_search.search(text)
    #font = 'NotoSansCJKjp'

    if 'Emoji' not in font:
        if font == 'NotoSans':
            font += 'CB'
        else:
            font += '-Black'

    return TextClip(text, size=size, color=color, font=font, method=method)
