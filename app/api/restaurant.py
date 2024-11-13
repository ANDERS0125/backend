
from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from app.models.restaurants import Restaurant
from app.database.database import get_session
from app.services.restaurant_service import (
    create_restaurant_service,
    read_restaurants_service,
    read_restaurant_service,
    read_restaurants_by_destination_service,
    update_restaurant_service,
    delete_restaurant_service
)

router = APIRouter()

@router.post("/restaurants/", response_model=Restaurant)
def create_restaurant(restaurant: Restaurant, session: Session = Depends(get_session)):
    return create_restaurant_service(restaurant, session)

@router.get("/restaurants/", response_model=List[Restaurant])
def read_restaurants(session: Session = Depends(get_session)):
    return read_restaurants_service(session)

@router.get("/restaurants/{restaurant_id}", response_model=Restaurant)
def read_restaurant(restaurant_id: int, session: Session = Depends(get_session)):
    return read_restaurant_service(restaurant_id, session)

@router.get("/restaurants/destination/{destination_id}", response_model=List[Restaurant])
def read_restaurants_by_destination(destination_id: int, session: Session = Depends(get_session)):
    return read_restaurants_by_destination_service(destination_id, session)

@router.put("/restaurants/{restaurant_id}", response_model=Restaurant)
def update_restaurant(restaurant_id: int, restaurant_data: Restaurant, session: Session = Depends(get_session)):
    return update_restaurant_service(restaurant_id, restaurant_data, session)

@router.delete("/restaurants/{restaurant_id}")
def delete_restaurant(restaurant_id: int, session: Session = Depends(get_session)):
    return delete_restaurant_service(restaurant_id, session)