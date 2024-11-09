from sqlalchemy.orm import Session
from app.models.user import Batch

def get_all_batches(db: Session):
    batches = db.query(Batch).filter(Batch.course_id != None).all()
    return batches

def get_batch(db: Session, batch_id: int):
    return db.query(Batch).filter(Batch.batch_id == batch_id).first()

def create_batch(db: Session, batch: Batch):
    db.add(batch)
    db.commit()
    db.refresh(batch)
    return batch

def update_batch(db: Session, batch_id: int, updated_data=dict):
    batch = db.query(Batch).filter(Batch.batch_id == batch_id).first()
    if batch:
        for key, value in updated_data.items():
            setattr(batch, key, value)
        db.commit()
        db.refresh(batch)
    return batch

def delete_batch(db: Session, batch_id: int):
    batch = db.query(Batch).filter(Batch.batch_id == batch_id).first()
    if batch:
        db.delete(batch)
        db.commit()
        return batch
