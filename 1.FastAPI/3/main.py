from typing import Union
import cv2
import numpy as np
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse
import io

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/salam")
def test():
    return "Alaic Salam"

@app.get("/salam/{firstname}/{lastname}")
def test2(firstname: str,lastname: str = "hoseini"):
    return "Alaic Salam " + firstname + " " + lastname

@app.get("/salam/{firstname}")
def test3(firstname: str,lastname: str = "hoseini"):
    return "Alaic Salam " + firstname + " " + lastname

@app.get("/tv-channel/{name}")
def test4(name: Union[str, int]):
    return {"name": name}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/create_image/{red}/{green}/{blue}")
def create_image(red: int ,green: int, blue: int):
    if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
        image = np.zeros((300, 200, 3), dtype=np.uint8)
        image[:,:] = (red, green, blue)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # cv2.imwrite("test.jpg",image)
        _, encoded_image = cv2.imencode(".png", image)

        return StreamingResponse(io.BytesIO(encoded_image.tobytes()), media_type="image/png")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                       detail="numbers must be between 0 and 255")