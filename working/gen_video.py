import os
from moviepy.editor import *
import sys
import cv2
import numpy as np
from PIL import Image

# object that holds song metadata
import song

# makes text clips
import gen_text

# takes the art and adds a drop shadow
import gen_art

# removes illegal or problematic characters for uploading
import string_clean

import gen_background

import gen_thumb

# settings
resolution   = (3840, 2160)        # desired resolution, prob only works at 16:9 ratio
make_album   = False                # at the send make one large video of all songs
make_songs   = True                # skip making songs and just make album of whats in export
upload_album = False                # upload the album video to youtube
upload_songs = False                # upload each song video to youtube
clear_export = True                # clears /export and /thumbs before making videos
debug_mode   = True                # displays extra prints, makes songs 5 sec long

# "advanced" settings
upload_binary = 'youtubeuploader'  # Change this to what your binary is named
video_background_blur = 10
thumbnail_background_blur = 100
video_gradient_opacity = 100
thumbnail_gradient_opacity = 100
# TODO
# add force black and white gradient

# making videos
def main():

    # have to initialize
    total_time = 0

    # clearing folders
    if clear_export:
        clear_folder(os.path.abspath(os.pardir) + '/export')
        clear_folder(os.path.abspath(os.pardir) + '/thumb')

    # making songs
    if make_songs:
            # for every file in /import
            for file_name in sorted(os.listdir(os.path.abspath(os.pardir) + '/import')):

                print('\n____________________________________\n')

                # making song object, which also saves /working/temp/art.png
                song_object = song.make_song(os.path.abspath(os.pardir) + '/import/' + file_name)

                # prints song metadata
                print('Title:        ' + song_object.trackTitle)
                print('Number:       ' + song_object.trackNumber)
                print('Album:        ' + song_object.trackAlbum)
                print('Album Artist: ' + song_object.trackAlbumArtist + '\n')

                # if debug mode, make vids 5 seconds long
                if debug_mode:
                    vid_length = 5
                else:
                    vid_length = song_object.trackLength

                # used to make the full album
                total_time += vid_length

                # making text clips
                clip_artist = gen_text.artist(text=song_object.trackArtist, resolution=resolution)
                clip_artist = clip_artist.set_position((0.5, 0.1), relative=True)

                clip_album = gen_text.album(text=song_object.trackAlbum, resolution=resolution)
                if len(song_object.trackArtist) > 38:    # if they have a long band name
                    clip_album = clip_album.set_position((0.5, 0.25), relative=True)
                else:
                    clip_album = clip_album.set_position((0.5, 0.17), relative=True)

                clip_track = gen_text.track(text=song_object.trackTitle, resolution=resolution)
                clip_track = clip_track.set_position((0.5, 0.35), relative=True)

                # making background image clips
                gen_background.make(resolution=resolution, blur=video_background_blur, file_name='background_video', debug_mode=debug_mode, gradient_opacity=video_gradient_opacity/100)
                background_clip = ImageClip('temp/background_video.png')
                background_clip = background_clip.set_position('center')

                # making art image clips
                gen_art.make(debug_mode=debug_mode)
                art_clip = ImageClip('temp/art_with_drop.png', transparent=True)
                #art_clip = art_clip.set_position((-0.01, 'center'), relative=True)

                # sizing
                art_clip = art_clip.resize(width=resolution[0]*.521)
                print('hello')
                print('Art clip size: ' + str(art_clip.size))

                # tall
                if (art_clip.size[0]/art_clip.size[1] > 1):
                    if debug_mode:
                        print("Short art")
                    art_clip.resize(height=resolution[1]*0.33)
                elif (art_clip.size[0]/art_clip.size[1] < 1):
                    if debug_mode:
                        print('Tall art')
                    art_clip = art_clip.resize(width=resolution[0]*.33)
                    art_clip = art_clip.set_position((0.04, 'center'), relative=True)
                elif (art_clip.size[0]/art_clip.size[1] == 1):
                    if debug_mode:
                        print('Square art')
                    art_clip = art_clip.resize(width=resolution[0]*.521)
                    art_clip = art_clip.set_position((-.01, 'center'), relative=True)


                # have to use transparent to force the resolution no matter what
                transparent_clip = ImageClip('transparent.png')
                transparent_clip = transparent_clip.resize(resolution)


                # making audio clip
                clip_audio = AudioFileClip(os.path.abspath(os.pardir) + '/import/' + file_name)

                # making thumbnail
                if upload_songs or upload_album is True:
                    gen_thumb.make(text=song_object.trackTitle, file_name=song_object.trackNumber, debug_mode=debug_mode, blur=thumbnail_background_blur, gradient_opacity=thumbnail_gradient_opacity/100)

                #making video

                video_clip = CompositeVideoClip([background_clip, art_clip, clip_artist, clip_album, clip_track])
                video_clip = video_clip.set_audio(clip_audio)
                video_clip = video_clip.set_duration(vid_length)

                if debug_mode:
                    video_clip.save_frame('temp/debug_frames/' + song_object.trackNumber + '.png')

                video_clip.write_videofile((os.path.abspath(os.pardir) + '/export/' + song_object.trackNumber + '.mp4'), fps=1, threads=8)

                # upload
                if upload_songs is True and debug_mode is False:
                    if sys.platform == 'linux':
                        #os.system('./youtubeuploader_linux_amd64 -filename \"' + os.path.abspath(os.pardir) + '/export/' + song_object.trackNumber + '.mp4\" -thumbnail \"/temp/thumb.png\" -title \"' + string_clean.clean(song_object.trackArtist) + ' // ' + string_clean.clean(song_object.trackTitle) + '\" -metaJSON ' + (os.path.abspath(os.pardir) + '/meta.json'))
                        os.system('./' + upload_binary + ' -filename \"' + os.path.abspath(os.pardir) + '/export/' + song_object.trackNumber + '.mp4' + '\" -thumbnail \"' + os.path.abspath(os.pardir) + '/thumb/' + song_object.trackNumber + '.png\" -title \"' + string_clean.clean(song_object.trackArtist) + ' // ' + string_clean.clean(song_object.trackTitle) + '\" -metaJSON ' + (os.path.abspath(os.pardir) + '/meta.json'))
                    else:
                        print('upload not currently implemented in windows, im just lazy')

                # closing
                clip_artist.close()
                clip_album.close()
                clip_track.close()
                background_clip.close()
                art_clip.close()
                transparent_clip.close()
                video_clip.close()

    if number_or_files(os.pardir + '/export') >= 2 and make_album is True:

        print('\n____________________________________\n\nBuilding Album\n')

        song_list = []

        gen_thumb.make(text=song_object.trackAlbum, is_album=True, debug_mode=debug_mode)

        for file_name in sorted(os.listdir(os.path.abspath(os.pardir) + '/export')):
            song_list.append(VideoFileClip(os.path.abspath(os.pardir + '/export/' + file_name)))

        whole_album = concatenate_videoclips(song_list, method='compose')

        whole_album.write_videofile(os.path.abspath(os.pardir) + '/export/album.mp4', fps=5, threads=8)

        if upload_album is True and debug_mode is False:
            os.system('./' + upload_binary + ' -filename \"' + os.path.abspath(os.pardir) + '/export/album.mp4' + '\" -thumbnail \"' + os.path.abspath(os.pardir) + '/thumb/thumb.png\" -title \"' + string_clean.clean(song_object.trackAlbumArtist) + ' // ' + string_clean.clean(song_object.trackAlbum) + ' (FULL ALBUM)\" -metaJSON ' + (os.path.abspath(os.pardir) + '/meta-album.json'))


### misc functions

def clear_folder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

# returns the number of files in folder
def number_or_files(dir):
    return len(os.listdir(dir))


if __name__ == '__main__':
    main()
