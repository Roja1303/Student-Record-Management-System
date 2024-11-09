from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas import EnrollmentCreate, EnrollmentResponse, EnrollmentUpdate
from app.repositories.enrollment_repositories import  create_enrollment, get_enrollment_by_student_and_course, update_enrollment, delete_enrollment,get_all_enrollments
from app.services import enrollment_service
from app.services.enrollment_service import get_enrollment_service
from typing import List

router = APIRouter()


# Enroll a Student in a Course
@router.post("/enrollments/", response_model=EnrollmentResponse)
def create_enrollment_route(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    # Check if the student is already enrolled in the course
    existing_enrollment = get_enrollment_by_student_and_course(db, stud_id=enrollment.stud_id, course_id=enrollment.course_id)
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Student is already enrolled in this course.")

    # If not, create a new enrollment
    new_enrollment = enrollment_service.create_enrollment_service(db=db, enrollment_data=enrollment)
    return new_enrollment

@router.get("/enrollments/", response_model=List[EnrollmentResponse])
def get_batch_route(db: Session = Depends(get_db)):
    enrollments = get_all_enrollments(db)
    if not enrollments:
        raise HTTPException(status_code=404, detail="No batches found")
    return enrollments

# Get Enrollments for a Specific Student
@router.get("/enrollments/{enrollment_id}", response_model=EnrollmentResponse)
def read_student_enrollments_route(enrollment_id: int, db: Session = Depends(get_db)):
    # Fetch the enrollments by student ID
    enrollments = get_enrollment_service(db, enrollment_id=enrollment_id)
    if not enrollments:
        raise HTTPException(status_code=404, detail="No enrollments found for this student.")

    return enrollments


# Update an Enrollment
@router.put("/enrollments/{enrollment_id}", response_model=EnrollmentResponse)
def update_enrollment_route(enrollment_id: int, enrollment_data: EnrollmentUpdate, db: Session = Depends(get_db)):
    # Update the enrollment using the provided enrollment data
    updated_enrollment = update_enrollment(db=db, enrollment_id=enrollment_id,
                                           updated_data=enrollment_data.dict(exclude_unset=True))

    if not updated_enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found.")

    return updated_enrollment


# Delete an Enrollment
@router.delete("/enrollments/{enrollment_id}", response_model=EnrollmentResponse)
def delete_enrollment_route(enrollment_id: int, db: Session = Depends(get_db)):
    # Delete the enrollment by enrollment_id
    deleted_enrollment = delete_enrollment(db=db, enrollment_id=enrollment_id)

    if not deleted_enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found.")

    return deleted_enrollment
