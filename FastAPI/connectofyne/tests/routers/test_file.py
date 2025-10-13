import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_get_presigned_url(async_client: AsyncClient, logged_in_token: str):
    filename = "test.png"
    content_type = "image/png"

    response = await async_client.get(
        "/api/get-presigned-url",
        params={"filename": filename, "content_type": content_type},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["upload_url"] == "https://fake-upload-url.com"
    assert data["file_path"] == "test"


@pytest.mark.anyio
async def test_get_download_url(async_client: AsyncClient, logged_in_token: str):
    filepath = "user/profile.png"
    download_url = "https://fake-upload-url.com"

    response = await async_client.get(
        "/api/download-url",
        params={"file_path": filepath},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["download_url"] == download_url


"""
mock_service.generate_upload_url.return_value = {
        "upload_url": "https://fake-upload-url.com",
        "file_path": "test",
    }
    mock_service.generate_download_url.return_value = {
        "download_url": "https://fake-upload-url.com"
    }
"""


# test 500
@pytest.mark.anyio
async def test_upload_url_500(
    async_client: AsyncClient, mock_s3_service, logged_in_token: str
):
    mock_s3_service.generate_upload_url.side_effect = Exception("s3 service failed")
    filename = "test.png"
    content_type = "image/png"

    response = await async_client.get(
        "/api/get-presigned-url",
        params={"filename": filename, "content_type": content_type},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )

    assert response.status_code == 500
    response.json()["detail"] = "s3 service failed"


@pytest.mark.anyio
async def test_set_profile_picture(async_client: AsyncClient, logged_in_token: str):
    response = await async_client.post(
        "/api/profile-picture",
        json={"file_path": "uploads/test.png"},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "profile picture updated"


## file_path is missing
@pytest.mark.anyio
async def test_set_profile_picture_file_path_missing(
    async_client: AsyncClient, logged_in_token: str
):
    response = await async_client.post(
        "/api/profile-picture",
        json={"file_path": ""},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "file_path is required"


## file_path is missing
@pytest.mark.anyio
async def test_set_profile_picture_no_file_path(
    async_client: AsyncClient, logged_in_token: str
):
    response = await async_client.post(
        "/api/profile-picture",
        json={},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )
    assert response.status_code == 422
