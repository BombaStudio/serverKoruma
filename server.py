from asyncio.windows_events import NULL
from flask import Flask, render_template, request, send_from_directory,url_for
import json
import codecs
import os

app = Flask(__name__)

#region mainServer
def mainServer():
    @app.route("/")
    def index():
        return '<link rel="shortcut icon" href="{}">'.format(url_for('http://127.0.0.1:5000/static', filename='favicon.ico'))
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')
#endregion
def msgServer():
    @app.route("/msgData/", methods = ["GET", "POST"])
    def msgData():
        #region read msgData
        if request.method == "GET":
            aa = []
            with codecs.open("msgData.json", 'r+','utf-8')as f:
                data = json.load(f)
                for d in data:
                    aa.append(d)
            return str(aa)
        #endregion
        if request.method == "POST":
            data = {}
            with open("msgData.json", 'r+') as f:
                data = json.load(f)
                #region delete element from msgData 
                if request.form["process"] == "del":
                    try:
                        del data[request.form["uid"]]
                        with codecs.open("msgData.json", 'w','utf-8') as f:
                            f.write(str(data).replace("'",'"'))
                        return data
                    except:
                        return "this object is not found"
                #endregion
                #region change element from msgData
                if request.form["process"] == "change":
                    try:
                        data[request.form["uid"]]["msg"] = request.form["msg"]
                        data[request.form["uid"]]["tel"] = request.form["tel"]
                        with codecs.open("msgData.json", 'w','utf-8') as f:
                            f.write(str(data).replace("'",'"'))
                        with codecs.open("msgData.json", "r+", 'utf-8') as f:
                            data = json.load(f)
                        return data
                    except:
                        return "this object is not found"
                #endregion
                #region add element from msgData
                if request.form["process"] == "add":
                    try:
                        data[request.form["uid"]] = {
                            "msg": request.form["msg"],
                            "tel":request.form["tel"]
                        }
                        with codecs.open("msgData.json", 'w','utf-8') as f:
                            f.write(str(data).replace("'",'"'))
                        with codecs.open("msgData.json", "r+", 'utf-8') as f:
                            data = json.load(f)
                        return data
                    except:
                        return "this object is not found"
                #endregion
    #region read msgData's elements
    @app.route("/msgData/<string:room>/", methods = ["GET", "POST"])
    def msgDatas(room):
        if request.method == "GET":
            data = {}
            with open("msgData.json", "r+") as f:
                data = json.load(f)
            try:
                return data[room]
            except:
                return "this object is not found"
        if request.method == "POST":
            pass
    #endregion
