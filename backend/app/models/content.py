from datetime import datetime

from sqlalchemy import String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Content(Base):
    __tablename__ = "content"

    id: Mapped[int] = mapped_column(primary_key=True)

    source: Mapped[str] = mapped_column(String(50))

    source_post_id: Mapped[str] = mapped_column(String(255), unique=True)

    author: Mapped[str] = mapped_column(String(255))

    text: Mapped[str] = mapped_column(Text)

    url: Mapped[str] = mapped_column(String(500))

    language: Mapped[str] = mapped_column(String(20))

    published_at: Mapped[datetime]

    scraped_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)