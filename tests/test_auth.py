import pytest

@pytest.mark.asyncio
async def test_user_login(async_client):
    response = await async_client.post("/api/v1/auth/login", json={
        "username": "zhangpp",
        "password": "123456"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()