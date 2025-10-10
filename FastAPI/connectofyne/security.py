import datetime
import logging
from typing import Annotated, Literal

from fastapi.security import OAuth2PasswordBearer
from jose import ExpiredSignatureError, JWTError, jwt
from passlib.context import CryptContext

from connectofyne import security
from connectofyne.database import database, user_table
from fastapi import Depends, HTTPException, status

logger = logging.getLogger(__name__)


SECRET_KEY = "akhsfkasfoierhi2384623846sdghjkagdjshdbkjnokldjshf"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer("/api/token")  ## populate documentation
pwd_context = CryptContext(schemes=["bcrypt"])


def create_credentials_exception(detail: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-authenticate": "Bearer"},
    )


def access_token_expire_minute() -> int:
    return 30


## confirmation token
def confirm_token_expire_minute() -> int:
    return 1440  # 24 hours


def create_access_token(email: str):
    logger.debug("creating access token ", extra={"email": email})
    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        minutes=access_token_expire_minute()
    )
    jwt_data = {"sub": email, "exp": expire, "type": "access"}
    encoded_jwt = jwt.encode(jwt_data, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_confirmation_token(email: str):
    logger.debug("creating confirmation token ", extra={"email": email})
    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        minutes=confirm_token_expire_minute()
    )
    jwt_data = {"sub": email, "exp": expire, "type": "confirmation"}
    encoded_jwt = jwt.encode(jwt_data, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


## Literal["access", "confirmation"] - type should be between these values.
def get_subject_for_token_type(
    token: str, type: Literal["access", "confirmation"]
) -> str:
    try:
        payload = jwt.decode(
            token, key=security.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
    except ExpiredSignatureError as e:
        raise create_credentials_exception(detail="token has expired") from e
    except JWTError as e:
        raise create_credentials_exception(detail="invalid token") from e

    email = payload.get("sub")
    if email is None:
        raise create_credentials_exception(detail="token is missing 'sub' field")

    token_type = payload.get("type")
    if token_type is None or token_type != type:
        raise create_credentials_exception(
            detail=f"token has incorrect type, expected type : {type}"
        )

    return email


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def get_user(email: str):
    logger.debug("fetching user from database => ", extra={"email": email})
    query = user_table.select().where(user_table.c.email == email)
    userinfo = await database.fetch_one(query)
    if userinfo:
        return userinfo
    return None


async def authenticate_user(email: str, password: str):
    logger.debug("authenticating user", extra={"email": email})
    user = await get_user(email)
    if not user:
        raise create_credentials_exception("invalid user or password")
    if not verify_password(password, user.password):
        raise create_credentials_exception("invalid user or password")
    if not user.confirmed:
        raise create_credentials_exception("user has not confirmed email")
    return user


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
):  ## dependency injection for token
    email = get_subject_for_token_type(token, "access")
    user = await get_user(email)
    if user is None:
        raise create_credentials_exception("could not find user for this token")
    return user
