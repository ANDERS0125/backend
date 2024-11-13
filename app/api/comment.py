
from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from app.models.comments import Comments
from app.database.database import get_session
from app.services.comment_service import (
    create_comment_service,
    read_comments_service,
    read_comment_service,
    update_comment_service,
    delete_comment_service
)

router = APIRouter()

@router.post("/comments/", response_model=Comments)
def create_comment(comment: Comments, session: Session = Depends(get_session)):
    return create_comment_service(comment, session)

@router.get("/comments/", response_model=List[Comments])
def read_comments(session: Session = Depends(get_session)):
    return read_comments_service(session)

@router.get("/comments/{comment_id}", response_model=Comments)
def read_comment(comment_id: int, session: Session = Depends(get_session)):
    return read_comment_service(comment_id, session)

@router.put("/comments/{comment_id}", response_model=Comments)
def update_comment(comment_id: int, comment_data: Comments, session: Session = Depends(get_session)):
    return update_comment_service(comment_id, comment_data, session)

@router.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, session: Session = Depends(get_session)):
    return delete_comment_service(comment_id, session)