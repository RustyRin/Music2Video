import cv2

'''
TODO
Make this take a file path string as an input, 
right now lib/temp/art.png should work

Should also add ability to be able to take in
a PIL image object as well as a string file path

The scale of the histogram should be tweaked
i think i fucked it a couple of times 
cause i wanted to force one gradient ot the other.
at lease put a comment on what the default should be
'''

def calc(debug_mode=False, imagePath=None):
    # read image
    img = cv2.imread('lib/temp/art.png')

    # makes a histogram of the grayscale
    histogram = cv2.calcHist([img], [0], None, [256], [0, 255])

    # dark art side              light art side     default: :200 0:
    if sum(histogram[:00]) > sum(histogram[256:]):
        if debug_mode:
            print('Detected dark art')
        return True     # dark
    else:
        if debug_mode:
            print('Detected light art')
        return False    # light
