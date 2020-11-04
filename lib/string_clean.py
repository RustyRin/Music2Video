'''
this takes in a string and adds \ to any illegal characters so it can be
uploaded to YouTube through the uploader
'''

illegal = ['<', '>', '/', '\\', '\'', '\"']

def clean(string):
    for c in string:
        if c in illegal:
            string = string.replace(c, '')

    return string
