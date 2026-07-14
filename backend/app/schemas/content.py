from datetime import datetime

from pydantic import BaseModel


class ContentCreate(BaseModel):
    source: str
    source_post_id: str
    author: str
    text: str
    url: str
    language: str
    published_at: datetime
    
from pydantic import BaseModel, ConfigDict


class ContentResponse(BaseModel):
    id: int
    source: str
    source_post_id: str
    author: str
    text: str
    url: str
    language: str
    published_at: datetime
    scraped_at: datetime

    model_config = ConfigDict(from_attributes=True)