from typing import Any, Optional

import aiohttp

from api_mcp.server import mcp_server
from api_tools.schema import Order

BASE_URL = "https://petstore3.swagger.io/api/v3"


@mcp_server.tool()
async def store_get_get_inventory() -> Optional[int]:

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=f"{BASE_URL}/store/inventory",
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return int(**data)

            else:
                return None


@mcp_server.tool()
async def store_post_place_order(req_data: Order, /) -> Optional[Order]:

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=f"{BASE_URL}/store/order", json=req_data.dict(exclude_unset=True)
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return Order(**data)

            else:
                return None


@mcp_server.tool()
async def store_get_get_order_by_id(order_id: int) -> Optional[Order]:
    url = f"{BASE_URL}/store/order/{order_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=url,
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return Order(**data)

            else:
                return None


@mcp_server.tool()
async def store_delete_delete_order(order_id: int) -> Optional[Order]:
    url = f"{BASE_URL}/store/order/{order_id}"

    async with aiohttp.ClientSession() as session:
        async with session.delete(
            url=url,
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return Order(**data)

            else:
                return None
