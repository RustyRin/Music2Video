# Music2Video
Takes audio and cover art and exports a video to upload online

## Dependancies
- [MoviePy](https://github.com/Zulko/moviepy)
- [PIL](https://pillow.readthedocs.io/en/stable/), IIRC it is installed with Python 3 by default now.
- [ImageMaick](https://www.imagemagick.org/script/index.php)
- [Mutagen](https://github.com/llogiq/mutagen)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Numpy](https://www.numpy.org/)
- [Noto Sans Font](https://www.google.com/get/noto/), but you can change it

## Running
1. There are files in `import/` and in `export/` they are only there so GitHub keeps the folders. At least delete the file in `import/`
2. Place in music files into input folder.
   - Music files need the following metadata:
     - **Track Number**: as an integer (ie. 5), not number out the total number of tracks (ie. 5/10)
     - **Track Artist**
     - **Track Name**
     - **Album Name**
3. Change settings (in `working/gen_video.py` global variables)
   - You can export in any resolution you want. Most tested is 1080p and 4K.
   - Set if you want to make a while album video, this is **VERY** memory intensive.
   - Set if you want to make songs. This will have purpose in the future for album only exporting.
   - Upload songs and album is for if you want to upload the videos to YouTube. To read more about this see [porjo's youtubeuploader](https://github.com/porjo/youtubeuploader) on how to set this up.
     - uploader_binary is the filename of the uploader that you got from porjo.
     - If you are uploading, it will be looking for `request.token` in `working/` so put your Google token in there
   - clear_export will clear `export/` (and `thumbs/` if you have either uploading enabled) when you start the script.
   - debug_mode prints debug lines and sets the video length to 5 seconds. This is true by default so you can make sure everything works before running for real.
4. Run `working/gen_video.py`

## Other
Odds are you're going to have trouble with fonts. [If you do try this](https://martin-thoma.com/add-a-new-font-to-imagemagick/)

## Todo
- [ ] If album art is not 1:1 aspect ratio for the size of the art so it is more centered. Mostly for taller art.
- [ ] If there is a non-audio file in input, have it be skipped instead of breaking the program
- [ ] If the track title is really long, make the text size smaller
