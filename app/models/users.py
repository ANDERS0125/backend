# models.py
from sqlmodel import SQLModel, Field
from datetime import date
from enum import Enum

class UserType(str, Enum):
    client = "client"
    admin = "admin"

class UsersBase(SQLModel):
    name: str
    last: str
    email: str = Field(unique=True)
    phone: str
    user_type: UserType
    direccion: str

class Users(UsersBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    registration_date: date = Field(default_factory=date.today)

class UsersCreate(UsersBase):
    password: str

# user_id:type = int
# name:type = string
# last:type = string
# phone:type = string
# email:type = string
# registration_date:type = Date
# user_type:type = Emun('client', 'admin')
# direccion:type = string
# sha256_passwd:type = string