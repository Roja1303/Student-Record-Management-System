from fastapi import APIRouter,Depends,HTTPException
from  sqlalchemy.orm import Session
from app.database.db import get_db #This imports the get_db function from your database module, which typically creates and returns a new database session
from app.repositories.user_repositories import get_user, create_user, update_user, delete_user #Imports repository functions that handle the actual database operations for user management (CRUD operations)
from app.services import user_service  #Imports the user service module, which may contain business logic related to user management. This module acts as an intermediary between the API layer and the data layer (repositories).
from app.schemas import UserCreate, UserUpdate, UserResponse #Imports Pydantic models that define the structure of the request and response data. UserCreate and UserUpdate are used for creating and updating users, while UserResponse is used for the API response format.
from app.models.user import User
from typing import List


router = APIRouter()

@router.get("/users", response_model=List[UserResponse])
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()  # Get all users from the database
    return [UserResponse.from_orm(user) for user in users]  # Convert each User instance to UserResponse

@router.get("/users/{user_id}", response_model=UserResponse)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/",response_model=UserResponse)
def create_user_route(user:UserCreate,db:Session=Depends(get_db)):
    existing_user = get_user(db, user.stud_id)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    #new_user = User(**user.dict())
    return user_service.create_user_service(db=db, user_create=user)


@router.put("/users/{user_id}",response_model=UserResponse)
def update_user_route(user_id:int, user_data:UserUpdate, db:Session = Depends(get_db)):
    updated_user = update_user(db=db, user_id=user_id, updated_data=user_data.dict(exclude_unset = True) )# The exclude_unset=True option ensures that only the fields that were included in the update request are sent.
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}",response_model = UserResponse)
def delete_user_route(user_id:int,db:Session = Depends(get_db)):
    deleted_user = delete_user(db=db, user_id=user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user

