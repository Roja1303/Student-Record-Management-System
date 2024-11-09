from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker # The specific session creation function or instance


DATABASE_URL = "postgresql://postgres:Roja%40Ambika1@localhost:5432/student_management"



engine = create_engine(DATABASE_URL)  #engine: Sets up a connection to the database.
Base = declarative_base()  #Base: Provides the blueprint for tables, so SQLAlchemy knows how they look.
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)  #SessionLocal: Creates new sessions to interact with the database whenever you want to add, update, or delete data.

def get_db():
    db = SessionLocal()  # Start a new session
    try:
        yield db  # Yield the session, providing it to the endpoint
    finally:
        db.close() # Close the session after the request finishes

