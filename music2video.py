from moviepy.editor import *
from moviepy.video.VideoClip import ImageClip
from moviepy.audio.AudioClip import AudioArrayClip
from PIL import Image, ImageFilter
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os


make_4k = True      # do you want your video to be exported in 4K
make_whole_album = True     # do you want to make a video of the whole album


def number_or_files(dir):   # returns the number of files in folder
    return len([item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))])


def clean_tag(tag):     # mutagen gives track metadata in castings or something. this removes them
    return tag[2:-2]


def is_char_cjk(char):  # checks if given character is chinese, japanese or korean
    ranges = [          # idk what the ranges without comments are, the dude on stack overflow didn't say (or at least what i saw)
        {"from": ord(u"\u3300"), "to": ord(u"\u33ff")},  # compatibility ideographs
        {"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},  # compatibility ideographs
        {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},  # compatibility ideographs
        {"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")},  # compatibility ideographs
        {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},  # Japanese Kana, only thing i improved on it
        {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},  # cjk radicals supplement
        {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
        {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
        {"from": ord(u"\u3040"), "to": ord(u"\u309f")},  # japanese hiragana
        {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
        {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
        {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
        {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # included as of Unicode 8.0
    ]
    return any([range["from"] <= ord(char) <= range["to"] for range in ranges])


def is_string_cjk(input_string):    # checks if the string has any chinese, japanese or korean characters
    i = 0
    input_string = list(input_string)
    while i < len(input_string):
        if is_char_cjk(input_string[i]) == True:
            return True
        i += 1
    return False


def make_text(text, type, length=0, color='white', method='caption', align='north-west'):   # makes textclips
    if type == 'artist':

        if make_4k:
            font_size = 120
            size = (1982, 300)
        else:
            font_size = 60
            size = (991, 150)

        if is_string_cjk(text) is False:
            font = 'Noto-Sans-Italic'
        else:
            font = 'Noto-Sans-CJK-JP-Medium'

        return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)

    if type == 'album':

        if make_4k:     # If the selected size is 4K or not
            font_size = 90
            size = (1982, 200)
        else:
            font_size = 45
            size = (991, 100)

        if is_string_cjk(text) is False:        # If the text has a Chinese or Japanese Character in
            font = 'Noto-Sans-Light-Italic'
        else:
            font = 'Noto-Sans-CJK-JP-Light'

        return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)

    if type == 'track':
        font = 'Noto-Sans-Black'


        if make_4k:
            font_size = 200
            size = (1900, 1320)
        else:
            font_size = 100
            size = (950, 660)

        if is_string_cjk(text) is True:
            font = 'Noto-Sans-CJK-JP-Black'
        if length > 50:
            return TextClip(text, size=size, color=color, font=font, method=method, align=align)
        else:
            return TextClip(text, size=size, color=color, fontsize=font_size, font=font, method=method, align=align)


def main():
    for filename in os.listdir('input/'):   # finds finds the cover art photo in the input folder
        if os.path.splitext(filename)[1] == '.png' or '.jpg' or '.JPEG':
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
                album_artist = clean_tag(str(audio['albumartist']))
                vid_length = audio.info.length
            else:   # if it got past the first if then its either a FLAc or MP3 file, so else is good enough
                audio = EasyID3('input\\' + str(filename))
                song_number = "{0:0>3}".format(clean_tag(str(audio['tracknumber'])))
                song_artist = clean_tag(str(audio['artist']))
                song_track = clean_tag(str(audio['title']))
                song_album = clean_tag(str(audio['album']))
                album_artist = clean_tag(str(audio['albumartist']))
                audio = MP3('input\\' + str(filename))
                vid_length = audio.info.length

            # Debug length. Use this if something looks weird and you dont want to wait forever to export
            vid_length = 3

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

        whole_album.write_videofile('export/album.mp4', fps=1)


if __name__ == '__main__':
    main()