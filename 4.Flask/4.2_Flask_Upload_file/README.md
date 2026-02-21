# Face Analysis Web App

A simple Flask-based web application that performs **face age analysis**
using DeepFace and also provides a **BMR (Basal Metabolic Rate)
calculator**.

![image](https://github.com/Moein-Moatali-2006/PyDeploy/blob/main/4.Flask/4.2_Flask_Upload_file/static/images/index.png)
![image](https://github.com/Moein-Moatali-2006/PyDeploy/blob/main/4.Flask/4.2_Flask_Upload_file/static/images/login.png)
![image](https://github.com/Moein-Moatali-2006/PyDeploy/blob/main/4.Flask/4.2_Flask_Upload_file/static/images/bmr.png)

## 🚀 Features

-   User registration (basic login form)
-   Image upload system
-   Face age prediction using DeepFace
-   BMR calculator (Mifflin-St Jeor equation)
-   SQLite database integration using SQLModel

## 🧠 Technologies Used

-   Python 3.x
-   Flask
-   DeepFace
-   SQLModel
-   SQLite
-   Werkzeug


## ▶️ Running the Application

``` bash
flask --app app.py run
```

Open in browser: http://127.0.0.1:5000/

## 🔹 Face Age Detection

Uses DeepFace:

``` python
DeepFace.analyze(
    img_path=saved_path,
    actions=["age"],
    enforce_detection=False
)
```

## 🔹 BMR Formula

For Men: BMR = (10 × weight) + (6.25 × height) - (5 × age) + 5

For Women: BMR = (10 × weight) + (6.25 × height) - (5 × age) - 161

## ⚠️ Notes

-   Educational project
-   Passwords stored as plain text (not secure)

## 👨‍💻 Author

Moein Moatali\
Computer Engineering Student\
Interested in AI & Backend Development
