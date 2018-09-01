from moviepy.editor import *
from moviepy.video.VideoClip import ImageClip
from moviepy.audio.AudioClip import AudioArrayClip
from PIL import Image, ImageFilter
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os, sys
sys.path.append(os.getcwd())
import unicode_search


make_4k = True      # do you want your video to be exported in 4K
make_whole_album = True     # do you want to make a video of the whole album
debug_mode = False


def number_or_files(dir):   # returns the number of files in folder
    return len([item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))])


def clean_tag(tag):     # mutagen gives track metadata in castings or something. this removes them
    return tag[2:-2]


def make_text(text, type, length=0, color='white', method='caption', align='north-west'):   # makes textclips
    if type == 'artist':

        if make_4k:
            font_size = 120
            size = (1982, 300)
        else:
            font_size = 60
            size = (991, 150)

        font = unicode_search.search(text)
        if font != 'Noto-Emoji':
            font += '-Italic'

        return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)

    if type == 'album':

        if make_4k:     # If the selected size is 4K or not
            font_size = 90
            size = (1982, 300)
        else:
            font_size = 45
            size = (991, 150)

        font = unicode_search.search(text)
        if font != 'Noto-Emoji':
            font += '-Italic'

        return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)

    if type == 'track':
        font = unicode_search.search(text)
        if font != 'Noto-Emoji':
            font += '-Black'

        if make_4k:
            font_size = 200
            size = (1900, 1320)
        else:
            font_size = 100
            size = (950, 660)

        if length > 50:
            return TextClip(text, size=size, color=color, font=font, method=method, align=align)
        else:
            return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)

    if type == 'thumb':
        size = (610, 570)
        font = unicode_search.search(text)
        if font != 'Noto-Emoji':

            if font == 'Noto-Sans':
                font += '-Condensed-Bold'
            else:
                font += '-Bold'

        return TextClip(text, size=size, color=color, font=font, method=method)


