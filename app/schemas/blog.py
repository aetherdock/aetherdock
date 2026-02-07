from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    summary: str
    content: str

class BlogRead(BaseModel):
    id: int
    title: str
    summary: str
    content: str
    status: str