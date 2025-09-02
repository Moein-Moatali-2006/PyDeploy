import cv2
import easyocr
import numpy as np

from deepface import DeepFace
from fastapi import FastAPI, HTTPException, UploadFile, status, File


app = FastAPI()
render = easyocr.Reader(["en", "fa"])

face_models = {
    "age": DeepFace.build_model("Age"),
    "gender": DeepFace.build_model("Gender"),
    "emotion": DeepFace.build_model("Emotion")
}

@app.get("/")
def read_root():
    return {"Message": "Welcome to image based app ---> Face Analysis, OCR:English-Persian, Object detection."}

# EasyOCR Repository in : https://github.com/JaidedAI/EasyOCR
@app.post("/OCR")
async def image_ocr(input_file: UploadFile= File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please post an image.")
    
    content = await input_file.read()
    np_array = np.frombuffer(content, dtype=np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
    if image is None:
        raise HTTPException(status_code=400, detail="Invalid image file.")

    result = render.readtext(image)
    parsed_result = []
    for bbox, text, prob in result:
        parsed_result.append({
            "bbox": [[int(x), int(y)] for x,y in bbox],
            "text": str(text),
            "confidence": float(prob)
        })
    return {"results": parsed_result}

# deepface repository in : https://github.com/serengil/deepface
@app.post("/FaceAnalysis")
async def image_face_analysis(input_file: UploadFile= File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please post an image.")
    
    content = await input_file.read()
    np_array = np.frombuffer(content, dtype=np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)

    result = DeepFace.analyze(
        img_path=image,
        actions=["gender", "age", "emotion"],             
        enforce_detection=False,
        detector_backend="opencv"
    )

    return {"result": result}