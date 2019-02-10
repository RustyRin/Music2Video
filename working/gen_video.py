import os
from moviepy.editor import *
import sys
import cv2
import numpy as np

import song
import gen_text
from PIL import Image, ImageFilter

# settings
make_4k = True  # resolution, if false resolution will be 1080p
make_whole_album = True  # will make one large video from the videos from export. will use lots of ram
make_songs = True  # do you want to make a video for each song. really only used for making album vid after batch rendering
debug_mode = True  # makes videos 5 seconds long
clear_export = True  # do you want to clear the export folder on startup. good for large albums


# this looks at the album art and returns true if its dark
def is_art_dark(file_name):
    img = cv2.imread('temp/art.png')
    # it makes a histogram of the gray scale
    histogram = cv2.calcHist([img], [0], None, [256], [0, 255])

    # fiddle with this for how sensitive dark detection is
    if sum(histogram[:30]) > sum(histogram[30:]):
        # is dark
        return True
    else:
        # is light
        return False


# returns the number of files in folder
def number_or_files(dir):
    return len(os.listdir(dir))


# deletes  the contents of a specified folder, i'm only using it to clear export
def clear_folder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


# makes the blurred art background
def make_background():
    temp = Image.open('temp/art.png')
    temp = temp.filter(ImageFilter.GaussianBlur(radius=100))
    temp.save('temp/blurred_art_video.png', 'PNG')
    temp.close()
    if make_4k:
        return ImageClip('temp/blurred_art_video.png').set_position('center').resize(width=4000)
    else:
        return ImageClip('temp/blurred_art_video.png').set_position('center').resize(width=2000)


# makes the art clip that is put on the left
def make_art_clip():
    art = Image.open('temp/art.png')  # might not need, keeping just in case
    art_width, art_height = art.size  # only time it might be good is odd sized album art
    art.close()

    if make_4k:
        art = ImageClip('temp/art.png').set_position((144, 300)).resize(width=1600)  # art clip

        art_drop = ImageClip('drop_square.png', transparent=True)  # makes drop shadow clip
        art_drop = art_drop.set_position((50, 200))  # set pos

        ratio = art_width / 1800

        art_drop = art_drop.resize((art_width, art_height))  # resize
        art_drop = art_drop.resize(width=1800)

        transparent = ImageClip('transparent.png')  # makes transparent, have to have to force resolution
        transparent = transparent.set_position('center')  # pos
        transparent = transparent.resize(width=3840)  # resize
    else:
        art = ImageClip('temp/art.png').set_position((72, 150)).resize(width=800)  # art clip
        art_drop = ImageClip('drop_square.png', transparent=True).set_position((25, 100)).resize(width=900)  # drop clip
        transparent = ImageClip('transparent.png')  # transparent clip

    art_drop = art_drop.set_opacity(0.5)  # sets drop opacity, if you want to tweak

    return CompositeVideoClip([transparent, art_drop, art])


def main():
    # clearing export
    if clear_export:
        clear_folder(os.path.abspath(os.pardir) + '/export')

    total_time = 0  # might not need, only used for making the whole album part
    album_artist = ""
    album_name = ""

    if make_songs:
        for file_name in sorted(os.listdir(os.path.abspath(os.pardir) + '/import')):
            print('\n____________________________________\n')

            # gets song object
            song_object = song.make_song(os.path.abspath(os.pardir) + '/import/' + file_name)
            album_artist = song_object.trackAlbumArtist
            album_name = song_object.trackAlbum

            # gradient
            if make_4k:
                transparent = ImageClip('transparent.png').set_position('center').resize(width=3840)
                if is_art_dark('temp/art.png'):
                    gradient = ImageClip('gradient_white.png').set_position('center').resize(width=3840)
                else:
                    gradient = ImageClip('gradient.png').set_position('center').resize(width=3840)

                # have to have transparent because composite video clip will make the first clip the resolution of the export
            else:
                transparent = ImageClip('transparent.png').set_position('center').resize(width=1920)
                if is_art_dark('temp/art.png'):
                    gradient = ImageClip('gradient_white.png').set_position('center').resize(width=1920)
                else:
                    gradient = ImageClip('gradient.png').set_position('center').resize(width=1920)

            # debug mode makes the videos shorter so it exports faster
            if debug_mode:
                vid_length = 5
            else:
                vid_length = song_object.trackLength

            total_time += vid_length

            # maked text clips
            if make_4k:
                clip_artist = gen_text.artist(song_object.trackArtist).set_position((1858, 300))

                if len(song_object.trackArtist) > 38:  # if the band has a really long name
                    clip_album = gen_text.album(song_object.trackAlbum).set_position((1858, 600))
                else:
                    clip_album = gen_text.album(song_object.trackAlbum).set_position((1858, 460))

                clip_track = gen_text.track(song_object.trackTitle).set_position((1858, 800))

            else:
                clip_artist = gen_text.artist(song_object.trackArtist, make_4k=False).set_position((929, 150))

                if len(song_object.trackArtist) > 38:
                    clip_album = gen_text.album(song_object.trackAlbum, make_4k=False).set_position((929, 300))
                else:
                    clip_album = gen_text.album(song_object.trackAlbum, make_4k=False).set_position((929, 225))

                clip_track = gen_text.track(song_object.trackTitle, make_4k=False).set_position((929, 400))

            clip_audio = AudioFileClip(os.path.abspath(os.pardir) + '/import/' + file_name)

            # write video
            video = CompositeVideoClip(
                [transparent, make_background(), gradient, make_art_clip(), clip_artist, clip_album, clip_track])
            video = video.set_audio(clip_audio)
            video = video.set_duration(vid_length)
            video.write_videofile((os.path.abspath(os.pardir) + '/export/' + song_object.trackNumber + '.mp4'), fps=1)

            # closing
            album = song_object.trackAlbum
            clip_audio.close()
            clip_track.close()
            clip_album.close()
            clip_artist.close()
            video.close()
            del clip_artist, clip_album, clip_track, clip_audio, video, vid_length, transparent, gradient, song_object

    # if there is more than 2 files in the export folder and make album is true; make album
    if number_or_files(os.pardir + '/export') >= 2 and make_whole_album is True:
        song_list = []  # video file clips of the individual songs are added to array

        for file_name in sorted(os.listdir(os.path.abspath(os.pardir) + '/export')):    # adding to array
            song_list.append(VideoFileClip(os.path.abspath(os.pardir + '/export/' + file_name)))

        whole_album = concatenate_videoclips(song_list, method='compose')

        if make_4k:
            whole_album = whole_album.resize(width=3840)
        else:
            whole_album = whole_album.resize(width=1080)

        # export
        whole_album.write_videofile(os.path.abspath(os.pardir) + '/export/album.mp4', fps=5)

if __name__ == '__main__':
    main()
