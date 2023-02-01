from flask import Flask, request, make_response, render_template, url_for
import os

from . import scraping

api = Flask(__name__, static_folder='./static')

coockpad_data = scraping.cockpadData()

# スマホに表示する画面
@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# URLを受け取って、スクレイピング
@api.route('/post_url', methods=['POST'])
def recieve_url():
    url = request.form["field"]
    print(url)

    if url[-1] == '/':
        url = url[:-1]

    # URLが誤り
    if url.split('/')[-2] != 'recipe':
        print("INVALID URL")
        return render_template('index.html')

    IMG_DIR = '/static/img/' + url.split('/')[-1]
    if not os.path.exists('app' + IMG_DIR):
    # ディレクトリが存在しない場合、ディレクトリを作成する
        os.makedirs('app' + IMG_DIR)

    # スクレイピング処理
    coockpad_data.scraping(url, IMG_DIR)
    print(coockpad_data.title)

    # スクレイピングが完了したら、PC側でブラウザを起動
    return render_template('index.html')
    
# プロジェクタ用の表示画面のURL
@api.route('/projection', methods=['GET'])
def projection():
    return render_template('projection.html', data = coockpad_data)
    
