
from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.cabin import Cabin

# Create cabin
def create_cabin_service(cabin: Cabin, session: Session):
    db_cabin = session.exec(select(Cabin).where(Cabin.cabin_id == cabin.cabin_id)).first()
    if db_cabin:
        raise HTTPException(status_code=400, detail="Cabin already exists")
    session.add(cabin)
    session.commit()
    session.refresh(cabin)
    return cabin

# Read all cabins
def read_cabins_service(session: Session):
    return session.exec(select(Cabin)).all()

# Read a cabin by ID
def read_cabin_service(cabin_id: int, session: Session):
    cabin = session.get(Cabin, cabin_id)
    if not cabin:
        raise HTTPException(status_code=404, detail="Cabin not found")
    return cabin

# Read cabins by destination ID
def read_cabins_by_destination_service(destination_id: int, session: Session):
    return session.exec(select(Cabin).where(Cabin.destination_id == destination_id)).all()

# Update cabin
def update_cabin_service(cabin_id: int, cabin_data: Cabin, session: Session):
    cabin = session.get(Cabin, cabin_id)
    if not cabin:
        raise HTTPException(status_code=404, detail="Cabin not found")
    cabin.cabin_type = cabin_data.cabin_type
    cabin.base_price = cabin_data.base_price
    cabin.destination_id = cabin_data.destination_id
    session.add(cabin)
    session.commit()
    session.refresh(cabin)
    return cabin

# Delete cabin
def delete_cabin_service(cabin_id: int, session: Session):
    cabin = session.get(Cabin, cabin_id)
    if not cabin:
        raise HTTPException(status_code=404, detail="Cabin not found")
    session.delete(cabin)
    session.commit()
    return {"message": "Cabin deleted successfully"}