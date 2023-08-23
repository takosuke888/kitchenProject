import glob

def getImgPath():

    types = ('jpg', 'png', 'JPG')
    files = []
    for t in types:
        file = glob.glob('./app/static/img/*.' + t)
        path = './' + file.split('.app/')[-1]
        files.append(path)
    return files
    