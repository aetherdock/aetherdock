from datetime import datetime
from sqlmodel import Session

from app.models.blog import Blog
from app.repository.blog_reop import (
    create_blog,
    get_blog,
    list_published_blogs,
    update_blog,
    delete_blog
)


def create_new_blog(session: Session, data, author_id: int):
    blog = Blog(
        title=data.title,
        summary=data.summary,
        content=data.content,
        author_id=author_id
    )
    return create_blog(session, blog)


def publish_blog(session: Session, blog_id: int):
    blog = get_blog(session, blog_id)
    blog.status = "published"
    blog.updated_at = datetime.now()
    return update_blog(session, blog)


def list_blogs(session: Session):
    return list_published_blogs(session)


def remove_blog(session: Session, blog_id: int):
    blog = get_blog(session, blog_id)
    delete_blog(session, blog)