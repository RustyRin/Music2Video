# Music2Video
Takes audio and cover art and exports a video to upload online

## Dependancies
- [MoviePy](https://github.com/Zulko/moviepy)
- [ImageMaick](https://www.imagemagick.org/script/index.php)
- [Mutagen](https://github.com/llogiq/mutagen)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Numpy](https://www.numpy.org/)
- [Noto Sans Font](https://www.google.com/get/noto/), but you can change it

## Running
1. Delete the files in export and import folders
2. Place in music files into input folder.
   - Music files need the following metadata:
     - **Track Number**: as an integer (ie. 5), not number out the total number of tracks (ie. 5/10)
     - **Track Artist**
     - **Track Name**
     - **Album Name**
3. Change settings (in working/gen_video.py global variables)
   - 4K or 1080p resolution (Default 4K)
   - Exporting the whole album as a whole video as well as individual videos (Defaults to True)
   - Debug mode that exports only 5 second videos (Off on default)
   - Clear export when starting

## Other
If you want to use this to upload to YouTube I suggest [porjo's youtubeuploader](https://github.com/porjo/youtubeuploader)

Odds are you're going to have trouble with fonts. [If you do try this](https://martin-thoma.com/add-a-new-font-to-imagemagick/)

Todo
- [ ] Force long single word song names to multi-line
- [ ] Allow mix of emojis and text in artist, album and title boxes
- [ ] Allow more granular control of the resolution by just giving the vertical height desired
- [ ] If album art is not 1:1 aspect ratio for the size of the art so it is more centered. Mostly for taller art.
- [ ] If there is a non-audio file in input, have it be skipped instead of breaking the program
- [ ] If the track title is really long, make the text size smaller
