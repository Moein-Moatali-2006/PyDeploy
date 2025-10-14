# University System API (FastAPI + PostgreSQL)

A simple **University Management System** built with **FastAPI** and **SQLAlchemy**, using **PostgreSQL** as the database.  
This project demonstrates CRUD operations for **students** and **courses** with RESTful APIs.

---

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Docker Setup](#docker-setup)
- [Future Improvements](#future-improvements)

---

## Features

- Create, Read, Update, Delete **Students**
- Create, Read, Update, Delete **Courses**
- Database relations between students and courses
- RESTful API using **FastAPI**
- Automatic database table creation using **SQLAlchemy**

---

## Technologies

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker (optional)
- Uvicorn (for running FastAPI)

---

## Project Structure

```
project_root/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI application and routes
│   ├── models.py      # Database models (SQLAlchemy)
│   ├── crud.py        # CRUD operations
│   └── database.py    # Database configuration
│
├── Dockerfile
├── docker-compose.yml (optional)
└── requirements.txt
```

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd University_System_(Expert_mode)
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Make sure PostgreSQL is running (either locally or in Docker).

---

## Running the Application

### Without Docker

```bash
uvicorn app.main:app --reload
```

Open your browser at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
You can test all API endpoints using the **Swagger UI**.

---

### With Docker

#### Run PostgreSQL

```bash
docker run --name university-db \
  -e POSTGRES_USER=moein_user \
  -e POSTGRES_PASSWORD=moein_pass \
  -e POSTGRES_DB=university_db \
  -p 5432:5432 \
  -d postgres
```

#### Build and Run FastAPI

```bash
docker build -t university-api .
docker run -d -p 8000:8000 --name university-api --link university-db university-api
```

Open Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## API Endpoints

### Students
- `POST /student` → Create student
- `GET /student?student_id=<id>` → Read student
- `PUT /student` → Update student
- `DELETE /student` → Delete student

### Courses
- `POST /course` → Create course
- `GET /course?course_id=<id>` → Read course
- `PUT /course` → Update course
- `DELETE /course` → Delete course

---

## Future Improvements

- Use **Pydantic Schemas** for request/response validation
- Implement **many-to-many** relationship between students and courses
- Add **list endpoints** for all students and courses
- Add **user authentication** (JWT)
- Write **unit tests** using pytest

---

## Author

**Moein Moatali**  
GitHub: [Moein Moatali](https://github.com/Moein-Moatali-2006)

