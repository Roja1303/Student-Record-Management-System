from pydantic import BaseModel,EmailStr
from datetime import date, datetime
from typing import Optional

#User schema
class UserCreate(BaseModel):
    stud_id: int
    name:str
    date_of_birth:date
    city:str
    qualification:str
    email: EmailStr
    phone_no: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    qualification: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_no: Optional[str] = None

class UserResponse(BaseModel):
    stud_id: int
    name: str
    date_of_birth: date
    city: Optional[str]
    qualification: str
    email: EmailStr
    phone_no: str

    class Config:
        from_attributes = True


#Batch schema
class BatchCreate(BaseModel):
    batch_start_date: date
    batch_end_date: date
    batch_strength: int
    course_id: int

class BatchUpdate(BaseModel):
    batch_start_date: Optional[date] = None
    batch_end_date: Optional[date] = None
    batch_strength: Optional[int] = None

class BatchResponse(BaseModel):
    batch_id: int
    batch_start_date: date
    batch_end_date: date
    batch_strength: int
    course_id: int

    class Config:
        from_attributes = True


#course schema

class CourseCreate(BaseModel):
    course_id: int
    course_name: str
    course_category: str  # Can be Enum if using fixed values like 'core' and 'elective'
    course_fees: float
    course_duration: int

class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    course_category: Optional[str] = None

class CourseResponse(BaseModel):
    course_id: int
    course_name: str
    course_category: str# Can be Enum if using fixed values like 'core' and 'elective'
    course_fees: float
    course_duration: int

    class Config:
        from_attributes = True


# enrollment schemas
class EnrollmentCreate(BaseModel):
    stud_id: int
    course_id: int
    batch_id: int  # Use this as a model field with type annotation
    enrollment_date: date

class EnrollmentUpdate(BaseModel):
    enrollment_date: Optional[date] = None

class EnrollmentResponse(BaseModel):
    enrollment_id: int
    stud_id: int
    course_id: int
    batch_id: int  # Use this as a model field with type annotation
    enrollment_date: date

    class Config:
        from_attributes = True







