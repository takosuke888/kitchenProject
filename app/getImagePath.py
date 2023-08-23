import glob

def getImgPath():

    types = ('jpg', 'png', 'JPG')
    files = []
    paths = []
    for t in types:
        files += glob.glob('./app/static/img/*.' + t)
        
    for file in files:
        path = './' + file.split('./app/')[-1]
        paths.append(path)
    
    print(paths)

    return paths
    