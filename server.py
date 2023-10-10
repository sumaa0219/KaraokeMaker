import downloadYT
import makeJson
from flask import Flask, request, render_template, jsonify

dYT = downloadYT.downloadYT()
mkJson = makeJson.makejson()

app = Flask(__name__,template_folder='./html')

@app.route('/', methods=['GET'])
def root_func_get():
    return "Hello World!"

@app.route('/addlist', methods=['GET'])
def downloadFromYT():
    return render_template("add.html")

@app.route('/list', methods=['GET'])
def showlist():
    json = mkJson.getFileList()
    dYT
    print(json)
    
    return render_template("list.html")

@app.route('/search', methods=['POST']) #ダウンロード処理
def process():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # ここで必要な処理を行い、データを生成
        processed_data = dYT.search(user_input)
        title = []
        author = []
        url = []
        print(processed_data[0].url)
        for i in range(7):
            title.append(processed_data[i].title)
            author.append(processed_data[i].author)
            url.append(processed_data[i].url)
        print(title,author,url)
        
        # データをJSON形式でクライアントに返す
    return jsonify(processed_data)


        


app.run(host="0.0.0.0", port=80, debug=True)