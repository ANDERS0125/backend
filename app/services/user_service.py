from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.users import Users, UsersCreate
from app.security.security import hash_password

# Crear usuario
def create_user_service(user: UsersCreate, session: Session):
    db_user = session.exec(select(Users).where(Users.email == user.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="user's email already exist")
    hashed_password = hash_password(user.password)
    db_user = Users(
        name=user.name,
        last=user.last,
        email=user.email,
        phone=user.phone,
        user_type=user.user_type,
        direccion=user.direccion,
        hashed_password=hashed_password
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

# Leer todos los usuarios
def read_users_service(session: Session):
    return session.exec(select(Users)).all()

# Leer un usuario por ID
def read_user_service(user_id: int, session: Session):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Actualizar usuario
def update_user_service(user_id: int, user_data: UsersCreate, session: Session):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = user_data.name
    user.last = user_data.last
    user.email = user_data.email
    user.phone = user_data.phone
    user.user_type = user_data.user_type
    user.direccion = user_data.direccion
    user.hashed_password = hash_password(user_data.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Eliminar usuario
def delete_user_service(user_id: int, session: Session):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User deleted successfully"}