def userServer():
    @app.route("/userData/", methods = ["GET", "POST"])
    def userData():
        #region read userData
        if request.method == "GET":
            aa = []
            with codecs.open("userData.json", 'r+','utf-8')as f:
                data = json.load(f)
                for d in data:
                    aa.append(d)
            return str(aa)
        #endregion
        if request.method == "POST":
            data = {}
            with open("userData.json", 'r+') as f:
                data = json.load(f)
                #region delete element from userData
                if request.form["process"] == "del":
                    try:
                        del data[request.form["uid"]]
                        with codecs.open("userData.json", 'w','utf-8') as f:
                            f.write(str(data).replace("'",'"'))
                        return data
                    except:
                        return "this object is not found"
                #endregion
                #region change element from userData
                if request.form["process"] == "change":
                    try:
                        data[request.form["uid"]]["tc"] = request.form["tc"]
                        data[request.form["uid"]]["isim"] = request.form["isim"]
                        data[request.form["uid"]]["soyisim"] = request.form["soyisim"]
                        data[request.form["uid"]]["dogum"] = request.form["dogum"]
                        data[request.form["uid"]]["il"] = request.form["il"]
                        data[request.form["uid"]]["ilce"] = request.form["ilce"]
                        data[request.form["uid"]]["ikametgah"] = request.form["ikametgah"]
                        data[request.form["uid"]]["tel"] = request.form["tel"]
                        with codecs.open("userData.json", 'w','utf-8') as f:
                            f.write(str(data).replace("'",'"'))
                        with codecs.open("userData.json", "r+", 'utf-8') as f:
                            data = json.load(f)
                        return data
                    except:
                        return "this object is not found"
                #endregion
                #region add element from userData
                if request.form["process"] == "add":
                    try:
                        data[request.form["uid"]] = {
                            "tc": request.form["tc"],
                            "isim":request.form["isim"],
                            "soyisim":request.form["soyisim"],
                            "dogum":request.form["dogum"],
                            "il":request.form["il"],
                            "ilce":request.form["ilce"],
                            "ikametgah":request.form["ikametgah"],
                            "tel":request.form["tel"],
                        }
                        with codecs.open("userData.json", 'w','utf-8') as f:
                            f.write(str(data).replace("'",'"'))
                        with codecs.open("userData.json", "r+", 'utf-8') as f:
                            data = json.load(f)
                        return data
                    except:
                        return "this object is not found"
                #endregion
                #endregion
    #region read userData's elements
    @app.route("/userData/<string:room>/", methods = ["GET", "POST"])
    def userDatas(room):
        if request.method == "GET":
            data = {}
            with open("userData.json", "r+") as f:
                data = json.load(f)
            try:
                return data[room]
            except:
                return "this object is not found"
        if request.method == "POST":
            pass
    #endregion
def locationServer():
    @app.route("/locationData/", methods = ["GET", "POST"])
    def locationData():
        #region read locationData
        if request.method == "GET":
            aa = []
            with codecs.open("locationData.json", 'r+','utf-8')as f:
                data = json.load(f)
                for d in data:
                    aa.append(d)
            return str(aa)
        #endregion
        if request.method == "POST":
            data = {}
            with open("locationData.json", 'r+') as f:
                data = json.load(f)
                #region delete element from locationData 
                if request.form["process"] == "del":
                    try:
                        del data[request.form["uid"]]
                        with codecs.open("locationData.json", 'w','utf-8') as f:
                            f.write(str(data).replace("'",'"'))
                        return data
                    except:
                        return "this object is not found"
                #endregion
                #region change element from locationData
                if request.form["process"] == "change":
                    try:
                        data[request.form["uid"]]["kor_x"] = request.form["kor_x"]
                        data[request.form["uid"]]["kor_y"] = request.form["kor_y"]
                        data[request.form["uid"]]["tel"] = request.form["tel"]
                        with codecs.open("locationData.json", 'w','utf-8') as f:
                            f.write(str(data).replace("'",'"'))
                        with codecs.open("locationData.json", "r+", 'utf-8') as f:
                            data = json.load(f)
                        return data
                    except:
                        return "this object is not found"
                #endregion
                #region add element from locationData
                if request.form["process"] == "add":
                    try:
                        data[request.form["uid"]] = {
                            "kor_x": request.form["kor_x"],
                            "kor_y": request.form["kor_y"],
                            "tel":request.form["tel"]
                        }
                        with codecs.open("locationData.json", 'w','utf-8') as f:
                            f.write(str(data).replace("'",'"'))
                        with codecs.open("locationData.json", "r+", 'utf-8') as f:
                            data = json.load(f)
                        return data
                    except:
                        return "this object is not found"
                #endregion
    #region read locationData's elements
    @app.route("/locationData/<string:room>/", methods = ["GET", "POST"])
    def locationDatas(room):
        if request.method == "GET":
            data = {}
            with open("locationData.json", "r+") as f:
                data = json.load(f)
            try:
                return data[room]
            except:
                return "this object is not found"
        if request.method == "POST":
            pass
    #endregion

def startServer():
    app.run(debug = True)

mainServer()
locationServer()
msgServer()
userServer()

if __name__ == '__main__':
    startServer()