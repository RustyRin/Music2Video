from moviepy.editor import *
import sys
import unicode_search

# makes text clips in the artist theme
def artist(text, color='white', method='caption', make_4k=True, align='north-west'):
    if make_4k:
        font_size = 120
        size = (1982, 300)
    else:
        font_size = 60
        size = (991, 150)

    # you may need to edit unicode_search font names if your version of Noto has diffrent names
    font = unicode_search.search(text)
    if 'Emoji' not in font:
        font += 'I'

    return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)


# makes text clips in the album theme
def album(text, color='white', method='caption', make_4k=True, align='north-west'):

    if make_4k:
        font_size = 90
        size = (1982, 300)
    else:
        font_size = 45
        size = (991, 150)

    font = unicode_search.search(text)

    if 'Emoji' not in font:
        font += 'I'

    return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)


# makes text clips in the track title theme
def track(text, color='white', method='caption', make_4k=True, align='north-west'):

    if make_4k:
        font_size = 200
        size = (1900, 1320)
    else:
        font_size = 100
        size = (950, 660)

    font = unicode_search.search(text)

    if 'Emoji' not in font:
        font += 'Bk'

    return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)
