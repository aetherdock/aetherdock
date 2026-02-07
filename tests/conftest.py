import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app

@pytest.fixture(scope="module")
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://127.0.0.1:8000") as client:
        yield client
