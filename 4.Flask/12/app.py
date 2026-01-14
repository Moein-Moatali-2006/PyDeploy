from flask import Flask, render_template, request, redirect, session
import os
# import cv2


app = Flask("Analyze Face")
app.config["UPLOAD_FOLDER"] = "./uploads"
app.config["ALLOWED_EXTENTIONS"] = {".png", ".jpg", ".jpeg"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")