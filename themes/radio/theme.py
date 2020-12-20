from moviepy.editor import *

# object that holds song metadata
from lib import song

# makes text clips
from lib import gen_text

# takes the art and adds a drop shadow
from lib import gen_art

# removes illegal or problematic characters for uploading
from lib import string_clean

# makes the backgrounds
from themes.radio import gen_background

# makes the thumbnails for youtube uploads
from lib import gen_thumb

def make(songObject=None, resolution=(1920,1080), debug_mode=False, forceBGColor=None, forceGradientColor=None, forceFont=None):


    # make a settings file that you would copy with thise theme file
    # make some sort of settings comfirmation function that checks if say
    # this settings file would have a sections that is the the name of the theme it is for
    # then this theme file would compare the theme name to one saved here
    # if they do not match throw an exception

    # if you need to force the color of the gradient. Will only work for "black" to force black gradient or "white" to force a white one, enter None to have it automatical do it
    force_gradient_color = None

    # how blurry you want to make background of the video to be, defult is 20
    video_background_blur = 20

    # how see through you want tht gradient to be, default is 95
    video_gradient_opacity = 95

    # making text clips
    clip_artist = gen_text.artist(text=songObject.trackArtist, resolution=resolution, debug_mode=debug_mode)
    clip_artist = clip_artist.set_position((0.5, 0.1), relative=True)

    clip_album = gen_text.album(text=songObject.trackAlbum, resolution=resolution, debug_mode=debug_mode)
    if len(songObject.trackArtist) > 38:    # if they have a long band name
        clip_album = clip_album.set_position((0.5, 0.25), relative=True)
    else:
        clip_album = clip_album.set_position((0.5, 0.17), relative=True)

    clip_track = gen_text.track(text=songObject.trackTitle, resolution=resolution, debug_mode=debug_mode)
    clip_track = clip_track.set_position((0.5, 0.35), relative=True)

    # making background image clips
    gen_background.make(resolution=resolution, blur=video_background_blur, file_name='background_video', debug_mode=debug_mode, gradient_opacity=video_gradient_opacity/100)
    background_clip = ImageClip('lib/temp/background_video.png')
    background_clip = background_clip.set_position('center')

    # make art clip
    art_clip = gen_art.make()

    if (art_clip.size[0]/art_clip.size[1] > 1):
        if debug_mode:
            print("Short art")
        art_clip.resize(height=resolution[1]*0.33)
        art_clip = art_clip.set_position((-.01, 'center'), relative=True)
    elif (art_clip.size[0]/art_clip.size[1] < 1):
        if debug_mode:
            print('Tall art')
        art_clip = art_clip.resize(width=resolution[0]*.51)
        art_clip = art_clip.set_position((0.002, 'center'), relative=True)
    elif (art_clip.size[0]/art_clip.size[1] == 1):
        if debug_mode:
            print('Square art')
        art_clip = art_clip.resize(width=resolution[0]*.64)
        art_clip = art_clip.set_position((-.064, 'center'), relative=True)


    # have to use transparent to force the resolution no matter what
    transparent_clip = ImageClip('lib/transparent.png')
    transparent_clip = transparent_clip.resize(resolution)

    # make thumbnail for this song with the themes tumbnail file
    # needs to be updated
    gen_thumb.make(text=songObject.trackTitle, file_name=('thumb/' + songObject.trackNumber + '.png'), debug_mode=debug_mode)
    gen_thumb.make(text=songObject.trackAlbum, file_name=('thumb/album.png'), is_album=True, debug_mode=debug_mode)
    
    return CompositeVideoClip([background_clip, art_clip, clip_artist, clip_album, clip_track])

if __name__ == "__main__":
    make(songObject=None, forceBGColor=None, forceGradientColor=None, forceFont=None)