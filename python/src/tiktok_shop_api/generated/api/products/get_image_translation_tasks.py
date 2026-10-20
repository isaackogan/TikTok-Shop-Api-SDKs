from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_image_translation_tasks_response import GetImageTranslationTasksResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    translation_task_ids: list[str] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_translation_task_ids: list[str] | Unset = UNSET
    if not isinstance(translation_task_ids, Unset):
        json_translation_task_ids = translation_task_ids


    params["translation_task_ids"] = json_translation_task_ids


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202506/images/translation_tasks",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetImageTranslationTasksResponse | None:
    if response.status_code == 200:
        response_200 = GetImageTranslationTasksResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetImageTranslationTasksResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    translation_task_ids: list[str] | Unset = UNSET,

) -> Response[GetImageTranslationTasksResponse]:
    """ Get Image Translation Tasks

     Retrieves the image translation task status and translated images for one or more previously
    submitted images.
    **Note**: Please wait 5 minutes after [task creation](684f8b2d6e0b37048b2448b4) before calling this
    API, and retry at intervals over 10 seconds to avoid rate limiting.
    Applicable only for sellers that sell across EU.

    Args:
        translation_task_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetImageTranslationTasksResponse]
     """


    kwargs = _get_kwargs(
        translation_task_ids=translation_task_ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    translation_task_ids: list[str] | Unset = UNSET,

) -> GetImageTranslationTasksResponse | None:
    """ Get Image Translation Tasks

     Retrieves the image translation task status and translated images for one or more previously
    submitted images.
    **Note**: Please wait 5 minutes after [task creation](684f8b2d6e0b37048b2448b4) before calling this
    API, and retry at intervals over 10 seconds to avoid rate limiting.
    Applicable only for sellers that sell across EU.

    Args:
        translation_task_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetImageTranslationTasksResponse
     """


    return sync_detailed(
        client=client,
translation_task_ids=translation_task_ids,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    translation_task_ids: list[str] | Unset = UNSET,

) -> Response[GetImageTranslationTasksResponse]:
    """ Get Image Translation Tasks

     Retrieves the image translation task status and translated images for one or more previously
    submitted images.
    **Note**: Please wait 5 minutes after [task creation](684f8b2d6e0b37048b2448b4) before calling this
    API, and retry at intervals over 10 seconds to avoid rate limiting.
    Applicable only for sellers that sell across EU.

    Args:
        translation_task_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetImageTranslationTasksResponse]
     """


    kwargs = _get_kwargs(
        translation_task_ids=translation_task_ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    translation_task_ids: list[str] | Unset = UNSET,

) -> GetImageTranslationTasksResponse | None:
    """ Get Image Translation Tasks

     Retrieves the image translation task status and translated images for one or more previously
    submitted images.
    **Note**: Please wait 5 minutes after [task creation](684f8b2d6e0b37048b2448b4) before calling this
    API, and retry at intervals over 10 seconds to avoid rate limiting.
    Applicable only for sellers that sell across EU.

    Args:
        translation_task_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetImageTranslationTasksResponse
     """


    return (await asyncio_detailed(
        client=client,
translation_task_ids=translation_task_ids,

    )).parsed
