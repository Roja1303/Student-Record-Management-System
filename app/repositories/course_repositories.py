from sqlalchemy.orm import Session
from app.models.user import Course


def get_all_courses(db: Session):
    return db.query(Course).all()


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.course_id == course_id).first()

def create_course(db:Session, course: Course ):
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def update_course(db:Session, course_id:int, updated_data=dict):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if course:
        for key,value in updated_data.items():
            setattr(course,key,value)
        db.commit()
        db.refresh(course)
        return course
    return None

def delete_course(db:Session, course_id: int):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if course:
        db.delete(course)
        db.commit()
        return course

