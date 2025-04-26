from typing import Any, Optional

import aiohttp

from api_code.schema import User, UserGetLoginUserQuery
from api_mcp.server import mcp_server

BASE_URL = "https://petstore3.swagger.io/api/v3"


@mcp_server.tool()
async def user_post_create_user(req_data: User, /) -> Optional[User]:

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=f"{BASE_URL}/user", json=req_data.dict(exclude_unset=True)
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return User(**data)

            else:
                return None


@mcp_server.tool()
async def user_post_create_users_with_list_input(
    req_data: list[User], /
) -> Optional[User]:

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=f"{BASE_URL}/user/createWithList",
            json=req_data.dict(exclude_unset=True),
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return User(**data)

            else:
                return None


@mcp_server.tool()
async def user_get_login_user(params: UserGetLoginUserQuery) -> Optional[str]:

    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{BASE_URL}/user/login",
            params=params.model_dump(exclude_unset=True),
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return str(**data)

            else:
                return None


@mcp_server.tool()
async def user_get_logout_user() -> Any:

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=f"{BASE_URL}/user/logout",
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return data

            else:
                return None


@mcp_server.tool()
async def user_get_get_user_by_name(username: str) -> Optional[User]:
    url = f"{BASE_URL}/user/{username}"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=url,
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return User(**data)

            else:
                return None


@mcp_server.tool()
async def user_put_update_user(req_data: User, /, username: str) -> Optional[User]:
    url = f"{BASE_URL}/user/{username}"

    async with aiohttp.ClientSession() as session:
        async with session.put(url=url, json=req_data.dict(exclude_unset=True)) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return User(**data)

            else:
                return None


@mcp_server.tool()
async def user_delete_delete_user(req_data: User, /, username: str) -> Optional[User]:
    url = f"{BASE_URL}/user/{username}"

    async with aiohttp.ClientSession() as session:
        async with session.delete(
            url=url, json=req_data.dict(exclude_unset=True)
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return User(**data)

            else:
                return None
