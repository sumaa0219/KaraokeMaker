import downloadYT
import makeJson
from flask import Flask, request, render_template, Response
import json
import subprocess
import os

dYT = downloadYT.downloadYT()
mkJson = makeJson.makejson()

baseDir = "assets"
karaokeDir = "audio"

def checkAssets():
    if not os.path.exists(os.path.join(baseDir)):
        os.mkdir(baseDir)

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
    page = ""
    try:
        for i in range(len(json)):
            num = str(i).zfill(4)
            pageSTR = f"""<div id='{num}' style="border: solid 2px"'>
                        <h2>{num}</h2>
                        <h2>{json[num]["musicName"]}</h2>
                        <h3>{json[num]["channeleName"]}</h3>
                        <img src={json[num]["thumbnail_url"]} height=270 width=495></img>
                    </div><br></br>"""
            page+=pageSTR
    except:
        page = "<h2>追加されている曲はありません</h2>"
    
    return render_template("list.html",page=page)

@app.route('/search', methods=['POST']) #ダウンロード処理
def process():
    if request.method == 'POST':
        print("get POST req")
        user_input = request.form['user_input']
        # ここで必要な処理を行い、データを生成
        processed_data = dYT.search(user_input)
        page = ""
        print(processed_data[0])
        for i in range(6):
            pageSTR = f"""<div id='{i}'>
                <img src='{processed_data[i]['thumbnail_url']}' height=270 width=495>
                <a href='#' onclick='sendGetRequest("{processed_data[i]['url']}")'>{processed_data[i]['title']}</a>
                <a>{processed_data[i]['author']}</a>
              </div>"""
            page += pageSTR
        # データをJSON形式でクライアントに返す
    return page

@app.route('/download', methods=['GET'])
def download():
    checkAssets()
    url = request.args.get('url')
    info = dYT.url_download(url,baseDir)
    print(info)
    mkJson.addJson(info["musicName"],info["musicAuthor"],info["thumbnail_url"])
    subprocess.run(['python', 'vocal-remover/inference.py', '--input',os.path.join(baseDir,info["musicName"]+".mp3"),"--output_dir",karaokeDir])
    os.remove(os.path.join(baseDir,info["musicName"]+".mp3"))
    dYT.convert_to_mp3(os.path.join(karaokeDir,info["musicName"]+".wav"),karaokeDir)

    return Response(response=json.dumps({'message': 'hello response'}), status=200)
        


app.run(host="0.0.0.0", port=5000, debug=True)