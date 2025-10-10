import logging

import pytest
from httpx import AsyncClient

from fastapi import BackgroundTasks

logger = logging.getLogger(__name__)


async def register_user(async_client: AsyncClient, email: str, password: str):
    return await async_client.post(
        "/api/register", json={"email": email, "password": password}
    )


@pytest.mark.anyio
async def test_register_user(async_client: AsyncClient, mock_send_mail_async):
    email = "test@example.com"
    password = "AB1234C"
    response = await register_user(async_client, email, password)
    # {"detail": "user created successfully."}
    logger.info(f"{response.json()}")
    assert response.status_code == 201
    assert "user created" in response.json()["detail"]
    assert "user created successfully" in response.json()["detail"]

    mock_send_mail_async.assert_called_once()


## user confirmation
@pytest.mark.anyio
async def test_confirm_user(async_client: AsyncClient, mocker, mock_send_mail_async):
    spy = mocker.spy(BackgroundTasks, "add_task")
    await register_user(async_client, "test@example.com", "1234567")
    confirmation_url = str(spy.call_args[1]["confirmation_url"])  # str(spy.spy_return)
    response = await async_client.get(confirmation_url)
    assert response.status_code == 200
    assert "user confirmed" in response.json()["detail"]
    mock_send_mail_async.assert_called_once()


"""
@pytest.mark.anyio
async def test_confirm_user(async_client: AsyncClient, mocker):
    spy = mocker.spy(Request, "url_for")
    await register_user(async_client, "test@example.com", "1234567")
    confirmation_url = str(spy.spy_return)
    response = await async_client.get(confirmation_url)
    assert response.status_code == 200
    assert "user confirmed" in response.json()["detail"]
"""

"""
@pytest.mark.anyio
step 1: This tells pytest that this is an asynchronous test (using async def), and it should be run using the AnyIO event loop (compatible with FastAPI, Starlette, etc.).


spy = mocker.spy(Request, "url_for")
step 2: You’re setting up a spy on the Request.url_for() method.
That means — during the test, every time your app calls Request.url_for(...), pytest-mock will record that call and capture what it returned.
Purpose:
To see what URL your app generated for the user confirmation link.


confirmation_url = str(spy.spy_return)
step 3: After register_user() runs, the spy has recorded what Request.url_for() returned.
That return value (the generated confirmation link) is stored in spy.spy_return.

For example, it could be:
http://testserver.com/api/confirm?token=abcdef123

"""


## user confirmation - invalid token
@pytest.mark.anyio
async def test_confirm_user_invalid_token(async_client: AsyncClient):
    response = await async_client.get("/api/confirm/invalid-token")
    assert response.status_code == 401


## user confirmation - after too late - 24 hours passed
@pytest.mark.anyio
async def test_confirm_user_token_expires(
    async_client: AsyncClient, mocker, mock_send_mail_async
):
    mocker.patch("connectofyne.security.confirm_token_expire_minute", return_value=-1)
    # spy = mocker.spy(Request, "url_for")
    spy = mocker.spy(BackgroundTasks, "add_task")
    await register_user(async_client, "test@example.com", "1234567")
    confirmation_url = str(spy.call_args[1]["confirmation_url"])  # str(spy.spy_return)
    response = await async_client.get(confirmation_url)
    assert response.status_code == 401
    assert "token has expired" in response.json()["detail"]
    mock_send_mail_async.assert_called_once()


@pytest.mark.anyio
async def test_register_user_already_exist(
    async_client: AsyncClient, registered_user: dict
):
    response = await register_user(
        async_client, registered_user["email"], registered_user["password"]
    )
    assert response.status_code == 400
    assert "user already exist." in response.json()["detail"]


@pytest.mark.anyio
async def test_login_user_not_exist(async_client: AsyncClient):
    response = await async_client.post(
        "/api/token",
        data={
            "username": "test@example.com",
            "password": "12345678",
            "grant_type": "password",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 401


@pytest.mark.anyio
async def test_login(async_client: AsyncClient, confirmed_user: dict):
    response = await async_client.post(
        "/api/token",
        data={
            "username": confirmed_user["email"],
            "password": confirmed_user["password"],
            "grant_type": "password",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 200


## try login with not confirmed user
@pytest.mark.anyio
async def test_login_user_not_confirmed(
    async_client: AsyncClient, registered_user: dict
):
    response = await async_client.post(
        "/api/token",
        data={
            "username": registered_user["email"],
            "password": registered_user["password"],
            "grant_type": "password",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 401
