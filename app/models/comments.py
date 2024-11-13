from sqlmodel import SQLModel, Field
from datetime import date


class Comments(SQLModel, table=True):
    comment_id: int = Field(default=None, primary_key=True)
    rating: int = Field(..., ge=1, le=5)  # Ensure rating is between 1 and 5
    comment: str = Field(default="")
    review_date: date = Field(default_factory=date.today)
    destination_id: int = Field(default=None, foreign_key="destination.destination_id")
    user_id: int = Field(default=None, foreign_key="usuario.user_id")
