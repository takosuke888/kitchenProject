# scraping-img-1.py
import urllib.request #拡張子のないURLから画像を保存
import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート
import csv

URL = 'https://cookpad.com/recipe/1519259' # URL入力
images = [] # 画像リストの配列]
classes = []


#class cockpadData():

    # title
    # author
    # main image

    # ingredients_length
    # ingredients_names
    # ingredients_amounts

    # step_length
    # step_text
    # step_image_paths


    

def getimages():

    soup = BeautifulSoup(requests.get(URL).content,'lxml') # bsでURL内を解析

    print(soup.find_all('img')) # 確認

    for link in soup.find_all('img'): # imgタグを取得しlinkに格納
        if link.get('src'): # imgタグ内の.jpgであるsrcタグを取得
            images.append(link.get('src'))
            classes.append(link.get('class'))

    with open('test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for i, img in enumerate(images):
            writer.writerow([i, classes[i], img])

    for i, url in enumerate(images):
        dl = urllib.request.urlopen(url).read()

        # ファイルへの保存
        save_name = 'img/' + str(i) + '.png'
        with open(save_name, 'wb') as f:
            f.write(dl)



def getIngredients():
    soup = BeautifulSoup(requests.get(URL).content,'lxml')
    ingredient_names = soup.findAll('div', class_='ingredient_name')
    ingradient_amounts = soup.findAll('div', class_='ingredient_quantity amount')
    for i, found in enumerate(ingredient_names):
        print(found.get_text(), ingradient_amounts[i].get_text())

def getStepTexts():
    soup = BeautifulSoup(requests.get(URL).content,'lxml')

    last = soup.find(class_='step_last')
    last_index = int(last['data-position'])

    texts = []

    # get step text
    step_texts = soup.findAll(class_='step_text')
    for i in range(last_index):
        texts.append(step_texts[i].get_text().replace('\n', ''))
    print(texts)

    img_paths = []

    # get step image
    steps = soup.findAll(class_='step')
    for i in range(last_index-1):
        if steps[i].find('img') is None:
            img_paths.append('none')
        else:
            img_paths.append(steps[i].find('img')['src'])
    last_step = soup.find(class_='step_last')
    if last_step.find('img') is None:
        img_paths.append('none')
    else:
        img_paths.append(last_step.find('img')['src'])

    print(img_paths)

def getMetaData():
    soup = BeautifulSoup(requests.get(URL).content,'lxml')
    title = soup.find(class_='recipe-title').get_text().replace('\n', '')
    author = soup.find(class_='author recipe_author_container').get_text().replace('\n', '')
    main_image_path = soup.find(class_='photo large_photo_clickable')['src']

getMetaData()