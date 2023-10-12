import json
import os

class makejson():
    def __init__(self):
        self.baseDir = "audio"
        self.jsonName = "karaokeList.json"
        self.checkJson()

    def checkJson(self):
        if not os.path.exists(os.path.join(self.baseDir)):
            os.mkdir(self.baseDir)

        if not os.path.exists(os.path.join(self.baseDir,self.jsonName)):
            newJson = {}
            with open(os.path.join(self.baseDir,self.jsonName), 'w') as f:
                json.dump(newJson, f, indent=2)

    def getFileList(self):
        with open(os.path.join(self.baseDir,self.jsonName), 'r', encoding="utf-8") as json_file:
            self.json = json.load(json_file)
        return self.json
    
    def addJson(self,Name,channelName,thumbnail_url):
        print(Name,channelName)
        with open(os.path.join(self.baseDir,self.jsonName), 'r', encoding="utf-8") as json_file:
            self.json = json.load(json_file)
        try: #一つ以上ある時
            keyList = list(self.json.keys())
            lastNum = keyList[-1]
            nextNum = int(lastNum) + 1
            nextNumStr = str(nextNum).zfill(4)
            newdict = {
                nextNumStr : {
                    "musicName" : Name,
                    "channeleName" : channelName,
                    "thumbnail_url" : thumbnail_url
                }
            }
            self.json.update(newdict)
            with open(os.path.join(self.baseDir,self.jsonName), 'w',encoding="utf-8") as f:
                json.dump(self.json, f,ensure_ascii=False, indent=2)

        except IndexError: #何もない時
            nextNumStr = "0000"
            newdict = {
                nextNumStr : {
                    "musicName" : Name,
                    "channeleName" : channelName,
                    "thumbnail_url" : thumbnail_url
                }
            }
            with open(os.path.join(self.baseDir,self.jsonName), 'w') as f:
                json.dump(newdict, f,ensure_ascii=False, indent=2)

