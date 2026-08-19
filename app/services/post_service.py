from datetime import datetime
from sqlalchemy.orm import Session
from app.models import Post
from app.services.ai_service import generate_post, TOPICS
from app.services.linkedin_service import publish_to_linkedin

def create_daily_post(db: Session, auto_publish: bool = False):
    used_topics = {p.topic for p in db.query(Post).all()}
    topic = next((t for t in TOPICS if t not in used_topics), TOPICS[0])
    content = generate_post(topic)
    post = Post(topic=topic, content=content, status="draft")
    db.add(post)
    db.commit()
    db.refresh(post)
    if auto_publish:
        publish_post(db, post.id)
    return post

def publish_post(db: Session, post_id: int):
    post = db.get(Post, post_id)
    if not post:
        raise ValueError("Post not found")
    if not post.approved:
        raise ValueError("Post must be approved before publishing")
    if post.status == "published":
        return post
    linkedin_id = publish_to_linkedin(post.content)
    post.status = "published"
    post.linkedin_post_id = linkedin_id
    post.published_at = datetime.utcnow()
    db.commit()
    db.refresh(post)
    return post
