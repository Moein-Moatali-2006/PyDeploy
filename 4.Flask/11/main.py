from flask import Flask, render_template, request


app = Flask("Test Prpject")


@app.route("/", methods=["GET"])
def my_root():
    name = "Moein"
    return render_template("index.html", name=name, x=10)

@app.route("/download", methods=["GET"])
def download():
    media = ["Image", "Music", "Movie"]
    return render_template("download.html", media=media)

@app.route("/me")
def my_information():
    my_info = {
        "firstname": "Moein",
        "email": "Moein@gmail.com"
    }
    return my_info

@app.route("/blog", methods=["GET", "POST"])
def blog():
    if request.method == "GET":
        return "This is GET method"
    elif request.method == "POST":
        return "This is POST method"