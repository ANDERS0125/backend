
from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from app.models.photo import Photo
from app.database.database import get_session
from app.services.photo_service import (
    create_photo_service,
    read_photos_service,
    read_photo_service,
    update_photo_service,
    delete_photo_service
)

router = APIRouter()

@router.post("/photos/", response_model=Photo)
def create_photo(photo: Photo, session: Session = Depends(get_session)):
    return create_photo_service(photo, session)

@router.get("/photos/", response_model=List[Photo])
def read_photos(session: Session = Depends(get_session)):
    return read_photos_service(session)

@router.get("/photos/{photo_id}", response_model=Photo)
def read_photo(photo_id: int, session: Session = Depends(get_session)):
    return read_photo_service(photo_id, session)

@router.put("/photos/{photo_id}", response_model=Photo)
def update_photo(photo_id: int, photo_data: Photo, session: Session = Depends(get_session)):
    return update_photo_service(photo_id, photo_data, session)

@router.delete("/photos/{photo_id}")
def delete_photo(photo_id: int, session: Session = Depends(get_session)):
    return delete_photo_service(photo_id, session)