#Data access layer

from sqlalchemy import Column,Integer,String,Date,DateTime,CHAR,Enum,Numeric,ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base


class User(Base):
    __tablename__ = "users"

    stud_id = Column(Integer,primary_key=True, index=True)
    name = Column(String, index=True)
    date_of_birth = Column(Date)
    city = Column(String, index=True)
    qualification = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_no = Column(String, unique= True, index=True)  # If phone_No is intended to store long phone numbers, it's often better to store it as a String to handle numbers with country codes, leading zeros, or other formatting options.

    enrollments = relationship("Enrollment", back_populates ="student")


class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer,primary_key=True, index=True)
    course_name = Column(String, index=True)
    course_category = Column(String, index=True)
    course_fees = Column(Numeric(10,2))
    course_duration = Column(Integer,index=True)

    course_enrolls= relationship("Enrollment",back_populates="course")

class Batch(Base):
    __tablename__= "batch"

    batch_id = Column(Integer,primary_key=True,index=True)
    batch_start_date = Column(Date)
    batch_end_date = Column(Date)
    batch_strength = Column(Integer)
    course_id = Column(Integer,ForeignKey('courses.course_id'), index=True)

    batch_enrolls = relationship("Enrollment",back_populates="batch")

class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer,primary_key=True,index=True)
    stud_id = Column(Integer,ForeignKey("users.stud_id"),index=True)
    batch_id = Column(Integer,ForeignKey("batch.batch_id"),index=True)
    course_id = Column(Integer,ForeignKey('courses.course_id'),index=True)
    enrollment_date = Column(DateTime)

    student = relationship("User",back_populates="enrollments")
    course = relationship("Course",back_populates="course_enrolls")
    batch = relationship("Batch",back_populates="batch_enrolls")
