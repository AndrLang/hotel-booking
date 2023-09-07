from httpx import AsyncClient
import pytest


@pytest.mark.parametrize("email, password, status_code", [
    ("alicia@proto.com", "alice", 200),
    ("alicia@proto.com", "al0ice", 409),
    ("alicia@protonmail.com", "al0ice", 200),
    ("abcdef", "alice", 422),
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/register", json={
            "email": email,
            "password": password,
        })

    assert response.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("test@test.com", "test", 200)
])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/login", json={
            "email": email,
            "password": password,
        })
    assert response.status_code == status_code