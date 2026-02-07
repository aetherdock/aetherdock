from sqlmodel import Session, select
from app.models.blog import Blog

def create_blog(session: Session, blog: Blog):
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog

def get_blog(session: Session, blog_id: int):
    return session.get(Blog, blog_id)

def list_published_blogs(session: Session):
    statement = select(Blog).where(Blog.status == "published")
    return session.exec(statement).all()

def update_blog(session: Session, blog: Blog):
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog

def delete_blog(session: Session, blog: Blog):
    session.delete(blog)
    session.commit()