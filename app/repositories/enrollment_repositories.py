from sqlalchemy.orm import Session
from app.models.user import Enrollment
from sqlalchemy.orm import Session
from app.models.user import Enrollment

def get_enrollment(db: Session, enrollment_id: int):
    return db.query(Enrollment).filter(Enrollment.enrollment_id == enrollment_id).first()

def get_all_enrollments(db: Session):
    enrollments = db.query(Enrollment).filter(Enrollment.enrollment_id != None).all()
    return enrollments

def get_enrollment_by_student_and_course(db: Session, stud_id: int, course_id: int):
    # Fetch all enrollments for a given student ID
    return db.query(Enrollment).filter(Enrollment.stud_id == stud_id,Enrollment.course_id == course_id).all()


def create_enrollment(db: Session, enrollment: Enrollment):
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return enrollment

def update_enrollment(db: Session, enrollment_id: int, updated_data=dict):
    enrollment = db.query(Enrollment).filter(Enrollment.enrollment_id == enrollment_id).first()
    if enrollment:
        for key, value in updated_data.items():
            setattr(enrollment, key, value)
        db.commit()
        db.refresh(enrollment)
    return enrollment

def delete_enrollment(db: Session, enrollment_id: int):
    enrollment = db.query(Enrollment).filter(Enrollment.enrollment_id == enrollment_id).first()
    if enrollment:
        db.delete(enrollment)
        db.commit()
        return enrollment
