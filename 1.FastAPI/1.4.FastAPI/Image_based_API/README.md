# Image-Based FastAPI Application

**Author:** Moein Moatali  
**Location:** Mashhad, Iran

This project is a **FastAPI** application with three main features:
1. **Face Analysis** using DeepFace
2. **OCR for English and Persian text** using EasyOCR
3. **Object Detection** using YOLO11n

---

## Requirements

- Python 3.10+
- OpenCV
- EasyOCR
- Ultralytics YOLO
- DeepFace
- FastAPI
- Uvicorn (for running the server)
- NumPy

Install dependencies using pip:

```bash
pip install opencv-python easyocr ultralytics deepface fastapi uvicorn numpy
```

---

## Running the Application

```bash
uvicorn main:app --reload
```
> Note: The main file is assumed to be named `main.py`.

---

## Endpoints

### 1. Root Endpoint
```
GET /
```
- Returns a welcome message:
```json
{"Message": "Welcome to image based app ---> Face Analysis, OCR:English-Persian, Object detection."}
```

### 2. OCR
```
POST /OCR
```
- Input: Image file (`UploadFile`)
- Output: Detected text with bounding boxes and confidence
- Example output:
```json
{
  "results": [
    {
      "bbox": [[x1,y1],[x2,y2],[x3,y3],[x4,y4]],
      "text": "Sample Text",
      "confidence": 0.98
    }
  ]
}
```

### 3. Face Analysis
```
POST /FaceAnalysis
```
- Input: Image file (`UploadFile`)
- Output: Face attributes including gender, age, and emotions
- Example output:
```json
{
  "result": {
    "age": 25,
    "gender": "Man",
    "emotion": {"happy":0.7, "sad":0.1, ...}
  }
}
```

### 4. Object Detection
```
POST /ObjectDetection
```
- Input: Image file (`UploadFile`)
- Output: List of detected objects including class name, class ID, confidence, and bounding boxes
- Example output:
```json
{
  "detections": [
    {
      "class_id": 0,
      "class_name": "person",
      "confidence": 0.95,
      "bbox": [x1, y1, x2, y2]
    }
  ]
}
```

---

## Resources

- [EasyOCR GitHub](https://github.com/JaidedAI/EasyOCR)  
- [DeepFace GitHub](https://github.com/serengil/deepface)  
- [Ultralytics YOLO](https://www.ultralytics.com)

---

## Notes

- Ensure the YOLO model (`yolo11n.pt`) is available in the project directory.
- YOLO training data is in `coco8.yaml` and training is done for 3 epochs.
- This project was developed by **Moein Moatali** in Mashhad, Iran.

