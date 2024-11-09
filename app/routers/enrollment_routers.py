from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas import EnrollmentCreate, EnrollmentResponse, EnrollmentUpdate
from app.repositories.enrollment_repositories import create_enrollment, get_enrollment, update_enrollment, \
    delete_enrollment, get_enrollments_by_student
from app.services import enrollment_service
from typing import List

router = APIRouter()


# Enroll a Student in a Course
@router.post("/enrollments/", response_model=EnrollmentResponse)
def create_enrollment_route(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    # Check if the student is already enrolled in the course
    existing_enrollment = get_enrollment(db, student_id=enrollment.stud_id, course_id=enrollment.course_id)
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Student is already enrolled in this course.")

    # If not, create a new enrollment
    new_enrollment = enrollment_service.create_enrollment_service(db=db, enrollment=enrollment)
    return new_enrollment


# Get Enrollments for a Specific Student
@router.get("/students/{student_id}/enrollments", response_model=List[EnrollmentResponse])
def read_student_enrollments_route(student_id: int, db: Session = Depends(get_db)):
    # Fetch the enrollments by student ID
    enrollments = get_enrollments_by_student(db, student_id=student_id)
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
