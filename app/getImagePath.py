import glob
import random

def getImgPath():

    types = ('jpg', 'png', 'JPG')
    files = []
    for t in types:
        files += glob.glob('../static/img/*.' + t)

    random.shuffle(files)

    return files
    