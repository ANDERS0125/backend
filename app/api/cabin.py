
from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from app.models.cabin import Cabin
from app.database.database import get_session
from app.services.cabin_service import (
    create_cabin_service,
    read_cabins_service,
    read_cabin_service,
    read_cabins_by_destination_service,
    update_cabin_service,
    delete_cabin_service
)

router = APIRouter()

@router.post("/cabins/", response_model=Cabin)
def create_cabin(cabin: Cabin, session: Session = Depends(get_session)):
    return create_cabin_service(cabin, session)

@router.get("/cabins/", response_model=List[Cabin])
def read_cabins(session: Session = Depends(get_session)):
    return read_cabins_service(session)

@router.get("/cabins/{cabin_id}", response_model=Cabin)
def read_cabin(cabin_id: int, session: Session = Depends(get_session)):
    return read_cabin_service(cabin_id, session)

@router.get("/cabins/destination/{destination_id}", response_model=List[Cabin])
def read_cabins_by_destination(destination_id: int, session: Session = Depends(get_session)):
    return read_cabins_by_destination_service(destination_id, session)

@router.put("/cabins/{cabin_id}", response_model=Cabin)
def update_cabin(cabin_id: int, cabin_data: Cabin, session: Session = Depends(get_session)):
    return update_cabin_service(cabin_id, cabin_data, session)

@router.delete("/cabins/{cabin_id}")
def delete_cabin(cabin_id: int, session: Session = Depends(get_session)):
    return delete_cabin_service(cabin_id, session)