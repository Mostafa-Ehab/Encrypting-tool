from flask import Flask, render_template, request
import os
from datetime import datetime
from helper import PathControl

app = Flask(__name__)


@app.route("/")
def index():
    if request.method == "GET":
        if request.args.get("file"):
            base = request.args.get("file")
            if os.path.isdir(base):
                os.chdir(base)
            else:
                return "0"

        else:
            os.chdir("/")
        files = os.scandir()
        for i in str(os.getcwd()).split("/"):
            print(i)
        return render_template("index.html", head=files, base=os.getcwd(), files=files, datetime=datetime, os=os)

if __name__ == "__main__":
    app.run(host="192.168.152.128")
