import asyncio

import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def 