#import urllib.request #拡張子のないURLから画像を保存
import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート
import csv
import time


class recipeData():

    def __init__(self):

        self.url = ""

        self.service_name = ""

        self.title = ""
        self.author = ""
        
        self.service_name = ""

        self.ingredient_length = 0
        self.ingredient_names = []
        self.ingredient_amounts = []

        self.step_length = 0
        self.step_last_index = 100
        self.step_texts = []

        self.step_img_paths = []
        self.main_img_path = ""
        self.main_video_path = ""

    def clearData(self):
        self.url = ""
        self.service_name = ""
        self.title = ""
        self.author = ""
        self.ingredient_length = 0
        self.ingredient_names = []
        self.ingredient_amounts = []
        self.step_length = 0
        self.step_last_index = 100
        self.step_texts = []
        self.step_img_paths = []
        self.main_img_path = ""
        self.main_video_path = ""

    def checkURL(self, url):
        self.url = url

        if url.split('/')[2] == 'delishkitchen.tv':
            self.service_name = 'dk'
            return True
        elif url.split('/')[2] == 'cookpad.com':
            self.service_name = 'cp'
            return True
        else:
            return False

    def scraping(self):

        soup = BeautifulSoup(requests.get(self.url).content,'lxml')
        print("Access...", self.url)
           
        time.sleep(1)

        if self.service_name == 'cp':
            self.cp_getMetaData(soup)
            self.cp_getIngredients(soup)
            self.cp_getSteps(soup)

        elif self.service_name == 'dk':
            self.dk_getMetaData(soup)
            self.dk_getIngredients(soup)
            self.dk_getSteps(soup)

    #cookpad
    def cp_getIngredients(self, soup):
        ingredient_names = soup.find_all('div', class_='ingredient_name')
        ingredient_amounts = soup.find_all('div', class_='ingredient_quantity amount')
        self.ingredient_length = len(ingredient_amounts)
        for i in range(len(ingredient_names)):
            self.ingredient_amounts.append(ingredient_amounts[i].get_text())
            self.ingredient_names.append(ingredient_names[i].get_text())

    #cookpad
    def cp_getSteps(self, soup):

        # get step text
        step_texts = soup.find_all(class_='step_text')
        self.step_length = min(len(step_texts), self.step_last_index)
        for i in range(self.step_length):
            self.step_texts.append(step_texts[i].get_text().replace('\n', ''))

        # get step image
        steps = soup.find_all(class_=['step','step_last'])
        for i in range(self.step_length):
            if steps[i].find('img') is None:
                self.step_img_paths.append('none')
            else:
                self.step_img_paths.append(steps[i].find('img')['src'])

    #cookpad
    def cp_getMetaData(self, soup):
        self.title = soup.find(class_='recipe-title').get_text().replace('\n', '')
        self.author = soup.find(class_='author recipe_author_container').get_text().replace('\n', '')
        self.main_img_path = soup.find(class_='photo large_photo_clickable')['src']
    
    # Delish kitchen
    def dk_getIngredients(self, soup):
        ingredient_names = soup.find_all(class_='ingredient-name')
        ingredient_amounts = soup.find_all(class_='ingredient-serving')
        self.ingredient_length = len(ingredient_amounts)
        for i in range(len(ingredient_names)):
            self.ingredient_amounts.append(ingredient_amounts[i].get_text())
            self.ingredient_names.append(ingredient_names[i].get_text())

    # Delish kitchen
    def dk_getSteps(self, soup):

        # get step text
        step_texts = soup.find_all(class_='step-desc')
        self.step_length = min(len(step_texts), self.step_last_index)

        for i in range(self.step_length):
            self.step_texts.append(step_texts[i].get_text().replace('\n', ''))

        # get step image
        steps = soup.find_all(class_=['step','step_last'])
        for i in range(self.step_length):
            if steps[i].find('img') is None:
                self.step_img_paths.append('none')
            else:
                self.step_img_paths.append(steps[i].find('img')['src'])

    # Delish kitchen
    def dk_getMetaData(self, soup):
        self.title = soup.select_one('h1.title').get_text().replace('\n', '') #セレクタを使用　<tag>.<class> (スペース不要)
        self.author = soup.select_one('p.name').get_text().replace('\n', '')
        videos = soup.find_all('source')
        for v in videos:
            if v.get('src') is not None: #srcを持たない要素はNoneとして抽出されている。
                if v.get('src')[-3:] == 'mp4':
                    self.main_video_path = v.get('src')

