from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import String

class Photo(SQLModel, table=True):
    __tablename__ = "photo" # type: ignore
    __table_args__ = {"extend_existing": True}

    photo_id: int = Field(default=None, primary_key=True)
    photo_base64: str = Field(sa_column=String(13300000))  # type: ignore # Máximo 10 MB en base64

    destination_id: int | None = Field(default=None, foreign_key="destination.destination_id")
    # destination: Destination | None = Relationship(back_populates="photos")
