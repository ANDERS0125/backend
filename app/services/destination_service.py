
from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.destinations import Destination

def create_destinations_service(destination: Destination, session: Session):
    session.add(destination)
    session.commit()
    session.refresh(destination)
    return destination

def read_destinations_service(session: Session):
    return session.exec(select(Destination)).all()

def read_destination_service(destination_id: int, session: Session):
    destination = session.get(Destination, destination_id)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    return destination

def update_destination_service(destination_id: int, destination_data: Destination, session: Session):
    destination = session.get(Destination, destination_id) 
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    destination.name = destination_data.head_line
    destination.description = destination_data.description
    destination.placeType = destination_data.place_type
    destination.googleMaps_url = destination_data.google_maps_url
    destination.full_addres = destination_data.full_address
    session.add(destination)
    session.commit()
    session.refresh(destination)
    return destination

# function to delete destination
def delete_destination_service(destination_id: int, session: Session):
    destination = session.get(Destination, destination_id)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    session.delete(destination)
    session.commit()