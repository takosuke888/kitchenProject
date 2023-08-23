from flask import Flask, request, make_response, render_template, url_for
import os
import sys

from . import scraping
from . import browser_call
from . import getImagePath

api = Flask(__name__, static_folder='./static')

recipe_data = scraping.recipeData()
youtube_url_tail = ''

# スマホに表示する画面
@api.route('/', methods=['GET'])
def index():
    recipe_data.clearData()
    return render_template('index.html')

# URLを受け取って、スクレイピング
@api.route('/post_url', methods=['POST'])
def recieve_url():

    recipe_data.clearData()

    # set last-index
    recipe_data.step_last_index = int(request.form["index"])
    print(recipe_data.step_last_index)

    url = request.form["field"]
    print(url)

    if recipe_data.checkURL(url) == False:
        print("INVALID URL")
        return render_template('index.html')

    # If save images
    #IMG_DIR = '/static/img/cookpad-recipe/' + url.split('/')[-1]
    #if not os.path.exists('app' + IMG_DIR):
    # ディレクトリが存在しない場合、ディレクトリを作成する
    #    os.makedirs('app' + IMG_DIR)

    # スクレイピング処理
    recipe_data.scraping()
    print(recipe_data.title)

    #open html in browser
    #render_template('projection.html', data = recipe_data)
    browser_call.call_selenium_browser('http://0.0.0.0:8000/projection')

    # スクレイピングが完了したら、PC側でブラウザを起動
    return render_template('index.html')

# URLを受け取って、youtube動画を埋め込む
@api.route('/post_youtube_url', methods=['POST'])
def recieve_youtube_url():

    global youtube_url_tail

    url = request.form["field"]
    print(url)
    
    if url[0:17] == 'https://youtu.be/':
        youtube_url_tail = url.split('https://youtu.be/')[-1]
    elif len(url.split('watch?v=') > 1):
        youtube_url_tail = url.split('watch?v=')[-1].split('&')[0]
    else:
        return 'Invalid URL'

    #open html in browser
    #render_template('projection_youtube.html', youtube_url_tail = youtube_url_tail)
    browser_call.call_selenium_browser('http://0.0.0.0:8000/projection_youtube')

    # スクレイピングが完了したら、PC側でブラウザを起動
    return render_template('index.html')

# URLを受け取って、youtube動画を埋め込む
@api.route('/get_imageviewer_request', methods=['GET'])
def get_imageviewer_request():
    browser_call.call_selenium_browser('http://0.0.0.0:8000/imageviewer')
    return render_template('index.html')

# プロジェクタ用のレシピ表示画面のURL
@api.route('/projection', methods=['GET'])
def projection_data():
    return render_template('projection.html', data = recipe_data)

# プロジェクタ用のYoutube表示画面のURL
@api.route('/projection_youtube', methods=['GET'])
def projection_youtube_data():
    #test
    return render_template('projection_youtube.html', youtube_url_tail = youtube_url_tail)

# プロジェクタ用の画像表示URL
@api.route('/imageviewer', methods=['GET'])
def projection_image():
    images = getImagePath.getImgPath()
    return render_template('projection_images.html', images = images)

# プロジェクタ用の黒画面表示画面のURL
@api.route('/black', methods=['GET'])
def projection_black():
    return render_template('black.html')

# プロジェクタ用の表示画面のURL
@api.route('/exit', methods=['GET'])
def exit_app():
    browser_call.close_window()
    return 'Thank you'




