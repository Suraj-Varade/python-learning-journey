import pytest
from httpx import AsyncClient

from connectofyne import security


## create a post
async def create_post(
    content: str, async_client: AsyncClient, logged_in_token: str
) -> dict:
    response = await async_client.post(
        "/api/post",
        json={"content": content},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )
    return response.json()


## like a post
async def like_post(
    post_id: int, async_client: AsyncClient, logged_in_token: str
) -> dict:
    response = await async_client.post(
        "/api/like",
        json={"post_id": post_id},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )

    return response.json()


## create  a comment
async def create_comment(
    comment_text: str, post_id: int, async_client: AsyncClient, logged_in_token: str
):
    response = await async_client.post(
        "/api/comment",
        json={"post_id": post_id, "comment": comment_text},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )
    return response.json()


## created comment - fixture
@pytest.fixture()
async def created_comment(
    async_client: AsyncClient, created_post: dict, logged_in_token: str
):
    return await create_comment(
        "this is my comment", created_post["post_id"], async_client, logged_in_token
    )


## created post - fixture
@pytest.fixture()
async def created_post(async_client: AsyncClient, logged_in_token: str):
    return await create_post("test post", async_client, logged_in_token)


## post endpoint - create a post --------------------------------------------------
@pytest.mark.anyio
async def test_create_post(
    async_client: AsyncClient, confirmed_user: dict, logged_in_token: str
):
    content = "test post"
    response = await async_client.post(
        "/api/post",
        json={"content": content},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )

    assert response.status_code == 201
    assert (
        {
            "post_id": 1,
            "content": content,
            "user_id": confirmed_user["user_id"],
            "image_url": None,
        }.items()
        <= response.json().items()
    )  # check if left side block present in the right side json items


