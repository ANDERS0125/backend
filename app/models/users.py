# models.py
from sqlmodel import SQLModel, Field

class UsersBase(SQLModel):
    name: str
    mail: str = Field(unique=True)

class Users(UsersBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str

class UsersCreate(UsersBase):
    password: str