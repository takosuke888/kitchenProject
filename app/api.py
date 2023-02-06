from flask import Flask, request, make_response, render_template, url_for
import os
import cv2
import numpy as np
import subprocess, shlex

from . import scraping
from . import browser_call

api = Flask(__name__, static_folder='./static')

coockpad_data = scraping.cockpadData()

# スマホに表示する画面
@api.route('/', methods=['GET'])
def index():
    coockpad_data.clearData()
    return render_template('index.html')

# URLを受け取って、スクレイピング
@api.route('/post_url', methods=['POST'])
def recieve_url():

    # set last-index
    coockpad_data.step_last_index = int(request.form["index"])
    print(coockpad_data.step_last_index)

    url = request.form["field"]
    print(url)

    if url[-1] == '/':
        url = url[:-1]

    # URLが誤り
    if url.split('/')[-2] != 'recipe':
        print("INVALID URL")
        return render_template('index.html')

    # If save images
    #IMG_DIR = '/static/img/cookpad-recipe/' + url.split('/')[-1]
    #if not os.path.exists('app' + IMG_DIR):
    # ディレクトリが存在しない場合、ディレクトリを作成する
    #    os.makedirs('app' + IMG_DIR)

    # スクレイピング処理
    coockpad_data.scraping(url, "")
    print(coockpad_data.title)

    #open html in browser
    render_template('projection.html', data = coockpad_data)
    browser_call.call_browser('http://0.0.0.0:8000/projection')

    # スクレイピングが完了したら、PC側でブラウザを起動
    return render_template('index.html')
    
# プロジェクタ用の表示画面のURL
@api.route('/projection', methods=['GET'])
def projection():
    return render_template('projection.html', data = coockpad_data)



