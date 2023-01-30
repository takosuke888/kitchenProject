from flask import Flask, request, make_response, render_template, url_for


api = Flask(__name__, static_folder='./static')


# スマホに表示する画面
@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# URLを受け取って、スクレイピング
@api.route('/post_url', methods=['POST'])
def recieve_url():
    url = request.form["field"]
    print(url)
    # スクレイピング処理
    # スクレイピングが完了したら、PC側でブラウザを起動
    return render_template('index.html')
    
# プロジェクタ用の表示画面のURL
@api.route('/projection', methods=['GET'])
def projection():
    return render_template('projection.html')
    