## create a post, where token is expired
# mocker allows us to modify the access_token's expiry.
@pytest.mark.anyio
async def test_create_post_with_expired_token(
    async_client: AsyncClient, confirmed_user: dict, mocker
):
    mocker.patch("connectofyne.security.access_token_expire_minute", return_value=-1)
    token = security.create_access_token(confirmed_user["email"])
    response = await async_client.post(
        "/api/post",
        json={"content": "Test content"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 401
    assert "token has expired" in response.json()["detail"]


## create a post, but don't pass the content
@pytest.mark.anyio
async def test_create_post_without_content(
    async_client: AsyncClient, logged_in_token: str
):
    response = await async_client.post(
        "/api/post", json={}, headers={"Authorization": f"Bearer {logged_in_token}"}
    )
    assert response.status_code == 422


## getting all post
@pytest.mark.anyio
async def test_get_all_post(async_client: AsyncClient, created_post: dict):
    response = await async_client.get("/api/post")
    assert response.status_code == 200
    assert response.json() == [{**created_post, "likes": 0}]


## getting all post -  but adding a sorting functionality. [new] -------------------------------------


@pytest.mark.anyio
@pytest.mark.parametrize(
    "sorting, expected_order",
    [
        ("new", [3, 2, 1]),
        ("old", [1, 2, 3]),
    ],
)
async def test_get_all_post_sorting(
    async_client: AsyncClient,
    logged_in_token: str,
    sorting: str,
    expected_order: list[int],
):
    await create_post("1st post", async_client, logged_in_token)  # post_id = 1
    await create_post("2nd post", async_client, logged_in_token)  # post_id = 2
    await create_post("3rd post", async_client, logged_in_token)  # post_id = 3

    response = await async_client.get("/api/post", params={"sorting": sorting})
    assert response.status_code == 200

    data = response.json()  ## data contains a list of posts
    post_ids = [post["post_id"] for post in data]
    assert post_ids == expected_order


@pytest.mark.anyio
async def test_get_all_post_sorting_by_likes(
    async_client: AsyncClient,
    logged_in_token: str,
):
    await create_post("1st post", async_client, logged_in_token)  # post_id = 1
    await create_post("2nd post", async_client, logged_in_token)  # post_id = 2
    await create_post("3rd post", async_client, logged_in_token)  # post_id = 3

    await like_post(1, async_client, logged_in_token)  # like post_id 1
    await like_post(2, async_client, logged_in_token)  # like post_id 2
    await like_post(2, async_client, logged_in_token)  # like post_id 2
    await like_post(2, async_client, logged_in_token)  # like post_id 2

    response = await async_client.get("/api/post", params={"sorting": "most_likes"})
    assert response.status_code == 200
    expected_order = [2, 1, 3]
    data = response.json()  ## data contains a list of posts
    post_ids = [post["post_id"] for post in data]
    assert post_ids == expected_order


@pytest.mark.anyio
async def test_get_all_post_wrong_sorting(
    async_client: AsyncClient, logged_in_token: str
):
    response = await async_client.post(
        "/api/post",
        params={"sorting": "wrong"},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )
    assert response.status_code == 422


"""
## getting all post - sorting [old] -------------------------------------
## but your code is duplicated, just for a sorting : new -- so consider adding parameterized pytest
@pytest.mark.anyio
async def test_get_all_post_sorting_old(
    async_client: AsyncClient, logged_in_token: str
):
    await create_post("1st post", async_client, logged_in_token)  # post_id = 1
    await create_post("2nd post", async_client, logged_in_token)  # post_id = 2
    await create_post("3rd post", async_client, logged_in_token)  # post_id = 3

    response = await async_client.get("/api/post", params={"sorting": "old"})
    assert response.status_code == 200

    data = response.json()  ## data contains a list of posts
    expected_order = [1, 2, 3]
    post_ids = [post["post_id"] for post in data]
    assert post_ids == expected_order
"""


## create  a comment -----------------------------------------------------
@pytest.mark.anyio
async def test_add_comment_to_post(
    async_client: AsyncClient,
    created_post: dict,
    confirmed_user: dict,
    logged_in_token: str,
):
    comment = "this is my very first comment to your post"
    post_id = created_post["post_id"]
    response = await async_client.post(
        "/api/comment",
        json={"post_id": post_id, "comment": comment},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )

    assert response.status_code == 201
    assert {
        "post_id": 1,
        "comment": comment,
        "comment_id": 1,
        "user_id": confirmed_user["user_id"],
    }.items() <= response.json().items()


## get comment on a post
@pytest.mark.anyio
async def test_getcomments_on_post(
    async_client: AsyncClient, created_post: dict, created_comment: dict
):
    post_id = created_post["post_id"]
    response = await async_client.get(f"/api/post/{post_id}/comment")

    assert response.status_code == 200
    assert response.json() == [created_comment]


## get comment on a post
@pytest.mark.anyio
async def test_getcomments_on_post_empty(async_client: AsyncClient, created_post: dict):
    post_id = created_post["post_id"]
    response = await async_client.get(f"/api/post/{post_id}/comment")

    assert response.status_code == 200
    assert response.json() == []


## get post with all comments
@pytest.mark.anyio
async def test_get_post_with_all_comments(
    async_client: AsyncClient, created_post: dict, created_comment: dict
):
    post_id = created_post["post_id"]
    response = await async_client.get(f"/api/post/{post_id}")

    assert response.status_code == 200
    assert response.json() == {
        "post": {**created_post, "likes": 0},
        "comments": [created_comment],
    }


## get post with comment - on missing post
@pytest.mark.anyio
async def test_get_missing_post_with_comments(
    async_client: AsyncClient, created_post: dict, created_comment: dict
):
    response = await async_client.get("/api/post/34")

    assert response.status_code == 404


# like a post -------------------------------------------------------
@pytest.mark.anyio
async def test_post_like(
    async_client: AsyncClient, created_post: dict, logged_in_token: str
):
    response = await async_client.post(
        "/api/like",
        json={"post_id": created_post["post_id"]},
        headers={"Authorization": f"Bearer {logged_in_token}"},
    )
    assert response.status_code == 201
    assert {"post_id": created_post["post_id"]}.items() <= response.json().items()
