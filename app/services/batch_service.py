from sqlalchemy.orm import Session
from app.repositories.batch_repositories import create_batch, get_batch, update_batch, delete_batch
from app.models.user import Batch,Course
from app.schemas import BatchCreate, BatchUpdate,BatchResponse

# Business logic for batch-related operations

def create_batch_service(db: Session, batch_data: BatchCreate):
    # Logic before creating a batch, if any
    new_batch = Batch(
        batch_start_date=batch_data.batch_start_date,
        batch_end_date=batch_data.batch_end_date,
        batch_strength=batch_data.batch_strength,
        course_id=batch_data.course_id
    )
    return create_batch(db, new_batch)

def get_batch_service(db: Session, batch_id: int):
    # Business logic, like access checks or logging can be added here
    batch = get_batch(db, batch_id)
    if batch:
        # You might need to fetch course details, depending on your use case
        course = db.query(Course).filter(Course.course_id == batch.course_id).first()
        if course:
            batch.course_id = course.course_id
    return batch

def update_batch_service(db: Session, batch_id: int, updated_data: BatchUpdate):
    # Business logic for updating a batch, if any
    updated_batch = update_batch(db, batch_id, updated_data.dict(exclude_unset=True))
    return updated_batch

def delete_batch_service(db: Session, batch_id: int):
    # Business logic before deletion, like checking for active enrollments
    deleted_batch = delete_batch(db, batch_id)
    return deleted_batch
