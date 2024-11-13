from sqlmodel import SQLModel, Field


class Cabin(SQLModel, table=True):
    cabin_id: int | None = Field(default=None, primary_key=True)
    cabin_type: str
    base_price: float
    destination_id: int = Field(default=None ,foreign_key="destination.destination_id")
