from sqlalchemy.orm import Session
from app.repositories.course_repositories import create_course, get_course, update_course, delete_course
from app.models.user import Course
from app.schemas import CourseCreate, CourseUpdate,CourseResponse

# Business logic for course-related operations
def create_course_service(db: Session, course_data: CourseCreate):
    # Logic before creating a course, if any
    new_course = Course(
        course_name=course_data.course_name,
        course_category=course_data.course_category,
        course_fees=course_data.course_fees,
        course_duration=course_data.course_duration
    )
    return create_course(db, new_course)

def get_course_service(db: Session, course_id: int):
    # Business logic, like access checks or logging can be added here
    course = get_course(db, course_id)
    return course

def update_course_service(db: Session, course_id: int, updated_data: CourseUpdate):
    # Business logic for updating a course, if any
    updated_course = update_course(db, course_id, updated_data.dict(exclude_unset=True))
    return updated_course

def delete_course_service(db: Session, course_id: int):
    # Business logic before deletion, like checking for active enrollments
    deleted_course = delete_course(db, course_id)
    return deleted_course
