import glob
import random

def getImgPath():

    types = ('jpg', 'png', 'JPG')
    files = []
    paths = []
    for t in types:
        files += glob.glob('/home/takosuke/kitchenProject/app/static/img/*.' + t)

    for file in files:
        newfile = './' + files.split('app/')[-1]
        paths.append(newfile)

    random.shuffle(paths)

    print(paths)

    return paths
    