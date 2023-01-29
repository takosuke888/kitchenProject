# scraping-img-1.py
import urllib.request #拡張子のないURLから画像を保存
import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート
import csv

URL = 'https://cookpad.com/recipe/4993029/' # URL入力
images = [] # 画像リストの配列]
classes = []

def getimages():

    soup = BeautifulSoup(requests.get(URL).content,'lxml') # bsでURL内を解析

    print(soup.find_all("img")) # 確認

    for link in soup.find_all("img"): # imgタグを取得しlinkに格納
        if link.get("src"): # imgタグ内の.jpgであるsrcタグを取得
            images.append(link.get("src"))
            classes.append(link.get("class"))

    with open('test.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        for i, img in enumerate(images):
            writer.writerow([i, classes[i], img])

    for i, url in enumerate(images):
        dl = urllib.request.urlopen(url).read()

        # ファイルへの保存
        save_name = 'img/' + str(i) + '.png'
        with open(save_name, "wb") as f:
            f.write(dl)




soup = BeautifulSoup(requests.get(URL).content,'lxml')
found = soup.findAll('div', class_='ingredient_name')

print(len(found))