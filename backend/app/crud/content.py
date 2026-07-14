from sqlalchemy.orm import Session

from app.models.content import Content
from app.schemas.content import ContentCreate


def create_content(db: Session, content: ContentCreate) -> Content:
    db_content = Content(
        source=content.source,
        source_post_id=content.source_post_id,
        author=content.author,
        text=content.text,
        url=content.url,
        language=content.language,
        published_at=content.published_at,
    )

    db.add(db_content)
    db.commit()
    db.refresh(db_content)

    return db_content

def get_all_content(db: Session) -> list[Content]:
    return db.query(Content).all()