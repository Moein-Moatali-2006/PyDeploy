import io
import cv2
import numpy as np
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse


app = FastAPI()
coders = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def show_coders():
    return coders

@app.post("/items")
def add_coders(id: int = Form(), name: str = Form(), pose: str = Form()):
    coders[id] = {"name": name, "pos": pose}
    return coders[id]

@app.delete("/items/{id}")
def delete(id : int):
    if id not in coders:
        raise HTTPException(status_code=404, detail="Not found!")
    
    del coders[id]
    return {"Message: ": "Deleted! ✅ "}

@app.put("/items/{id}")
def update(id:int, name: str = Form(None), pose: str = Form(None)):
    if id not in coders:
        raise HTTPException(status_code=404, detail="Not found!")    
    
    if name is not None:
        coders[id]["name"] = name
    if pose is not None:
        coders[id]["pose"] = pose
    
    return coders[id]

@app.post("/convert2gray")
async def convert2gray(input_file: UploadFile = File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=404, detail="Not found!")
    
    contents = await input_file.read()
    np_array = np.frombuffer(contents, dtype=np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
    cv2.imwrite("output.png", image)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _ , encode = cv2.imencode(".png", image)
    bytes_image = encode.tobytes()

    return StreamingResponse(io.BytesIO(bytes_image), media_type="image/png")