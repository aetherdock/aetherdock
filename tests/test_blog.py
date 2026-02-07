import pytest

@pytest.mark.asyncio
async def test_blog_flow(async_client):
    login_resp = await async_client.post(
        "/api/v1/auth/login",
        json = {
            "username": "zhangpp",
            "password": "123456"
        }
    )
    token = login_resp.json()["access_token"]
    headers = {
        "Authorization": f"Bearer {token}"
    }

    create_resp = await async_client.post(
        "/api/v1/blogs",
        headers = headers,
        json = {
            "title": "Test Blog",
            "summary": "This is a test summary",
            "content": "This is a test blog"
        }
    )
    assert create_resp.status_code == 200
    blog_id = create_resp.json()["id"]

    publish_resp = await async_client.post(
        f"/api/v1/blogs/{blog_id}/publish",
        headers = headers
    )
    assert publish_resp.status_code == 200

    list_resp = await async_client.get("/api/v1/blogs")
    assert list_resp.status_code == 200
    assert len(list_resp.json()) >= 1