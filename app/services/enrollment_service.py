from sqlalchemy.orm import Session
from app.repositories.enrollment_repositories import create_enrollment, get_enrollment, update_enrollment, delete_enrollment
from app.models.user import Enrollment
from app.schemas import EnrollmentCreate, EnrollmentUpdate

# Business logic for enrollment-related operations

def create_enrollment_service(db: Session, enrollment_data: EnrollmentCreate):
    # Logic before creating an enrollment, if any
    new_enrollment = Enrollment(**enrollment_data.dict())
    return create_enrollment(db, new_enrollment)

def get_enrollment_service(db: Session, enrollment_id: int):
    # Business logic, like access checks or logging can be added here
    enrollment = get_enrollment(db, enrollment_id)
    return enrollment

def update_enrollment_service(db: Session, enrollment_id: int, updated_data: EnrollmentUpdate):
    # Business logic for updating an enrollment, if any
    updated_enrollment = update_enrollment(db, enrollment_id, updated_data.dict(exclude_unset=True))
    return updated_enrollment

def delete_enrollment_service(db: Session, enrollment_id: int):
    # Business logic before deletion, like checking if the enrollment exists
    deleted_enrollment = delete_enrollment(db, enrollment_id)
    return deleted_enrollment
