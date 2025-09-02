import io
import cv2
import easyocr
import numpy as np

from ultralytics import YOLO
from deepface import DeepFace
from fastapi import FastAPI, HTTPException, UploadFile, status, File


app = FastAPI()
render = easyocr.Reader(["en", "fa"])

# Set YOLO dependencies
model_object_detection = YOLO("yolo11n.pt")
result_object_detection = model_object_detection.train(data="coco8.yaml", epochs=3)
result_object_detection = model_object_detection.val()

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

# YOLO11n in : https://www.ultralytics.com
@app.post("/ObjectDetection")
async def image_object_detection(input_file: UploadFile= File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please post an image.")
    
    content = await input_file.read()
    np_array = np.frombuffer(content, dtype=np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)

    results = model_object_detection(image)[0]
    detections = []
    for box in results.boxes:
        detections.append({
            "class_id": int(box.cls[0]),
            "class_name": results.names[int(box.cls[0])],
            "confidence": float(box.conf[0]),
            "bbox": box.xyxy[0].tolist()  
        })

    return {"detections": detections}