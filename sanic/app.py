import asyncio

from sanic import Sanic
from sanic import response

app = Sanic("My Hello, world app")
# app.config.ACCESS_LOG = False
# print(app.config.ACCESS_LOG)


@app.route('/')
async def test(request):
    await asyncio.sleep(2)
    return response.json({'hello': 'world'})
