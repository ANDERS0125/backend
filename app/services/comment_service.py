
from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.comments import Comments

# Create comment
def create_comment_service(comment: Comments, session: Session):
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment

# Read all comments
def read_comments_service(session: Session):
    return session.exec(select(Comments)).all()

# Read a comment by ID
def read_comment_service(comment_id: int, session: Session):
    comment = session.get(Comments, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

# Update comment
def update_comment_service(comment_id: int, comment_data: Comments, session: Session):
    comment = session.get(Comments, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment.rating = comment_data.rating
    comment.comment = comment_data.comment
    comment.review_date = comment_data.review_date
    comment.destination_id = comment_data.destination_id
    comment.user_id = comment_data.user_id
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment

# Delete comment
def delete_comment_service(comment_id: int, session: Session):
    comment = session.get(Comments, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    session.delete(comment)
    session.commit()
    return {"message": "Comment deleted successfully"}