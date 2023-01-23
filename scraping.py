# scraping-img-1.py
import urllib.request #拡張子のないURLから画像を保存
import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート

URL = 'https://cookpad.com/recipe/4993029/' # URL入力
images = [] # 画像リストの配列

soup = BeautifulSoup(requests.get(URL).content,'lxml') # bsでURL内を解析

print(soup.find_all("img")) # 確認

for link in soup.find_all("img"): # imgタグを取得しlinkに格納
    if link.get("src"): # imgタグ内の.jpgであるsrcタグを取得
        images.append(link.get("src").split('.png')[0]) # imagesリストに格納



# urlopen


url = 'https://img.cpcdn.com/steps/24575634/m/585a7c13f704aea125df3b176a4638c2?u=3501781&amp;p=1523845646'
# urlの処理
dl = urllib.request.urlopen(url).read()

# ファイルへの保存
save_name = "a.png"
with open(save_name, "wb") as f:
    f.write(dl)