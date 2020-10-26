import os
from moviepy.editor import *
import sys
import cv2
import numpy as np
from PIL import Image
import argparse
import importlib

# custom functions to make my life easier
# from lib import myFunctions   # not needed rn, but maybe in the future

# object that holds song metadata
from lib import song

# removes illegal or problematic characters for uploading
from lib import string_clean

# makes the thumbnails for youtube uploads
from lib import gen_thumb

# makes the composite video clip
import theme 

# listing the folders in /themes which hold available themes
def listThemes():
    return next(os.walk(os.path.abspath('themes')))[1]

# making videos
def main(args):

    # settings
    resolution   = args.resolution     # desired resolution, prob only works at 16:9 ratio
    make_album   = args.makeAlbum      # at the send make one large video of all songs
    make_songs   = args.makeSongs      # skip making songs and just make album of whats in export
    upload_album = args.uploadAlbum    # upload the album video to youtube
    upload_songs = args.uploadSongs    # upload each song video to youtube
    clear_export = args.clearExport    # clears /export and /thumbs before making videos
    debug_mode   = args.debugMode      # displays extra prints, makes songs 5 sec long
    fps          = int(args.fps)       # the framerate of the exported video

    # have to initialize
    total_time = 0

    # clearing folders
    if clear_export:
        clear_folder('export')
        clear_folder('thumb')

    # making songs
    if make_songs:
            # for every file in /import
            for file_name in sorted(os.listdir('import')):

                print('\n____________________________________\n')

                # making song object, which also saves /working/temp/art.png
                song_object = song.make_song('import/' + file_name)

                # prints song metadata
                print('Title:        ' + song_object.trackTitle)
                print('Number:       ' + song_object.trackNumber)
                print('Album:        ' + song_object.trackAlbum)
                print('Track Artist: ' + song_object.trackArtist)
                print('Album Artist: ' + song_object.trackAlbumArtist + '\n')

                # if debug mode, make vids 5 seconds long
                if debug_mode:
                    vid_length = 5
                else:
                    vid_length = song_object.trackLength

                # used to make the full album
                total_time += vid_length

                # set up video from the theme
                video_clip = theme.make(songObject=song_object, resolution=resolution, debug_mode=debug_mode)
                
                # make the audio clip from the music
                # then set the music to be the audio
                clip_audio = AudioFileClip('import/' + file_name)
                video_clip = video_clip.set_audio(clip_audio)
                video_clip = video_clip.set_duration(vid_length)

                if debug_mode:
                    video_clip.save_frame('lib/temp/debug_frames/' + song_object.trackNumber + '.png')

                video_clip.write_videofile(( 'export/' + song_object.trackNumber + '.mp4'), fps=fps, threads=12)

                # upload
                if upload_songs is True and debug_mode is False:
                    if sys.platform == 'linux':
                        # this needs to be fixed when i get upload token again
                        os.system('./' + upload_binary + ' -filename \"' + os.path.abspath(os.pardir) + '/export/' + song_object.trackNumber + '.mp4' + '\" -thumbnail \"' + os.path.abspath(os.pardir) + '/thumb/' + song_object.trackNumber + '.png\" -title \"' + string_clean.clean(song_object.trackArtist) + ' // ' + string_clean.clean(song_object.trackTitle) + '\" -metaJSON ' + (os.path.abspath(os.pardir) + '/meta.json'))
                    else:
                        print('upload not currently implemented in windows, im just lazy')

                # closing
                video_clip.close()

    if number_or_files('export') >= 2 and make_album is True:

        print('\n____________________________________\n\nBuilding Album\n')

        song_list = []

        #gen_thumb.make(text=song_object.trackAlbum, is_album=True, debug_mode=debug_mode, gradient_opacity=thumbnail_gradient_opacity/100)
        gen_thumb.make(text=song_object.trackAlbum, is_album=True, debug_mode=debug_mode, gradient_opacity=100/100)

        for file_name in sorted(os.listdir('export/')):
            song_list.append(VideoFileClip('export/' + file_name))

        whole_album = concatenate_videoclips(song_list, method='compose').set_duration(total_time)

        whole_album.write_videofile('export/album.mp4', fps=fps, threads=12)

        if upload_album is True and debug_mode is False:
            # this needs to be fixed when i get an upload token
            os.system('./lib/youtubeuploader -filename \"export/album.mp4\" -thumbnail \"thumb/album.png\" -title \"' + song_object.trackAlbumArtist + ' // ' + song_object.trackAlbum + ' (FULL ALBUM)\" -metaJSON meta-album.json')

### misc functions

# clears given folder, might need to move to myFunctions
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
    parser = argparse.ArgumentParser(description="This generates videos from given mp3 and flac files.")
    parser.add_argument("--listThemes", help="Lists the available themes", action="store_true")

    parser.add_argument("--resolution", default=(3840,2160), help="To set the video resolution. Using high resoltions with makeAlbum on will crash if you run out of ram. MUST be in (horizontal,height)")
    parser.add_argument('--fps', default=24, help="The framerate of the exported video, lower numbers save space and speed up rendering, higher makes any animations in selected theme smoother. Default is 24")
    parser.add_argument("--makeAlbum", choices=[True, False], default=True,help="If you want to export all of the videos into one long album long video, this eats up ram at high resolutions")
    parser.add_argument("--makeSongs", choices=[True, False], default=True, help="If you want to make the songs, default is True. This is useful if you already made some of the videos and want to only render specific videos while exporting full album")
    parser.add_argument("--uploadSongs", choices=[True, False], default=False, help="If you want to upload videos to YouTube after render. You need to set up the uploader first.")
    parser.add_argument("--uploadAlbum", choices=[True, False], default=False, help="If you want to upload the album video after render, make album also need to be eneabled.")
    parser.add_argument('--clearExport', choices=[True, False], default=True, help="clears the export and thumbnail folders after rendering")
    parser.add_argument('--debugMode', default=False, help="Enables debug mode. This enables verbose logging and forces all videos to be 5 seconds long.")

    parser.add_argument('--themeSettings', help="For any arguments for the theme you are using")
    args = parser.parse_args()

    if args.listThemes:
        print("Available themes in " + str(os.path.abspath('themes')) + '\n' + str(listThemes()))
    else:
        main(args)
