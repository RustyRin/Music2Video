# How To Make Themes

Theme files are basic files that just make [CompositeVideoClips](https://zulko.github.io/moviepy/getting_started/compositing.html#id1) and return them back to the main `music2video` python file.

The theme file **MUST** be named `theme.py` and must have a function called `make` that takes in a sonngObject, a resolution, and debug mode.

Song object is an object that contains all the needed information about the song that is currently being rendered.
It contains the following information
- trackTitle: Title of the song
- trackNumber: The position the song is in within its album
- trackArtist: The artist the *performed* or *composed* the song
- trackAlbumArtist: The artist is not *always* the artist of the album.
- trackAlbum: The album the song is in
- trackLength: How long the song is. (IIRC it is in seconds)
- Art for the track is saved in `lib/temp/art.png`

---

### Already written functions
There are a decent amount of functions that you may use in the `lib/` folder.
You can import these by a simple `from lib import abcxyz`
Here is a basic breakdown of the various files and their functions

- **dropShadow.py**
  - hexToRGBA(hex)
    - You give hex (even with #) and it returns RGBA
  - apply(image, blurAmount, dropOffset(5,5), shadowColor('#000000'), shadowOpacity=1, dropZoom=1.5, returnImage=False)
    - This, as the nume suggests applies a drop shadow to the given image
    - **Image**
      - This is *either* a file path to the given image or a PIL image object
    - **blurAmount** is the amount of blur; the number is kinda arbitrary, higher number means more blur. Do not put it too high, the PIL gausian blur likes to freak out at very high numbers
    - **dropOffset** is the amount of pixels you want to offset the blur by.
    - **shadowColor** is the color of the blur you would want. Must be a hex value
    - **shadowOpacity**, this is currently not implemented.
    - **dropZoom** is how much larger you want the drop shadow. If it is too small, it will be entirely covered by the image you're trying to add it to.
- **gen_art.py**
  - This is basically a wrapper for dropShadow. You give it a file location of the album art (otherwise it assumes it is saved in `lib/temp/art.png`), it applies the drop shadow and returns an image clip.
  - It has all of the same args, but theyre named differently.
- **gen_thumb.py**
  - This makes thumbnails in the Radio theme. This will go away at some point and be rolled into the main radio theme folder
- **gen_video.py**
  - Legacy code of the old way to render videos
- **is_dark.py**
  - calc(debug_mode=False, imagePath=None)
  - reads `lib/temp/art.png` but should in the future take in a image path with the imagePath arg
  - The numbers on line 25 determine how sensitive/accuruate it is, change to your needs
- **myFunctions.py**
  - The functions here are smaller or fairly unimportant, but I judt don't want to keep rewriting
  - getRelativeRootDir():
    - gives the absolute path of the msuic2video folder path
  - hex_to_rgb(hex=None)
    - takes in hex, gives RGB, *not* RGBA
- **resize_art.py**
  - maintain_ratio(image_name, desired_size)
    - you give the file path of the image along with the new size that you want to give it.
    - It will save and replace the old one ising the file path that you gave it
    - returns nothing
- **song.py**
  - This is the object that hold all of the information about the song
- **string_clean.py**
  - clean(string)
    - takes sting and takes out any illegal chars that might cause problems when uploading to YouTube
- **unicode_search.py**
  - main(input)
    - runs reach with input
    - returns what rearch gives
  - search(input_string)
    - give a string, it breaks it into charaters and tells you which noto font you should use to support the language of the sting.
    - currently has a bug that just looks at the last character and uses what that was as an indicator for the language of the string.
      - But for 99% of the time, it works. Good enough I guess.

---

# Actually Making a Theme

You are going to have to import some (if not all) of the moviepy packages  

> `from moviepy.editor import *`

And importing the required custom functions. (such as gen_art if you want to show the art)

initialize the `make` function, it will have to take in `sonngObject`, `resolution` and `debug_mode`.

> ```
> from from moviepy.editor import *
> from lib import gen_art
>
> def make(sonngObject=None, resolution=(3840, 2160), debug_mode=False):
>   # Where you make the theme ...
> ```

Now, lets say you want to insert the album art

> ```  
>   # Cont. from above code ...
>   clip_art = gen_art.make(        # makes the clip
>        debug_mode = debug_mode,
>        artLocation = 'lib/temp/art.png')
>
>    # set position
>    clip_art = clip_art.set_position(('center', 'center'), relative=True)
> ```

Above, I both made the art clip and then set the position of the clip relative to the size of the resolution.  

Since the art clip is just a [ImageClip in moviepy](https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=imageclip#imageclip), you can use all of the same functions you can and would use on a normal one.
