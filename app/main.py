from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.api import users, destination, restaurant, photo, comment, cabin
from app.database.database import init_db
from app.security.auth import authenticate_user, create_access_token, get_current_user, get_current_admin
from datetime import timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize the database
init_db()

# Include routers
app.include_router(users.router)
app.include_router(destination.router)
app.include_router(restaurant.router)
app.include_router(photo.router)
app.include_router(comment.router)
app.include_router(cabin.router)
#app.include_router(admin.router)
#app.include_router(auth.router)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password) # type: ignore
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email, "user_type": user.user_type}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    user = get_current_user(token)
    return user

@app.get("/admin/me")
async def read_admin_me(token: str = Depends(oauth2_scheme)):
    admin = get_current_admin(token)
    return admin

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}
