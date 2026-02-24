import os
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, flash, session as flask_session
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pydantic import BaseModel


app = Flask("Face Analyze")
app.secret_key = "Secretkey man"
app.config["UPLOAD_FOLDER"] = "./uploads"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg"}

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    city: str = Field()
    username: str = Field()
    password: str = Field()

engine = create_engine("sqlite:///./database.db", echo=True)
SQLModel.metadata.create_all(engine)

# PyDantic models for request validation
class RegisterModel(BaseModel):
    city: str
    username: str
    password: str

class LoginModel(BaseModel):
    username: str
    password: str

def auth(email, passsword):
    if email == "Moein@gmail.com" and passsword == "1234":
        return True
    else:
        return False

def allowed_file(filename):
    return True 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html", a=2, b=3)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        try:
            login_model = LoginModel(
                username = request.form["username"],
                my_password = request.form["password"]
            )
        except:
            flash("Type Error", "warning")
            return redirect(url_for("login"))
        
        with Session(engine) as db_session:
            statement = select(User).where(User.username == login_model.username)
            user = db_session.exec(statement).first()
        
        if user:
            password_byte = LoginModel.password.encode("utf-8")
            if bcrypt.checkpw(password_byte, user.password):
                flash("welcome")
                flask_session["user_id"] = user.id
                return redirect(url_for("upload"))
            else:
                flash("Your password is incorrect")
                return redirect(url_for("login"))
        else:
            flash("Your username is incorrect")
            return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])     
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        try:
            register_data = RegisterModel(request.form["city"],
                                        request.form["username"],
                                            request.form["password"])
        except:
            flash("Type Error")
            return redirect(url_for("register"))

        with Session(engine) as db_session:
           statement = select(User).where(User.username == register_data.username)
           result = db_session.exec(statement).first()

        if not result:
            password_byte = register_data.password.encode("utf-8")
            hashed_password = bcrypt.hashpw(password_byte, bcrypt.gensalt())
            with Session(engine) as db_session:
                user = User(
                    city=register_data.city,
                    username=register_data.username,
                    password=hashed_password
                )
                db_session.add(user)
                db_session.commit()
            flash("Your register done succsesfully")
            return redirect(url_for("login"))
        else:
            flash("Username already exist. Try another username")
            return redirect(url_for("register"))
            
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if flask_session.get("user_id"):
        if request.method == "GET":
            return render_template("upload.html")
        elif request.method == "POST":

            my_image = request.files["image"]
            if my_image.filename == "":
                return redirect(url_for("upload"))
            else:
                if my_image and allowed_file(my_image.filename):
                    save_path = os.path.join(app.config["UPLOAD_FOLDER"], my_image.filename)
                    my_image.save(save_path)

                #     result = Deepface.analyze(
                #         img_path = save_path,
                #         actions = ["age"]
                #     )
                #     age = result[0]["age"]
                
                # return render_template("result.html", age=age)
    else:
        return redirect(url_for("index"))


@app.route("/logout")
def logout():
    flask_session.pop("user_id")
    return redirect(url_for("index"))