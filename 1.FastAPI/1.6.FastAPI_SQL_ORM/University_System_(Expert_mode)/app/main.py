from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .crud import create_student, update_student, read_student, delete_student
from .crud import create_course, update_course, read_course, delete_course
from .database import Base, SessionLocal, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    yield db
    db.close()

@app.get("/")
def read_root():
    return {"Message: ": "Welcome to my university system!"}

@app.post("/student")
def user_add(firstname: str, lastname: str, average: float, graduated: bool, db: Session= Depends(get_db)):
    student = create_student(db, firstname, lastname, average, graduated)
    return student



