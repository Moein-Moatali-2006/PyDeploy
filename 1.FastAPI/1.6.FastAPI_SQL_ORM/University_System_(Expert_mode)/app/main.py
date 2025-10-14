from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .crud import create_student, update_student, read_student, delete_student
from .crud import create_course, update_course, read_course, delete_course
from .database import Base, SessionLocal, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Message": "Welcome to my university system!"}

@app.post("/student")
def student_create(firstname: str, lastname: str, average: float, graduated: bool, db: Session= Depends(get_db)):
    student = create_student(db, firstname, lastname, average, graduated)
    return student

@app.get("/student")
def student_read(student_id: int, db: Session= Depends(get_db)):
    student = read_student(db, student_id)
    return student

@app.put("/student")
def student_update(student_id: int, firstname: str= None, lastname: str= None,
                    average: float= None, graduated: bool= None, db: Session= Depends(get_db)):
    student = update_student(db, student_id, firstname, lastname, average, graduated)
    return student

@app.delete("/student")
def student_delete(student_id: int, db: Session= Depends(get_db)):
    student = delete_student(db, student_id)
    return student

@app.post("/course")
def course_create(name: str, unit: int, db: Session= Depends(get_db)):
    course = create_course(db, name, unit)
    return course

@app.get("/course")
def course_read(course_id: int, db: Session= Depends(get_db)):
    course = read_course(db, course_id)
    return course

@app.put("/course")
def course_update(course_id: int, name: str= None, unit: int= None, db: Session= Depends(get_db)):
    course = update_course(db, course_id, name, unit)
    return course

@app.delete("/course")
def course_delete(course_id: int, db: Session= Depends(get_db)):
    course = delete_course(db, course_id)
    return course

