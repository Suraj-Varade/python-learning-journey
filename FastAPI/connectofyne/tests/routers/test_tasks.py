import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_send_simple_email(async_client: AsyncClient, mock_send_mail_async):
    response = await async_client.post(
        "/api/register",
        json={"email": "test@example.com", "password": "1234567"},
    )

    # Assert
    assert response.status_code == 201
    mock_send_mail_async.assert_called_once()

    # assert True