def clear_folder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def main():

    # CLEARING EXPORT FOLDER
    clear_folder('export')

    for filename in os.listdir('input/'):   # finds finds the cover art photo in the input folder
        if os.path.splitext(filename)[1] == '.png' or os.path.splitext(filename)[1] == '.jpg' or os.path.splitext(filename)[1] == '.JPEG':
            album_art = 'input/' + filename

    # TRANSPARENT
    # it needs transparent to se the size of the frame. compose video takes the first clip as the size of the video. this is going behind everything
    if make_4k:
        transparent = ImageClip('working/transparent.png').resize(width=3840)
    else:
        transparent = ImageClip('working/transparent.png')

    # BACKGROUNG BLURRED CLIP
    temp = Image.open(album_art)    # makes the blurred background IMAGE, not ImageClip
    bg = temp.filter(ImageFilter.GaussianBlur(radius=100))
    bg.save('working/background_blurred.png', 'PNG')
    art_width, art_height = temp.size   # used for making drop shadows in the gradient and drop shadow section
    bg.close()
    background_blurred = ImageClip('working/background_blurred.png').set_position('center')
    if make_4k:
        background_blurred = background_blurred.resize(width=4000)
    else:
        background_blurred = background_blurred.resize(width=2000)

    # ALBUM ART CLIP
    art_clip = ImageClip(album_art, transparent=True)
    if make_4k:     # makes the album art ImageClip, resizes itm then positions it into place
        art_clip = art_clip.resize(width=1600).set_position((144, 300))
    else:
        art_clip = art_clip.resize(width=800).set_postion((72, 150))

    # GRADIENT CLIP, DROPSHADOW CLIP
    drop_image = Image.open('working/drop_square.png')
    drop_image = drop_image.resize((art_width, art_height), Image.ANTIALIAS)
    drop_image.save('working/drop_shadow.png')
    if make_4k:
        gradient = ImageClip('working/gradient.png', transparent=True).resize(width=3840)
        drop_shadow = ImageClip('working/drop_shadow.png', transparent=True).resize(width=1800).set_position((50, 200))
    else:
        gradient = ImageClip('working/gradient.png', transparent=True)
        drop_shadow = ImageClip('working/drop_shadow.png', transparent=True).resize(width=900).set_position((25, 100))

    drop_shadow = drop_shadow.set_opacity(0.5)  # default is 0.5

    totaltime = 0 # might not need, only see it in the make whole album part

    for filename in os.listdir('input/'):

        # just to make it pretty when i run it in
        print("________________________________________________________________________________________________________________________\n")

        print('Filename: ' + filename)
        if os.path.splitext(filename)[1] == '.flac' or os.path.splitext(filename)[1] == '.mp3':      # checks if the file in input is a FLAC or MP3 file

            # FLAC FILES
            if os.path.splitext(filename)[1] == '.flac':
                audio = FLAC('input/' + str(filename))
                song_number = "{0:0>3}".format(clean_tag(str(audio['tracknumber'])))
                song_artist = clean_tag(str(audio['artist']))
                song_track = clean_tag(str(audio['title']))
                song_album = clean_tag(str(audio['album']))
                vid_length = audio.info.length
            else:   # if it got past the first if then its either a FLAc or MP3 file, so else is good enough
                audio = EasyID3('input\\' + str(filename))
                song_number = "{0:0>3}".format(clean_tag(str(audio['tracknumber'])))
                song_artist = clean_tag(str(audio['artist']))
                song_track = clean_tag(str(audio['title']))
                song_album = clean_tag(str(audio['album']))
                audio = MP3('input\\' + str(filename))
                vid_length = audio.info.length

            if debug_mode:
                vid_length = 5

            totaltime += vid_length

            print('Song: ' + song_track + '\nTrack number: ' + song_number + '\nArtist: ' + song_artist + '\nAlbum: ' + song_album + '\nAlbum Artist: ' + album_artist + '\n')

            # MAKING TEXT CLIPS
            if make_4k:

                clip_artist = make_text(song_artist, 'artist').set_position((1858, 300))
                if len(song_artist) > 30:   # if the artist name is over 30 char it will shift the album text down
                    clip_album = make_text(song_album, 'album').set_position((1858, 600))
                else:
                    clip_album = make_text(song_album, 'album').set_position((1858, 460))

                clip_track = make_text(song_track, 'track').set_position((1858, 800))
            else:
                clip_artist = make_text(song_artist, 'artist').set_position((929, 150))
                if len(song_artist) > 30:   # if the artist name is over 30 char it will shift the album text down
                    clip_album = make_text(song_album, 'album').set_position((929, 300))
                else:
                    clip_album = make_text(song_album, 'album').set_position((929, 225))

                clip_track = make_text(song_track, 'track').set_position((1858, 800))

            clip_audio = AudioFileClip('input/' + filename)

            # EXPORTING
            video = CompositeVideoClip([transparent, background_blurred, gradient, drop_shadow, art_clip, clip_artist, clip_album, clip_track]).set_audio(clip_audio).set_duration(vid_length)
            video.write_videofile(('export/' + song_number + '.mp4'), fps=1)    # it is a static image, the fps does not matter

            # CLOSING
            clip_audio.close()
            del video
            del clip_audio
            del clip_track
            del clip_album
            del clip_artist

    # MAKING ALBUM VIDEO
    if number_or_files('input/') > 2 and make_whole_album == True:
        song_list = []  # this makes an array of all the video files in export. i found it easier to just re-export the video files in a cocatenate

        print("________________________________________________________________________________________________________________________\n")

        for filename in os.listdir('export/'):
            song_list.append(VideoFileClip('export/' + filename))

        whole_album = concatenate_videoclips(song_list, method='compose')
        if make_4k:
            whole_album = whole_album.resize(width=3840)
        else:
            whole_album = whole_album.resize(width=1920)

        whole_album = whole_album.set_duration(totaltime)

        whole_album.write_videofile('export/album.mp4', fps=5)


if __name__ == '__main__':
    main()
