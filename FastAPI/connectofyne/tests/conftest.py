import logging
import os
from typing import AsyncGenerator, Generator
from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

os.environ["ENV_STATE"] = "test"
import connectofyne.tasks as tasks
from connectofyne.database import database, user_table
from connectofyne.main import app

logger = logging.getLogger(__name__)
## from connectofyne.routers.post import comment_table, post_table


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    await database.connect()
    yield
    await (
        database.disconnect()
    )  ## since the db rollback set to True, it will rollback everything.


## at the beginning of the test function - we are connecting to DB
## yield -->> run the test functions


@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac


@pytest.fixture()
async def registered_user(async_client: AsyncClient) -> dict:
    user_details = {"email": "test@example.com", "password": "12344"}
    await async_client.post("/api/register", json=user_details)
    query = user_table.select().where(user_table.c.email == user_details["email"])
    logger.debug(query)
    user_result = await database.fetch_one(query)
    logger.debug(user_result)
    user_details["user_id"] = user_result.user_id
    return user_details


@pytest.fixture()
async def confirmed_user(registered_user: dict) -> dict:
    query = (
        user_table.update()
        .where(user_table.c.email == registered_user["email"])
        .values(confirmed=True)
    )
    await database.execute(query)
    return registered_user


@pytest.fixture()
async def logged_in_token(async_client: AsyncClient, confirmed_user: dict) -> str:
    response = await async_client.post(
        "/api/token",
        data={
            "username": confirmed_user["email"],
            "password": confirmed_user["password"],
            "grant_type": "password",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    print("TOKEN RESPONSE:", response.status_code, response.json())
    return response.json()["access_token"]


@pytest.fixture(autouse=True)
async def mock_send_mail_async(monkeypatch):
    """
    Automatically mock all email-sending during tests.
    """
    mock_send_mail_async = AsyncMock(return_value={"detail": "mail send successfully"})
    mock_send_user_registration_email = AsyncMock(
        return_value={"detail": "mail send successfully"}
    )

    monkeypatch.setattr(tasks, "send_mail_async", mock_send_mail_async)
    monkeypatch.setattr(
        tasks, "send_user_registration_email", mock_send_user_registration_email
    )

    return mock_send_user_registration_email
