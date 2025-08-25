# FastAPI To-Do App

This project is a simple **To-Do application** built with [FastAPI](https://fastapi.tiangolo.com/) and [aiosqlite](https://aiosqlite.omnilib.dev/en/stable/).  
It provides CRUD operations (Create, Read, Update, Delete) for managing tasks stored in a SQLite database.

---

## Features

- ✅ Create a task with title, description, time, and status  
- 📖 Read all tasks from the database  
- ✏️ Update an existing task by ID  
- ❌ Delete a task by ID  

---

## Requirements

Make sure you have Python 3.8+ installed.  
Then install dependencies:

```bash
pip install fastapi uvicorn aiosqlite
```

---

## How to Run

Run the FastAPI app using Uvicorn:

```bash
uvicorn main:app --reload
```

The app will be available at:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints

### Root
- **GET /** → Welcome message

### Tasks
- **GET /task** → Get all tasks  
- **POST /task** → Add a new task  
  - Params: `title`, `description`, `time`, `status`  
- **PUT /task** → Update an existing task by ID  
  - Params: `id`, `title`, `description`, `time`, `status`  
- **DELETE /task** → Delete a task by ID  
  - Params: `id`

---

## Database Schema

Before running the app, create the SQLite database with the following schema:

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    time TEXT,
    status INTEGER
);
```

---

## Example Request (via cURL)

```bash
# Add a new task
curl -X POST http://127.0.0.1:8000/task -F "title=Study" -F "description=Read ML book" -F "time=2025-08-25" -F "status=0"

# Get all tasks
curl http://127.0.0.1:8000/task

# Update a task
curl -X PUT http://127.0.0.1:8000/task -F "id=1" -F "title=Study Math" -F "description=Read algebra" -F "time=2025-08-26" -F "status=1"

# Delete a task
curl -X DELETE http://127.0.0.1:8000/task -F "id=1"
```

---

## Notes

- The app uses SQLite (`todo.db`) as the database.  
- Form data is used for POST, PUT, and DELETE requests.  
- Error handling is included for invalid IDs.  

---

## Author

Developed by **Moien Moatali**
