import pytest
from httpx import AsyncClient, ASGITransport
from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool

from app.main import app
from app.db import get_session
from app.models.user import User
from app.services.auth_service import hash_password

# Use in-memory database for tests
TEST_DB_URL = "sqlite:///:memory:"
engine = create_engine(
    TEST_DB_URL, 
    connect_args={"check_same_thread": False}, 
    poolclass=StaticPool
)

@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="test_user")
def test_user_fixture(session: Session):
    user = User(
        username="zhangpp",
        password_hash=hash_password("123456"),
        role="admin"
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@pytest.fixture
async def async_client(session: Session, test_user: User):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://127.0.0.1:8000") as client:
        yield client
    
    app.dependency_overrides.clear()
