from sqlmodel import SQLModel, Field


class Restaurant(SQLModel, table=True):
    restaurant_id: int = Field(default=None, primary_key=True)
    contact_info: str
    opening_hours: str = Field(default="")
    destination_id: int = Field(default=None, foreign_key="destination.destination_id")
