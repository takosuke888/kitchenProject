import glob
import random

def getImgPath():

    types = ('jpg', 'png', 'JPG')
    files = []
    for t in types:
        files += glob.glob('/home/takosuke/kitchenProject/app/static/img/*.' + t)

    random.shuffle(files)

    return files
    