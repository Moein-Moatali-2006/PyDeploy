# FastAPI + SQLAlchemy User Management API

This project is a **simple User Management API** built with **FastAPI** and **SQLAlchemy**, using **SQLite** as the database.

---

## 🔹 Features
- Create a user
- Read a user by ID
- Update a user (optional fields: `name` and `email`)
- Delete a user
- Simple and clear structure, suitable for small or educational projects

---

## 📦 Requirements
- Python >= 3.10
- FastAPI
- SQLAlchemy
- Uvicorn (for running the server)

---

## ⚡ Installation and Running
1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app 
```

3. Access the API in your browser or Postman:
```
http://127.0.0.1:8000
```

4. Access automatic Swagger documentation:
```
http://127.0.0.1:8000/docs
```

---

## 📚 Database Structure
- Database: SQLite (`sql_app.db`)
- Table: `users`
- Columns:
  - `id` : Primary Key
  - `name` : User name
  - `email` : User email

---

## 📝 Endpoints

### 1. Home
```
GET /
```
- Response: Welcome message

### 2. Create User
```
POST /user
```
- Parameters: `name` (str), `email` (str)
- Response: Created user data

### 3. Read User
```
GET /users?user_id=<id>
```
- Response: User data by ID
- Error: 404 if user not found

### 4. Update User
```
PUT /users?user_id=<id>&new_name=<name>&new_email=<email>
```
- `new_name` and `new_email` are optional
- Only provided fields will be updated
- Response: Updated user data

### 5. Delete User
```
DELETE /users?user_id=<id>
```
- Response: Success message
- Error: 404 if user not found

---

## 💡 Notes
- Uses `SessionLocal` for database session management
- `flush` and `commit` are used to save changes to the database
- Simple and clear design for learning and practicing FastAPI and SQLAlchemy