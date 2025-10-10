import logging

import pytest
from jose import jwt

from connectofyne import security

logger = logging.getLogger(__name__)


def test_access_token_expire_minutes():
    assert security.access_token_expire_minute() == 30


def test_confirmation_token_expire_minutes():
    assert security.confirm_token_expire_minute() == 1440


def test_create_access_token():
    token = security.create_access_token("21344@212.com")
    assert {"sub": "21344@212.com", "type": "access"}.items() <= jwt.decode(
        token, key=security.SECRET_KEY, algorithms=[security.ALGORITHM]
    ).items()


def test_create_confirmation_token():
    token = security.create_confirmation_token("21344@212.com")
    assert {"sub": "21344@212.com", "type": "confirmation"}.items() <= jwt.decode(
        token, key=security.SECRET_KEY, algorithms=[security.ALGORITHM]
    ).items()


## test - when token type is valid.
def test_get_subject_for_token_type_valid_confirmation():
    email = "test@example.com"
    token = security.create_confirmation_token(email)
    response = security.get_subject_for_token_type(token, "confirmation")
    assert email == response


## test - when token type is invalid.
def test_get_subject_for_token_type_invalid_confirmation():
    email = "test@example.com"
    token = security.create_confirmation_token(email)
    with pytest.raises(security.HTTPException):
        security.get_subject_for_token_type(token, "access")


## test - when token type is valid. - access
def test_get_subject_for_token_type_valid_access():
    email = "test@example.com"
    token = security.create_access_token(email)
    response = security.get_subject_for_token_type(token, "access")
    assert email == response


## test - when token type is invalid.- access
def test_get_subject_for_token_type_invalid_access():
    email = "test@example.com"
    token = security.create_access_token(email)
    with pytest.raises(security.HTTPException):
        security.get_subject_for_token_type(token, "confirmation")


def test_get_subject_for_token_type_expired(mocker):
    mocker.patch("connectofyne.security.access_token_expire_minute", return_value=-1)
    email = "test@example.com"
    token = security.create_access_token(email)
    with pytest.raises(security.HTTPException) as exe_info:
        security.get_subject_for_token_type(token, "access")
    assert "token has expired" == exe_info.value.detail


## invalid token
def test_get_subject_for_token_invalid():
    token = "invalid token"
    with pytest.raises(security.HTTPException) as exe_info:
        security.get_subject_for_token_type(token, "confirmation")
    assert "invalid token" == exe_info.value.detail


## sub is missing
def test_get_subject_for_token_type_sub_is_missing():
    email = "test@example.com"
    token = security.create_access_token(email)
    payload = jwt.decode(
        token, key=security.SECRET_KEY, algorithms=[security.ALGORITHM]
    )
    del payload["sub"]

    token = jwt.encode(payload, key=security.SECRET_KEY, algorithm=security.ALGORITHM)

    with pytest.raises(security.HTTPException) as exe_info:
        security.get_subject_for_token_type(token, "access")
    assert "token is missing 'sub' field" == exe_info.value.detail


def test_password_hashes():
    password = "password"
    password_hash = security.get_password_hash(password)
    assert security.verify_password(password, password_hash)


@pytest.mark.anyio
async def test_get_user(registered_user: dict):
    user = await security.get_user(registered_user["email"])

    assert user.email == registered_user["email"]


@pytest.mark.anyio
async def test_get_user_not_found():
    user = await security.get_user("user12@example.com")

    assert user is None


@pytest.mark.anyio
async def test_authenticate_user(confirmed_user: dict):
    user = await security.authenticate_user(
        confirmed_user["email"], confirmed_user["password"]
    )
    assert user.email == confirmed_user["email"]


@pytest.mark.anyio
async def test_authenticate_user_not_found():
    with pytest.raises(security.HTTPException):
        await security.authenticate_user("test@example.com", "1233")


@pytest.mark.anyio
async def test_authenticate_user_wrong_password(registered_user: dict):
    with pytest.raises(security.HTTPException):
        await security.authenticate_user(registered_user["email"], "wrong password")


@pytest.mark.anyio
async def test_get_current_user(registered_user: dict):
    token = security.create_access_token(registered_user["email"])
    user = await security.get_current_user(token)
    logger.debug(user)
    assert user.email == registered_user["email"]


@pytest.mark.anyio
async def test_get_current_user_invalid_token():
    with pytest.raises(security.HTTPException):
        await security.get_current_user("invalid token")


@pytest.mark.anyio
async def test_get_current_user_wrong_type_token(registered_user: dict):
    token = security.create_confirmation_token(registered_user["email"])

    with pytest.raises(security.HTTPException):
        await security.get_current_user(
            token
        )  ## since get_current_user - excepts only the access token and we are passing confirmation token
