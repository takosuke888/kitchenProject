# scraping-img-1.py
import urllib.request #拡張子のないURLから画像を保存
import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート
import csv
import time


class cockpadData():

    def __init__(self):

        self.url = ""

        self.title = ""
        self.author = ""
        self.main_img_path = ""

        self.ingredient_length = 0
        self.ingredient_names = []
        self.ingredient_amounts = []

        self.step_length = 0
        self.step_last_index = 100
        self.step_texts = []
        self.step_img_paths = []

        self.static_step_img_paths = []
        self.static_main_img_path = ""

        self.imgDir = ""

    def checkURL():
        return False

    def scraping(self, url, imgdir, last_step = 100):
        self.url = url
        self.imgDir = imgdir
        self.step_last_index = last_step

        soup = BeautifulSoup(requests.get(self.url).content,'lxml')
        print("Access...", self.url)
        time.sleep(1)

        self.getMetaData(soup)
        self.getIngredients(soup)
        self.getSteps(soup)
        self.getimages()

    def getIngredients(self, soup):
        ingredient_names = soup.findAll('div', class_='ingredient_name')
        ingredient_amounts = soup.findAll('div', class_='ingredient_quantity amount')
        self.ingredient_length = len(ingredient_amounts)
        for i in range(len(ingredient_names)):
            self.ingredient_amounts.append(ingredient_amounts[i].get_text())
            self.ingredient_names.append(ingredient_names[i].get_text())

    def getSteps(self, soup):

        # get step text
        step_texts = soup.findAll(class_='step_text')

        self.step_length = min(len(step_texts), self.step_last_index)

        for i in range(self.step_length):
            self.step_texts.append(step_texts[i].get_text().replace('\n', ''))

        # get step image
        steps = soup.findAll(class_=['step','step_last'])
        for i in range(self.step_length):
            if steps[i].find('img') is None:
                self.step_img_paths.append('none')
            else:
                self.step_img_paths.append(steps[i].find('img')['src'])

    def getMetaData(self, soup):
        self.title = soup.find(class_='recipe-title').get_text().replace('\n', '')
        self.author = soup.find(class_='author recipe_author_container').get_text().replace('\n', '')
        self.main_img_path = soup.find(class_='photo large_photo_clickable')['src']

    

    def getimages(self):

        dl = urllib.request.urlopen(self.main_img_path).read()
        # ファイルへの保存
        save_name = 'app' + self.imgDir + '/main.png'
        self.static_main_img_path = '.' + self.imgDir + '/main.png'
        with open(save_name, 'wb') as f:
            f.write(dl)

        for i, url in enumerate(self.step_img_paths):
            if url == 'none':
                self.static_step_img_paths.append("none")
                continue
            dl = urllib.request.urlopen(url).read()
            time.sleep(1)
            # ファイルへの保存
            self.static_step_img_paths.append('.' + self.imgDir + '/step_' + str(i) + '.png')
            save_name = 'app' + self.imgDir + '/step_' + str(i) + '.png'
            with open(save_name, 'wb') as f:
                f.write(dl)
                
