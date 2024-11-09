from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.repositories.course_repositories import get_all_courses, get_course, create_course, update_course, delete_course
from app.schemas import CourseResponse,CourseCreate,CourseUpdate
from app.services.course_service import create_course_service, get_course_service, update_course_service, delete_course_service
from typing import List

router = APIRouter()

@router.post("/courses/", response_model=CourseResponse)
def create_course_route(course: CourseCreate, db: Session = Depends(get_db)):
    existing_course = get_course(db, course.course_id)
    if existing_course:
        raise HTTPException(status_code=404, details="Course already exists with this code")
    new_course = create_course_service(db=db, course_data=course)  # Pass 'course' as 'course_data'
    return new_course


@router.get("/courses/", response_model=List[CourseResponse])
def read_courses_route(db: Session = Depends(get_db)):
    return get_all_courses(db)

@router.get("/courses/{course_id}", response_model = CourseResponse)
def read_course_route(course_id: int, db:Session = Depends(get_db)):
    course = get_course(db, course_id = course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/courses/{course_id}",response_model = CourseResponse)
def update_course_route(course_id:int, course_data:CourseUpdate, db:Session = Depends(get_db)):
    updated_course = update_course(db=db, course_id=course_id, updated_data=course_data.dict(exclude_unset=True))
    if not updated_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated_course

@router.delete("/courses/{course_id}", response_model = CourseResponse)
def delete_course_route(course_id:int, db: Session = Depends(get_db)):
    deleted_course = delete_course(db=db, course_id=course_id)
    if not deleted_course:
        raise HTTPException(status_code=404, details = "Course not found")
    return deleted_course