import logging
from typing import Annotated

from connectofyne import tasks
from connectofyne.database import database, user_table
from connectofyne.models.user import UserIn
from connectofyne.security import (
    authenticate_user,
    create_access_token,
    create_confirmation_token,
    get_password_hash,
    get_subject_for_token_type,
    get_user,
)
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Request, status

logger = logging.getLogger(__name__)

router = APIRouter()


# Register
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserIn, background_tasks: BackgroundTasks, request: Request
):
    if await get_user(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user already exist."
        )

    query = user_table.insert().values(
        email=user.email, password=get_password_hash(user.password)
    )

    logger.debug(query)

    await database.execute(query)

    # send mail to user, background task -- automatically await the function
    # adding this will help us to improve API endpoint performance, the process will not wait for sending email,
    # and immediately respond back to client
    background_tasks.add_task(
        tasks.send_user_registration_email,
        user.email,
        confirmation_url=request.url_for(
            "confirm_email", token=create_confirmation_token(user.email)
        ),
    )

    return {
        "detail": "user created successfully, please confirm your email.",
        "confirmation_url": request.url_for(
            "confirm_email", token=create_confirmation_token(user.email)
        ),
    }


"""
@router.post("/token", status_code=status.HTTP_200_OK)
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    grant_type: Annotated[str, Form()],
):
    user = await authenticate_user(username, password)
    access_token = create_access_token(user.email)
    return {"access_token": access_token, "token_type": "bearer"}
"""


## login
@router.post("/token", status_code=200)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await authenticate_user(form_data.username, form_data.password)
    access_token = create_access_token(user.email)
    return {"access_token": access_token, "token_type": "Bearer"}


@router.get("/confirm/{token}")
async def confirm_email(token: str):
    email = get_subject_for_token_type(token, "confirmation")
    query = (
        user_table.update().where(user_table.c.email == email).values(confirmed=True)
    )
    logger.debug(query)

    await database.execute(query)
    return {"detail": "user confirmed"}
