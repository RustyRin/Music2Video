import cv2

def calc(debug_mode=False):
    # read image
    img = cv2.imread('temp/art.png')

    # makes a histogram of the grayscale
    histogram = cv2.calcHist([img], [0], None, [256], [0, 255])

    # dark side              light side     default: :200 0:
    if sum(histogram[:150]) > sum(histogram[0:]):
        if debug_mode:
            print('Detected dark art')
        return True     # dark
    else:
        if debug_mode:
            print('Detected light art')
        return False    # light
