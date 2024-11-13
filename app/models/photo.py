from sqlmodel import SQLModel, Field
from sqlalchemy import String


class Photo(SQLModel, table=True):
    photo_id: int = Field(default=None, primary_key=True)
    photo_base64: str = Field(sa_column=String(13300000))  # type: ignore # Máximo 10 MB en base64

    destination_id: int = Field(foreign_key="destination.destination_id")
