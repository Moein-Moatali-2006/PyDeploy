import datetime
from werkzeug.security import generate_password_hash
from flask import Flask, request, url_for, redirect, render_template
from sqlmodel import Session, select
from pydantic import BaseModel, ValidationError
from database import Contact, Register, make_database

app = Flask("Personal Website")
engine = make_database(True)

class RegisterModel(BaseModel):
    firstname: str
    lastname: str
    email: str
    username: str
    age: int
    city: str
    country: str
    password: str
    jointime: str

class LoginModel(BaseModel):
    username: str
    password: str

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
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            firstname = request.form.get("firstname")
            lastname = request.form.get("lastname")
            email = request.form.get("email")
            username = request.form.get("username")

            age = request.form.get("age")
            age = int(age) if age else None

            city = request.form.get("city")
            country = request.form.get("country")
            password = request.form.get("password")
            hashed_password = generate_password_hash(password)

            jointime = str(datetime.datetime.now())

            user = RegisterModel(
                firstname=firstname,
                lastname=lastname,
                email=email,
                username=username,
                age=age,
                city=city,
                country=country,
                password=hashed_password,
                jointime=jointime
            )

            user = Register(**user.dict())

            with Session(engine) as session:
                statement = select(Register).where(Register.username == username)
                existing_user = session.scalar(statement)

                if existing_user:
                    return render_template("register.html", username_exists=True)

                session.add(user)
                session.commit()
            
            return redirect(url_for("login"))

        except ValidationError as error:
            print(error.errors())
            return render_template("register.html")
    
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = LoginModel(
            username=request.form.get("username"),
            password=request.form.get("password")
        )

        ...

    return render_template("login.html")
