import logging
from enum import Enum
from typing import Annotated

import sqlalchemy
from connectofyne.database import comment_table, database, like_table, post_table
from connectofyne.models.post import (
    Comment,
    CommentIn,
    PostLike,
    PostLikeIn,
    UserPost,
    UserPostIn,
    UserPostWithComments,
    UserPostWithLikes,
)
from connectofyne.models.user import User
from connectofyne.security import get_current_user

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

logger = logging.getLogger(__name__)


select_post_and_likes = (
    sqlalchemy.select(
        post_table, sqlalchemy.func.count(like_table.c.like_id).label("likes")
    )
    .select_from(post_table.outerjoin(like_table))
    .group_by(post_table.c.post_id)
)
## give me all the columns from post_table, and extra column count - sqlalchemy.select
## select it from - post_table outerjoin like_table
## then group_by it based on post_table.post_id, so that we can easily get the count
"""
SELECT 
    posts.post_id,
    posts.content,
    posts.user_id,
    COUNT(likes.like_id) AS likes
FROM posts
LEFT JOIN likes ON posts.post_id = likes.post_id
GROUP BY posts.post_id;
"""


## Find a post ---------------------------------------------------
async def find_post(post_id: int):
    logger.info(f"finding a post with post_id {post_id}")
    query = post_table.select().where(post_table.c.post_id == post_id)
    return await database.fetch_one(query)  # first value return by the query


## Create a post ---------------------------------------------------
@router.post("/post", response_model=UserPost, status_code=status.HTTP_201_CREATED)
async def create_post(
    post: UserPostIn, current_user: Annotated[User, Depends(get_current_user)]
):
    logger.info("creating a post")

    """
    current_user: User = await get_current_user(
        await oauth2_scheme(request)
    )  # this will grab the bearer token from client request    
    """

    data = {**post.model_dump(), "user_id": current_user.user_id}
    ## dictionary keys should matches column names.
    query = post_table.insert().values(data)
    last_record_id = await database.execute(query)
    return {**data, "post_id": last_record_id}


# {
#   1: {'post_id': 1, 'content': 'this is my first post'},
#   2: {'post_id': 2, 'content': 'this is my second post'}
# }


## for all kind of sorting, filtering - enum is the best choice to consider
class PostSorting(str, Enum):
    new = "new"
    old = "old"
    most_likes = "most_likes"


## get all the available post ---------------------------------------------------
## include likes and sorted by number of likes
@router.get("/post", response_model=list[UserPostWithLikes])
## sorting: PostSorting = PostSorting.new - this will be coming as querystring (fastapi expect)
## https://domain.com/api/post?sorting=most_likes
async def get_all_post(sorting: PostSorting = PostSorting.new):
    logger.info("getting all posts")

    match sorting:
        case PostSorting.new:
            query = select_post_and_likes.order_by(post_table.c.post_id.desc())
        case PostSorting.old:
            query = select_post_and_likes.order_by(post_table.c.post_id.asc())
        case PostSorting.most_likes:
            query = select_post_and_likes.order_by(sqlalchemy.desc("likes"))

    return await database.fetch_all(query)


"""    
    if sorting == PostSorting.new:
        query = select_post_and_likes.order_by(post_table.c.post_id.desc())
    elif sorting == PostSorting.old:
        query = select_post_and_likes.order_by(post_table.c.post_id.asc())
    else:
        query = select_post_and_likes.order_by(sqlalchemy.desc("likes"))
"""


"""
## get all the available post ---------------------------------------------------

@router.get("/post", response_model=list[UserPost])
async def get_all_post():
    logger.info("getting all posts")
    query = post_table.select()

    
    logger.debug(
        query
    )  
    ## 2025-10-07T14:54:59 DEBUG    connectofyne.routers.post:49 - SELECT posts.post_id, posts.content FROM posts
    
    return await database.fetch_all(query)
"""


## Create a comment ---------------------------------------------------
@router.post(
    "/comment",
    response_model=Comment,
    status_code=(status.HTTP_201_CREATED),
)
async def create_comment(
    comment: CommentIn, current_user: Annotated[User, Depends(get_current_user)]
):
    logger.info("creating a comment")

    """
    current_user: User = await get_current_user(
        await oauth2_scheme(request)
    )  # this will grab the bearer token from client request
    """

    post = await find_post(comment.post_id)
    if not post:
        # logger.error(f"post with post_id {comment.post_id} not found")
        raise HTTPException(status_code=404, detail="Post not found")

    data = {**comment.model_dump(), "user_id": current_user.user_id}
    query = comment_table.insert().values(data)
    last_record_id = await database.execute(query)
    return {**data, "comment_id": last_record_id}


## **data - is for structuring dictionary within another dictionary.


"""
{
	"comment": "this is my 2 comment to your post 2",
	"post_id": 2,
	"comment_id": 1
}
"""


## get all comments on a post ---------------------------------------------------
@router.get("/post/{post_id}/comment", response_model=list[Comment])
async def get_comments_on_post(post_id: int):
    logger.info(f"get all comments on a post {post_id}")
    query = comment_table.select().where(comment_table.c.post_id == post_id)
    return await database.fetch_all(query)


"""
[
	{
		"comment": "this is my 1 comment to your post 1",
		"post_id": 1,
		"comment_id": 1
	},
	{
		"comment": "this is my 2 comment to your post 1",
		"post_id": 1,
		"comment_id": 2
	}
]
"""


## get post with comments ---------------------------------------------------
@router.get("/post/{post_id}", response_model=UserPostWithComments)
async def get_post_with_comments(post_id: int):
    logger.info(f"finding a post with post_id {post_id}")

    query = select_post_and_likes.where(post_table.c.post_id == post_id)

    logger.debug(query)

    post = await database.fetch_one(query)

    if not post:
        # logger.error(f"post with post_id {post_id} not found")
        raise HTTPException(status_code=404, detail="post not found")

    return {
        "post": post,
        "comments": await get_comments_on_post(post_id),
    }


## liking the post
@router.post("/like", response_model=PostLike, status_code=201)
async def like_post(
    like: PostLikeIn, current_user: Annotated[User, Depends(get_current_user)]
):
    logger.info("liking a post")
    # get the post
    post = await find_post(like.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="post not found")

    data = {**like.model_dump(), "user_id": current_user.user_id}
    query = like_table.insert().values(data)

    logger.debug(query)

    last_record_id = await database.execute(query)
    return {**data, "like_id": last_record_id}
