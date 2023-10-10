import json
import os

class makejson():
    def __init__(self):
        self.baseDir = "audio"
        self.jsonName = "karaokeList.json"
        self.checkJson()
        with open(os.path.join(self.baseDir,self.jsonName), 'r', encoding="utf-8") as json_file:
            self.json = json.load(json_file)

    def checkJson(self):
        if not os.path.exists(os.path.join(self.baseDir,self.jsonName)):
            newJson = {}
            with open(os.path.join(self.baseDir,self.jsonName), 'w') as f:
                json.dump(newJson, f, indent=2)

    def getFileList(self):
        return self.json
    
    def addJson(self,Name,channelName):
        try: #一つ以上ある時
            keyList = list(self.json.keys())
            lastNum = keyList[-1]
            nextNum = int(lastNum) + 1
            nextNumStr = str(nextNum).zfill(4)
            newdict = {
                nextNumStr : {
                    "musicName" : Name,
                    "channeleName" : channelName
                }
            }
            self.json.update(newdict)
            with open(os.path.join(self.baseDir,self.jsonName), 'w') as f:
                json.dump(self.json, f, indent=2)

        except IndexError: #何もない時
            nextNumStr = "0001"
            newdict = {
                nextNumStr : {
                    "musicName" : Name,
                    "channeleName" : channelName
                }
            }
            with open(os.path.join(self.baseDir,self.jsonName), 'w') as f:
                json.dump(newdict, f, indent=2)

