import asyncio

from asgiref.wsgi import WsgiToAsgi

from flask import Flask


app = Flask(__name__)


@app.route("/")
async def hello_world():
    await asyncio.sleep(2)
    return {"hello": "world"}


asgi_app = WsgiToAsgi(app)