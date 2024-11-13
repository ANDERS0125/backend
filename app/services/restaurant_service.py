from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.restaurants import Restaurant

# Create restaurant
def create_restaurant_service(restaurant: Restaurant, session: Session):
    db_restaurant = session.exec(select(Restaurant).where(Restaurant.contact_info == restaurant.contact_info)).first()
    if db_restaurant:
        raise HTTPException(status_code=400, detail="Restaurant already exists")
    session.add(restaurant)
    session.commit()
    session.refresh(restaurant)
    return restaurant

# Read all restaurants
def read_restaurants_service(session: Session):
    return session.exec(select(Restaurant)).all()

# Read a restaurant by ID
def read_restaurant_service(restaurant_id: int, session: Session):
    restaurant = session.get(Restaurant, restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

# Read restaurants by destination ID
def read_restaurants_by_destination_service(destination_id: int, session: Session):
    return session.exec(select(Restaurant).where(Restaurant.destination_id == destination_id)).all()

# Update restaurant
def update_restaurant_service(restaurant_id: int, restaurant_data: Restaurant, session: Session):
    restaurant = session.get(Restaurant, restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    restaurant.contact_info = restaurant_data.contact_info
    restaurant.opening_hours = restaurant_data.opening_hours
    restaurant.destination_id = restaurant_data.destination_id
    session.add(restaurant)
    session.commit()
    session.refresh(restaurant)
    return restaurant

# Delete restaurant
def delete_restaurant_service(restaurant_id: int, session: Session):
    restaurant = session.get(Restaurant, restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    session.delete(restaurant)
    session.commit()
    return {"message": "Restaurant deleted successfully"}