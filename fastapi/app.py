import asyncio

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    await asyncio.sleep(2)
    return {"Hello": "World"}
