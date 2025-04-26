from typing import Any, Optional

import aiohttp

from api_code.schema import (ApiResponse, Pet, PetGetFindPetsByStatusQuery,
                             PetGetFindPetsByTagsQuery,
                             PetPostUpdatePetWithFormQuery,
                             PetPostUploadFileQuery)
from api_mcp.server import mcp_server

BASE_URL = "https://petstore3.swagger.io/api/v3"


@mcp_server.tool()
async def pet_put_update_pet(req_data: Pet, /) -> Optional[Pet]:

    async with aiohttp.ClientSession() as session:
        async with session.put(
            url=f"{BASE_URL}/pet", json=req_data.dict(exclude_unset=True)
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return Pet(**data)

            else:
                return None


@mcp_server.tool()
async def pet_post_add_pet(req_data: Pet, /) -> Optional[Pet]:

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=f"{BASE_URL}/pet", json=req_data.dict(exclude_unset=True)
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return Pet(**data)

            else:
                return None


@mcp_server.tool()
async def pet_get_find_pets_by_status(
    params: PetGetFindPetsByStatusQuery,
) -> Optional[list[Pet]]:

    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{BASE_URL}/pet/findByStatus",
            params=params.model_dump(exclude_unset=True),
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return [Pet(**obj) for obj in data]

            else:
                return None


@mcp_server.tool()
async def pet_get_find_pets_by_tags(
    params: PetGetFindPetsByTagsQuery,
) -> Optional[list[Pet]]:

    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{BASE_URL}/pet/findByTags",
            params=params.model_dump(exclude_unset=True),
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return [Pet(**obj) for obj in data]

            else:
                return None


@mcp_server.tool()
async def pet_get_get_pet_by_id(pet_id: int) -> Optional[Pet]:
    url = f"{BASE_URL}/pet/{pet_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=url,
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return Pet(**data)

            else:
                return None


@mcp_server.tool()
async def pet_post_update_pet_with_form(
    pet_id: int, params: PetPostUpdatePetWithFormQuery
) -> Optional[Pet]:
    url = f"{BASE_URL}/pet/{pet_id}"

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=url,
            params=params.model_dump(exclude_unset=True),
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return Pet(**data)

            else:
                return None


@mcp_server.tool()
async def pet_delete_delete_pet(
    pet_id: int, params: PetPostUpdatePetWithFormQuery
) -> Optional[Pet]:
    url = f"{BASE_URL}/pet/{pet_id}"

    async with aiohttp.ClientSession() as session:
        async with session.delete(
            url=url,
            params=params.model_dump(exclude_unset=True),
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return Pet(**data)

            else:
                return None


@mcp_server.tool()
async def pet_post_upload_file(
    pet_id: int, params: PetPostUploadFileQuery
) -> Optional[ApiResponse]:
    url = f"{BASE_URL}/pet/{pet_id}/uploadImage"

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=url,
            params=params.model_dump(exclude_unset=True),
        ) as resp:
            print(resp)
            if resp.ok:

                data = await resp.json()
                return ApiResponse(**data)

            else:
                return None
