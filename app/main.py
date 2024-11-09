from fastapi import FastAPI
from app.routers import user_routers, batch_routers, course_routers, enrollment_routers
from app.database.db import engine
from app.models.user import Base

app = FastAPI()

# Register routers with prefixes
app.include_router(user_routers.router)  # Register user-related routes
app.include_router(batch_routers.router)  # Register batch-related routes with prefix
app.include_router(course_routers.router)  # Register course-related routes with prefix
app.include_router(enrollment_routers.router)  # Register enrollment-related routes with prefix

# Create the database tables at the start of the application (optional)
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
