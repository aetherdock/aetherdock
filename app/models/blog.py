from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field

class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    summary: str
    content: str
    status: str = "draft"

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    author_id: int = Field(foreign_key="user.id")