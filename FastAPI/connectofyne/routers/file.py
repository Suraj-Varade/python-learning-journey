import logging
from typing import Annotated

from connectofyne.database import database, user_table
from connectofyne.file_service import S3Service
from connectofyne.models.user import User, UserProfilePicture
from connectofyne.security import get_current_user

from fastapi import APIRouter, Depends, HTTPException, Query, status

logger = logging.getLogger(__name__)

router = APIRouter()

s3_service = S3Service()

## step 1: get presigned url
## step 2: once you got presigned url - upload a file to that endpoint
## step 3: get download url - use the filepath (received in response of #1)


@router.get("/get-presigned-url", status_code=status.HTTP_200_OK)
def get_upload_url(
    current_user: Annotated[User, Depends(get_current_user)],
    filename: str = Query(...),
    content_type: str = Query(...),
):
    try:
        return s3_service.generate_upload_url(filename, content_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/download-url", status_code=status.HTTP_200_OK)
def get_download_url(
    current_user: Annotated[User, Depends(get_current_user)],
    file_path: str = Query(...),
):
    try:
        return s3_service.generate_download_url(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/profile-picture")
async def update_profile_picture(
    payload: UserProfilePicture,
    current_user: Annotated[User, Depends(get_current_user)],
):
    if not payload.file_path:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="file_path is required"
        )

    query = (
        user_table.update()
        .where(user_table.c.user_id == current_user["user_id"])
        .values(profile_picture=payload.file_path)
    )

    await database.execute(query)
    return {"detail": "profile picture updated", "file_path": payload.file_path}
