import os
import uuid
import cv2
from pydantic import BaseModel
from werkzeug.utils import secure_filename
from ultralytics import YOLO
from flask import Flask, render_template, request, redirect, url_for
from sqlmodel import SQLModel, Field, Session ,create_engine

# Database
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str 
    username: str
    age: int
    city: str
    country: str
    password: str

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

# Data Validation
class UserModel(BaseModel):
    first_name: str
    last_name: str
    email: str 
    username: str
    age: int
    city: str
    country: str
    password: str


# Routes
app = Flask("Face Analysis App")

app.config["UPLOADS"] = "static/uploads"
app.config["RESULT_FOLDER"] = "static/results"

os.makedirs(app.config["UPLOADS"], exist_ok=True)
os.makedirs(app.config["RESULT_FOLDER"], exist_ok=True)

# Model
model = YOLO("yolo26n.pt")  # load an official model

# index
@app.route("/")
def root():
    return render_template("index.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        username = request.form.get("username")
        age = request.form.get("age")
        city = request.form.get("city")
        country = request.form.get("country")
        password = request.form.get("password")

        user_valid = UserModel(first_name, last_name, email, username, age, city, country, password)
        user = User(first_name, last_name, email, username, age, city, country, password)
        with Session(engine) as session:
            session.add(user)
            session.commit()
        
        return redirect(url_for("upload"))    
    
    return render_template("login.html")

# upload
@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":
        file = request.files.get("input_file")
        if not file or file.filename == "":
            return "No file selected"

        filename = secure_filename(file.filename)
        saved_path = os.path.join(app.config["UPLOADS"], filename)
        file.save(saved_path)

        return redirect(url_for("result", filename=filename))

    return render_template("upload.html")

# Result
@app.route("/result/<filename>")
def result(filename):
    saved_path = os.path.join(app.config["UPLOADS"], filename)

    results = model(saved_path)
    img = cv2.imread(saved_path)

    for res in results:
        boxes = res.boxes
        
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]

            label = f"{class_name} {conf:.2f}"

            if conf > 0.2:
                cv2.rectangle(img, (x1, y1), (x2, y2), (0,165,255), 2)
                (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
                cv2.rectangle(img, (x1, y1 - h - 10), (x1 + w, y1), (0,165,255), -1)
                cv2.putText(img, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)

    result_filename = f"{uuid.uuid4().hex}.png"
    result_path = os.path.join(app.config["RESULT_FOLDER"], result_filename)
    cv2.imwrite(result_path, img)

    return render_template("result.html", image=result_filename)

# BMR
@app.route("/bmr", methods=["GET", "POST"])
def bmr():
    if request.method == "POST":
        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))
        age = float(request.form.get("age"))
        gender = request.form.get("gender")

        if gender == "Male":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        elif gender == "Female":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

        return render_template("bmr.html", alert=True, bmr=bmr)
    
    return render_template("bmr.html")