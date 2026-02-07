from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.api.deps import get_db, require_admin
from app.schemas.blog import BlogCreate, BlogRead
from app.models.user import User
from app.services.blog_service import (
    create_new_blog,
    publish_blog,
    list_blogs, 
    remove_blog
)

router = APIRouter(prefix="/blogs", tags=["blog"])

@router.get("", response_model=list[BlogRead])
def get_blogs(session: Session = Depends(get_db)):
    return list_blogs(session)

@router.post("", dependencies=[Depends(require_admin)])
def create_blog(data: BlogCreate, session: Session = Depends(get_db), user: User=Depends(require_admin)):
    return create_new_blog(session, data, user.id)

@router.post("/{blog_id}/publish", dependencies=[Depends(require_admin)])
def publish_blog_endpoint(blog_id: int, session: Session = Depends(get_db)):
    return publish_blog(session, blog_id)

@router.delete("/{blog_id}", dependencies=[Depends(require_admin)])
def delete_blog(blog_id: int, session: Session = Depends(get_db)):
    return remove_blog(session, blog_id)