import cv2
import glob

types = ('jpg', 'png', 'JPG')
files = []
for t in types:
    files += glob.glob('./app/static/src/*.' + t)

for file in files:
    img = cv2.imread(file, 1)
    h = img.shape[0]
    w = img.shape[1]
    w2 = 1280
    h2 = round(h * 1280 / w )
    resized = cv2.resize(img, (w2, h2))
    filename = file.split('\\')[-1]
    newname = './app/static/img/' + filename
    cv2.imwrite(newname, resized)