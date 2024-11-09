from http.client import HTTPException

from sqlalchemy.orm import Session
from app.repositories.user_repositories import create_user, get_user, update_user, delete_user
from app.schemas import UserCreate, UserUpdate, UserResponse
from app.models.user import User
from datetime import datetime


def create_user_service(db: Session, user_create: UserCreate) -> UserResponse:
    """
    Service function to create a new user. It checks for an existing user and creates a new one.
    """
    # Check if user with the same email already exists
    existing_user = get_user(db, user_create.stud_id)
    if existing_user:
        raise HTTPException(status_code=404, details="User with this ID already exists.")

    # If not, create a new user in the database
    user = User(**user_create.dict())
    created_user = create_user(db, user)
    return UserResponse.from_orm(created_user)


def get_user_service(db: Session, user_id: int) -> UserResponse:
    """
    Service function to retrieve a user by ID.
    """
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404,details="User not found.")
    return UserResponse.from_orm(user)


def update_user_service(db: Session, user_id: int, user_update: UserUpdate) -> UserResponse:
    """
    Service function to update a user's details.
    """
    updated_user = update_user(db, user_id, user_update.dict(exclude_unset=True))
    if not updated_user:
        raise HTTPException(status_code=404,details="User not found.")
    return UserResponse.from_orm(updated_user)


def delete_user_service(db: Session, user_id: int) -> UserResponse:
    """
    Service function to delete a user by ID.
    """
    deleted_user = delete_user(db, user_id)
    if not deleted_user:
        raise HTTPException(status_code=404,details="User not found.")
    return UserResponse.from_orm(deleted_user)
