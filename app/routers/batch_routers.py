from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas import BatchCreate, BatchUpdate, BatchResponse
from app.services.batch_service import create_batch_service, get_batch_service, update_batch_service, delete_batch_service
from app.repositories.batch_repositories import get_all_batches,get_batch,create_batch,update_batch,delete_batch
from app.models.user import Batch,Course
from typing import List

router = APIRouter()

@router.post("/batches/", response_model=BatchResponse)
def create_batch(batch: BatchCreate, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == batch.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    new_batch = Batch(
        batch_start_date=batch.batch_start_date,
        batch_end_date=batch.batch_end_date,
        batch_strength=batch.batch_strength,
        course_id=batch.course_id
    )
    db.add(new_batch)
    db.commit()
    db.refresh(new_batch)
    return new_batch


router.get("/batches/", response_model=List[BatchResponse])
def read_courses_route(db: Session = Depends(get_db)):
    return get_all_batches(db)


@router.get("/batches/{batch_id}", response_model=BatchResponse)
def get_batch_route(batch_id: int, db: Session = Depends(get_db)):
    batch = get_batch_service(db, batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return batch

@router.put("/batches/{batch_id}", response_model=BatchResponse)
def update_batch_route(batch_id: int, batch_data: BatchUpdate, db: Session = Depends(get_db)):
    updated_batch = update_batch_service(db, batch_id, batch_data)
    if not updated_batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return updated_batch

@router.delete("/batches/{batch_id}", response_model=BatchResponse)
def delete_batch_route(batch_id: int, db: Session = Depends(get_db)):
    deleted_batch = delete_batch_service(db, batch_id)
    if not deleted_batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return deleted_batch
