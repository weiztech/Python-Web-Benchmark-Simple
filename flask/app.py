from time import sleep

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    sleep(2)
    return {"hello": "world"}
