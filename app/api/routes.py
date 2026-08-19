from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.models import Post
from app.schemas import PostResponse
from app.services.post_service import create_daily_post, publish_post

Base.metadata.create_all(bind=engine)
router = APIRouter()

@router.post("/posts/generate", response_model=PostResponse)
def generate(db: Session = Depends(get_db)):
    return create_daily_post(db, auto_publish=False)

@router.get("/posts", response_model=list[PostResponse])
def list_posts(db: Session = Depends(get_db)):
    return db.query(Post).order_by(Post.created_at.desc()).all()

@router.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(404, "Post not found")
    return post

@router.post("/posts/{post_id}/approve", response_model=PostResponse)
def approve(post_id: int, db: Session = Depends(get_db)):
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(404, "Post not found")
    post.approved = True
    post.status = "approved"
    db.commit()
    db.refresh(post)
    return post

@router.post("/posts/{post_id}/publish", response_model=PostResponse)
def publish(post_id: int, db: Session = Depends(get_db)):
    try:
        return publish_post(db, post_id)
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(400, str(exc))
