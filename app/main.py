from fastapi import FastAPI
from app.api import users, admin, auth, destination
from app.database.database import init_db

app = FastAPI()

# Initialize the database
init_db()

# Include routers
app.include_router(users.router)
app.include_router(destination.router)
#app.include_router(admin.router)
#app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}
