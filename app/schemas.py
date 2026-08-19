from datetime import datetime
from pydantic import BaseModel

class PostResponse(BaseModel):
    id: int
    topic: str
    content: str
    status: str
    approved: bool
    linkedin_post_id: str | None
    published_at: datetime | None
    created_at: datetime

    class Config:
        from_attributes = True
