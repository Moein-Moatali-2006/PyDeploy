from sqlalchemy.orm import Session
from .models import Student, Course

# Student CRUD: 
def create_student(db: Session, firstname: str, lastname: str, average: float, graduated: bool):
    student = Student(
        firstname = firstname,
        lastname = lastname,
        average = average,
        graduated = graduated
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def read_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is not None:
        return student 

def update_student(db: Session, student_id: int, firstname: str= None, lastname: str= None, average: float= None, graduated: bool= None):
    student = db.query(Student).filter(Student.id == student_id).first()

    if firstname is not None:
        student.firstname = firstname
    if lastname is not None:
        student.lastname = lastname
    if average is not None:
        student.average = average
    if graduated is not None:
        student.graduated = graduated
    
    db.commit()
    db.refresh(student)
    return student

def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    db.delete(student)
    db.commit()
    return {"Message": "Student deleted."}

# Course CRUD:
def create_course(db: Session, name: str, unit: int):
    course = Course(
        name = name,
        unit = unit
    )

    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def read_course(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is not None:
        return course

def update_course(db: Session,course_id: int, name: str= None, unit: int= None):
    course = db.query(Course).filter(Course.id == course_id).first()
    if name is not None:
        course.name = name
    if unit is not None:
        course.unit = unit

    db.commit()
    db.refresh(course)
    return course

def delete_course(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    db.delete(course)
    db.commit()
    return {"Message": "Course Deleted!"}