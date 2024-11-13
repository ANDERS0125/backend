from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from app.models.users import Users, UsersCreate
from app.database.database import get_session
from app.services.user_service import (
    create_user_service,
    read_users_service,
    read_user_service,
    update_user_service,
    delete_user_service
)

router = APIRouter()

@router.post("/users/", response_model=Users)
def create_user(user: UsersCreate, session: Session = Depends(get_session)):
    return create_user_service(user, session)

@router.get("/users/", response_model=List[Users])
def read_users(session: Session = Depends(get_session)):
    return read_users_service(session)

@router.get("/users/{user_id}", response_model=Users)
def read_user(user_id: int, session: Session = Depends(get_session)):
    return read_user_service(user_id, session)

@router.put("/users/{user_id}", response_model=Users)
def update_user(user_id: int, user_data: UsersCreate, session: Session = Depends(get_session)):
    return update_user_service(user_id, user_data, session)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    return delete_user_service(user_id, session)