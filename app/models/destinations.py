from sqlmodel import SQLModel, Field


class Destination(SQLModel, table=True):
    destination_id: int | None = Field(default=None, primary_key=True)
    head_line: str = Field(default="")
    place_type: str = Field(default="")
    description: str = Field(default="")
    google_maps_url: str = Field(default="")
    full_address: str = Field(default="")
    status: str = Field(default="active")  # Expected values: 'active', 'disable'
