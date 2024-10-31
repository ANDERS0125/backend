from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.users import Users, UsersCreate
from app.security.security import hash_password

# Crear usuario
def create_user_service(user: UsersCreate, session: Session):
    hashed_password = hash_password(user.password)
    db_user = Users(name=user.name, mail=user.mail, hashed_password=hashed_password)
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
    user.mail = user_data.mail
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
