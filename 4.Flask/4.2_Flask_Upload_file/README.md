# Face Analysis Flask App

A simple Flask web application that allows users to upload an image and
analyze facial age using DeepFace.

![index](static\images\index.png)
![login](static\images\login.png)

## 🚀 Features

-   User registration (basic email & password storage with SQLModel)
-   Image upload functionality
-   Facial age estimation using DeepFace
-   SQLite database integration
-   Clean Flask routing structure

## 🛠 Tech Stack

-   Python 3.11
-   Flask
-   DeepFace
-   SQLModel
-   SQLite

## 📂 Project Structure

    flask_app/
    │
    ├── app.py
    ├── database.db
    ├── templates/
    │   ├── index.html
    │   ├── login.html
    │   ├── upload.html
    │   └── result.html
    ├── uploads/
    └── README.md




    pip install -r requirements.txt

## ▶️ Running the Application

    flask --app app.py run

The app will run at:

    http://127.0.0.1:5000

## 📸 How It Works

1.  User submits email and password.
2.  User uploads an image.
3.  The image is analyzed using DeepFace.
4.  Estimated age is displayed on the result page.

## ⚠️ Notes

-   This project is for learning purposes.
-   Passwords are stored in plain text (not secure for production).
-   DeepFace and TensorFlow are resource-intensive.
-   Do not use the Flask development server in production.

## 🔮 Future Improvements

-   Add password hashing
-   Add user authentication sessions
-   Store uploaded images securely
-   Improve error handling
-   Use a production WSGI server (Gunicorn)
-   Optimize model loading for performance

## 📜 License

This project is for educational purposes only.
