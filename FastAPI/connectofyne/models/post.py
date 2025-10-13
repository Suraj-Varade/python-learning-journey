from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserPostIn(BaseModel):
    content: str


class UserPost(UserPostIn):
    post_id: int = 0
    user_id: int
    image_url: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

    """
    class config:
        orm_mode = True  # Hey, this model may receive ORM objects, 
        # so I should allow attribute access instead of just dictionary keys.
    """


class UserPostWithLikes(UserPost):
    likes: int  # count of likes

    model_config = ConfigDict(from_attributes=True)

    """
    class config:
        orm_mode = True
    """


class CommentIn(BaseModel):
    comment: str
    post_id: int


class Comment(CommentIn):
    comment_id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)

    """
    class config:
        orm_mode = True  # return_value["comment"] or return_value.comment
    """


class UserPostWithComments(BaseModel):
    post: UserPostWithLikes
    comments: list[Comment]


class PostLikeIn(BaseModel):
    post_id: int


class PostLike(PostLikeIn):
    like_id: int
    user_id: int
