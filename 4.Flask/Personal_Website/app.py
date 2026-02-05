from flask import Flask, request, url_for, redirect, render_template
from sqlmodel import Session
from database import Contact, Register, make_database

app = Flask("Personal Website")
engine = make_database(True)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        user_message = Contact(
            phone=request.form["user_phone_number"],
            email=request.form["user_email"],
            text=request.form["user_text"]
        )

        with Session(engine) as session:
            session.add(user_message)
            session.commit()
        
        return redirect(url_for("contact"))
