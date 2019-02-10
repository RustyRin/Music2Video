from mutagen.flac import Picture, FLAC
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os


class song(object):     # takes in a mutagen object

    def __init__(self, file_path):

        if os.path.splitext(file_path)[1] == '.flac':
            audio = FLAC(file_path)

            try:  # TRACK TITLE
                self.trackTitle = clean_tag(str(audio['title']))
            except:
                print('Track title is not set or improper: ' + file_path)
                return

            try:  # TRACK NUMBER
                self.trackNumber = "{0:0>3}".format(clean_tag(str(audio['tracknumber'])))
            except:
                print('Track number not set or improper: ' + file_path)
                return

            try:  # TRACK ARTIST
                self.trackArtist = clean_tag(str(audio['artist']))
            except:
                print('Track artist not set or improper: ' + file_path)
                return

            try:  # TRACK ALBUM
                self.trackAlbum = clean_tag(str(audio['album']))
            except:
                print('Track album not set or improper: ' + file_path)
                return

            try:  # ALBUM ARTIST
                self.trackAlbumArtist = clean_tag(str(audio['albumartist']))
            except:
                print('Album artist not set or improper: ' + file_path)
                return

            try:  # ART
                os.system('ffmpeg -i \"' + file_path + '\" temp/art.png -y -loglevel quiet')
            except:
                print('Track art not set or improper: ' + file_path)
                return

            try:  # length
                self.trackLength = audio.info.length
            except:
                print('Not sure how, but cannot get song length: ' + file_path)
                return

        else:
            audio = EasyID3(file_path)

            try:  # TRACK TITLE
                self.trackTitle = clean_tag(str(audio['title']))
            except:
                print('Track title not set or improper: ' + file_path)
                return

            try:  # TRACK NUMBER
                self.trackNumber = "{0:0>3}".format(clean_tag(str(audio['tracknumber'])))
                if '/' in self.trackNumber:
                    raise Exception
            except:
                print('rack number not set or improper: ' + file_path)
                return

            try:  # TRACK ARTIST
                self.trackArtist = clean_tag(str(audio['artist']))
            except:
                print('Track artist not set or improper: ' + file_path)
                return

            try:  # TRACK ALBUM
                self.trackAlbum = clean_tag(str(audio['album']))
            except:
                print('Track album not set or improper: ' + file_path)
                return

            try:  # TRACK ALBUM ARTIST
                self.trackAlbumArtist = clean_tag(str(audio['albumartist']))
            except:
                print('Album artist not set or improper: ' + file_path)
                return

            try:  # ART
                os.system('ffmpeg -i \"' + file_path + '\" temp/art.png -y -loglevel quiet')
            except:
                print('Track art not set or improper: ' + file_path)
                return

            try:  # length
                audio = MP3(file_path)
                self.trackLength = audio.info.length
            except:
                print('Not sure how, but cannot get song length')
                return


def make_song(file_path):
    return song(file_path)


def save_art_flac(flac_object):
    pics = flac_object.pictures
    for p in pics:
        if p.type == 3: # front cover
            print('\nfound front cover')
            with open('cover.jpg', 'wb') as f:
                f.write(p.data)


def clean_tag(tag):
    return tag[2:-2]
