
from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.photo import Photo

# Create photo
def create_photo_service(photo: Photo, session: Session):
    session.add(photo)
    session.commit()
    session.refresh(photo)
    return photo

# Read all photos
def read_photos_service(session: Session):
    return session.exec(select(Photo)).all()

# Read a photo by ID
def read_photo_service(photo_id: int, session: Session):
    photo = session.get(Photo, photo_id)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    return photo

# Update photo
def update_photo_service(photo_id: int, photo_data: Photo, session: Session):
    photo = session.get(Photo, photo_id)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    photo.photo_base64 = photo_data.photo_base64
    photo.destination_id = photo_data.destination_id
    session.add(photo)
    session.commit()
    session.refresh(photo)
    return photo

# Delete photo
def delete_photo_service(photo_id: int, session: Session):
    photo = session.get(Photo, photo_id)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    session.delete(photo)
    session.commit()
    return {"message": "Photo deleted successfully"}