# Music2Video
Takes audio and cover art and exports a video to upload online

## Dependancies
- [MoviePy](https://github.com/Zulko/moviepy)
- [ImageMaick](https://www.imagemagick.org/script/index.php)
- [Mutagen](https://github.com/llogiq/mutagen)

## Running
1. Delete the files in export and import folders
2. Place in music files into input folder.
   - Music files need the following metadata: 
     - **Track Number**: as a simple number (ie. 5), not number out the total number of tracks (ie. 5/10)
     - **Track Artist**
     - **Track Name**
     - **Album Name**
     - **Album Artist**: diffrent from track artist
3. If you want to can change a bit of settings in the python file, such as
   - 4K or 1080p resolution (Default 4K)
   - Exporting the whole album as a whole video as well as individual videos (Defaults to True)
   - Debug mode that exports only 5 second videos (Off on default)
   
## Other
If you want to use this to upload to YouTube I suggest [porjo's youtubeuploader](https://github.com/porjo/youtubeuploader)
