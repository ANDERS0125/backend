from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from app.models.destinations import Destination
from app.database.database import get_session
from app.services.destination_service import (
    create_destinations_service,
    read_destinations_service,
    read_destination_service,
    update_destination_service,
    delete_destination_service
)

router = APIRouter()

@router.post("/destinations/", response_model=Destination)
def create_destination(destination: Destination, session: Session = Depends(get_session)):
    return create_destinations_service(destination, session)

@router.get("/destinations/", response_model=List[Destination])
def read_destinations(session: Session = Depends(get_session)):
    return read_destinations_service(session)

@router.get("/destinations/{destination_id}", response_model=Destination)
def read_destination(destination_id: int, session: Session = Depends(get_session)):
    return read_destination_service(destination_id, session)

@router.put("/destinations/{destination_id}", response_model=Destination)
def update_destination(destination_id: int, destination_data: Destination, session: Session = Depends(get_session)):
    return update_destination_service(destination_id, destination_data, session)

@router.delete("/destinations/{destination_id}")
def delete_destination(destination_id: int, session: Session = Depends(get_session)):
    return delete_destination_service(destination_id, session)