from flask import Flask, request, url_for, redirect, render_template


app = Flask("Personal Website")

@app.route("/")
def root():
    return render_template("index.html")