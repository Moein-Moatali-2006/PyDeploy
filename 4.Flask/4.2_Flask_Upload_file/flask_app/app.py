import os
from werkzeug.utils import secure_filename
from deepface import DeepFace
from flask import Flask, render_template, request, redirect, url_for
from sqlmodel import SQLModel, Field, Session ,create_engine

# Database
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str 
    password: str

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

# Routes
app = Flask("Face Analysis App")
app.config["UPLOADS"] = "../uploads/"

# index
@app.route("/")
def root():
    return render_template("index.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User(email=email, password=password)
        with Session(engine) as session:
            session.add(user)
            session.commit()
        
        return redirect(url_for("upload"))    
    
    return render_template("login.html")

# upload
@app.route("/upload", methods=["GET", "POST"])
def upload():
    global saved_path

    if request.method == "POST":
        file = request.files.get("input_file")

        filename = secure_filename(file.filename)
        saved_path = os.path.join(app.config["UPLOADS"], filename)
        file.save(saved_path)

        return redirect(url_for("result"))

    return render_template("upload.html")

# Result
@app.route("/result")
def result():
    info = DeepFace.analyze(
    img_path=saved_path,
    actions=["age"],
    enforce_detection=False)

    if isinstance(info, list):
        age = info[0]["age"]
    else:
        age = info["age"]

    return render_template("result.html", age=age)

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