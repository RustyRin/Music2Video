import os

'''
These are functions that are used in multiple files
but are small or not *important* enought to warrent their own file
'''

def getRelativeRootDir():
    return os.path.abspath(str(os.getcwd))

def hex_to_rgb(hex=None):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))