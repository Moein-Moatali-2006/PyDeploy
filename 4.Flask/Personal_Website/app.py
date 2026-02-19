import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, url_for, redirect, render_template, session
from sqlmodel import Session, select
from pydantic import BaseModel, ValidationError
from database import Contact, Register, make_database


app = Flask("Personal Website")
app.config["SECRET_KEY"] = "change_this_secret_key"

# Make databse: sqlite
engine = make_database(True)

# Models
class RegisterModel(BaseModel):
    firstname: str
    lastname: str
    email: str
    username: str
    age: int | None
    city: str
    country: str
    password: str
    jointime: datetime.datetime


class LoginModel(BaseModel):
    username: str
    password: str

# ----------     Routes     ---------- 
@app.route("/")
def root():
    return render_template("index.html")

# Contacts
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_message = Contact(
            phone=request.form.get("user_phone_number"),
            email=request.form.get("user_email"),
            text=request.form.get("user_text")
        )

        with Session(engine) as db:
            db.add(user_message)
            db.commit()

        return redirect(url_for("contact"))

    return render_template("contact.html")

# Register 
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            age = request.form.get("age")
            age = int(age) if age else None

            user_data = RegisterModel(
                firstname=request.form.get("firstname"),
                lastname=request.form.get("lastname"),
                email=request.form.get("email"),
                username=request.form.get("username"),
                age=age,
                city=request.form.get("city"),
                country=request.form.get("country"),
                password=generate_password_hash(request.form.get("password")),
                jointime=datetime.datetime.now()
            )

            with Session(engine) as db:
                statement = select(Register).where(Register.username == user_data.username)
                existing_user = db.scalar(statement)

                if existing_user:
                    return render_template("register.html", username_exists=True)

                new_user = Register(**user_data.dict())
                db.add(new_user)
                db.commit()

            return redirect(url_for("login"))

        except ValidationError:
            return render_template("register.html")

    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            user_data = LoginModel(
                username=request.form.get("username"),
                password=request.form.get("password")
            )

            with Session(engine) as db:
                statement = select(Register).where(Register.username == user_data.username)
                db_user = db.scalar(statement)

                if not db_user:
                    return render_template("login.html", login_error=True)

                if not check_password_hash(db_user.password, user_data.password):
                    return render_template("login.html", login_error=True)

                # Login success
                session["user_id"] = db_user.id
                session["username"] = db_user.username

                return redirect(url_for("root"))

        except ValidationError:
            return render_template("login.html", login_error=True)

    return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("root"))

# Blog
@app.route("/blog")
def blog():
    return render_template("blog.html")

