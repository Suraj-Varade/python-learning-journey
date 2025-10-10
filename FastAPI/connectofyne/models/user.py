from pydantic import BaseModel


class User(BaseModel):
    user_id: int | None = None
    email: str


class UserIn(User):
    password: str
