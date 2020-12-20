from moviepy.editor import *
import moviepy.video.fx.all as vfx
from lib import song
from lib import dropShadow
from lib import gen_art
from lib import gen_text
from lib import gen_thumb

from themes.weDidThis import gen_background

def make(songObject = None, resolution = (3840, 2160), debug_mode=False, forceBGColor=None, forceGradientColor=None, forceFont=None):

    # this theme was made with live for We Did This Records <3
    shadow_color = '#000000'
    artist_album_text_color= '#f2f2f2'

    video_background_blur = 20
    video_gradient = 95
    force_gradient_color = True

    clip_cat_top = ImageClip(
        dropShadow.apply(
            image='./themes/weDidThis/logo_cat_top.png',
            blurAmount = 15,
            dropOffset= (5,5),
            shadowColor=shadow_color
        )
    )
    clip_cat_top = clip_cat_top.set_position( (.84, -.014), relative=True)
    clip_cat_top = clip_cat_top.resize(width=int(resolution[0]*.15))

    clip_cat_bottom = ImageClip(
        dropShadow.apply(
            image='./themes/weDidThis/logo_cat_bottom.png',
            blurAmount=15,
            dropOffset=(5,5),
            shadowColor=shadow_color
        )
    )
    clip_cat_bottom = clip_cat_bottom.set_position( (.84, .85), relative=True)
    clip_cat_bottom = clip_cat_bottom.resize(width=int(resolution[0]*.15))

    clip_africa = ImageClip(
        dropShadow.apply(
            image = './themes/weDidThis/africa_RP.png',
            blurAmount = 30,
            shadowColor = shadow_color,
            dropOffset = (0,0)
        )
    )
    clip_africa = clip_africa.set_position((0.75, 'center'), relative=True)


    clip_art = gen_art.make(
        debug_mode=debug_mode,
        artLocation=None,
        drop_shadow_blur=30,
        drop_shadow_color=shadow_color,
        drop_shadow_zoom=1.9,
        drop_shadow_offset=(0,0) 
    )
    clip_art = clip_art.set_position((0.327, 'center'), relative=True)
    clip_art = clip_art.resize(width=int(resolution[0]*.845))

    gen_background.make(
        resolution = resolution,
        blur = video_background_blur,
        file_name = 'background_video',
        debug_mode = debug_mode,
        gradient_opacity = video_gradient/100,
        force_light_gradient=force_gradient_color
    )
    clip_background = ImageClip('lib/temp/background_video.png')
    clip_background = clip_background.set_position('center')
    '''
    clip_artist = gen_text.artist(
        text=(songObject.trackArtist + ' // ' + songObject.trackAlbum),
        color='#FFFFFF',
        resolution=resolution,
        font='NotoSansDisplayI',
        debug_mode=debug_mode,
        stroke_color='black',
        stroke_width=0,
        font_size=100
    )
    '''
    clip_artist = TextClip(
        txt=(songObject.trackArtist),
        color=artist_album_text_color,
        fontsize=int(resolution[1]/25.0),
        font='NotoSansI',
        align='north-west'
    )
    clip_artist = clip_artist.set_position((.02, 0.1), relative=True)

    clip_track = TextClip(
        txt = songObject.trackTitle,
        color='white',
        fontsize= int(resolution[1] * 0.122592593),
        font='NotoSansBk',
        align='north-west',
        size = (int(resolution[1] * 0.88962963), int(resolution[1] * 0.621111111)),
        method='caption'
    )
    clip_track = clip_track.set_position((.02, .125), relative=True)


    # have to use transparent to force the resolution no matter what
    transparent_clip = ImageClip('lib/transparent.png')
    transparent_clip = transparent_clip.resize(resolution)

    clip = CompositeVideoClip([transparent_clip, clip_background, clip_cat_top, clip_cat_bottom, clip_artist, clip_track, clip_art])
    clip.save_frame('lib/temp/debug_frames/' + songObject.trackNumber + '.png')

    gen_thumb.make(text=songObject.trackTitle, file_name=('thumb/' + songObject.trackNumber), debug_mode=debug_mode)

    return clip