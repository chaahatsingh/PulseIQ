from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app.schemas.content import ContentCreate, ContentResponse
from app.crud.content import create_content, get_all_content

from app.crud.content import create_content
from app.db.dependencies import get_db
from app.schemas.content import ContentCreate

app = FastAPI(title="PulseIQ")


@app.get("/")
def root():
    return {"message": "PulseIQ Backend Running"}


@app.post(
    "/content",
    response_model=ContentResponse,
    status_code=201,
)
def create_content_endpoint(
    content: ContentCreate,
    db: Session = Depends(get_db),
):
    return create_content(db, content)

@app.get(
    "/content",
    response_model=list[ContentResponse],
)
def get_all_content_endpoint(
    db: Session = Depends(get_db),
):
    return get_all_content(db)