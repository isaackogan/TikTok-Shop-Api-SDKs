from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_image_translation_tasks_request import CreateImageTranslationTasksRequest
from ...models.create_image_translation_tasks_response import CreateImageTranslationTasksResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreateImageTranslationTasksRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202505/images/translation_tasks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateImageTranslationTasksResponse | None:
    if response.status_code == 200:
        response_200 = CreateImageTranslationTasksResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateImageTranslationTasksResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateImageTranslationTasksRequest,

) -> Response[CreateImageTranslationTasksResponse]:
    """ Create Image Translation Tasks

     Initiates a translation task for one or more images. This asynchronous API queues the images for
    processing in the specified target language.
    Applicable only for sellers that sell across EU.
    Use the [Image Translation Completed webhook](684f8d9bcc4e44049347a12e) to monitor the translation
    progress, or pass the task ID to the [Get Image Translation Tasks API](684f8b2d535a9d048f234564) to
    retrieve the status and the translated images.
    **Note**:
    - Please wait 5 minutes after task creation before calling the Get endpoint, and retry at intervals
    over 10 seconds to avoid rate limiting.
    - Each task corresponds to the translation of 1 image into 1 target language.
    - You can create up to 20 tasks per call and 500 tasks per day. Any tasks beyond the daily limit
    will be rejected.

    Args:
        body (CreateImageTranslationTasksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateImageTranslationTasksResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateImageTranslationTasksRequest,

) -> CreateImageTranslationTasksResponse | None:
    """ Create Image Translation Tasks

     Initiates a translation task for one or more images. This asynchronous API queues the images for
    processing in the specified target language.
    Applicable only for sellers that sell across EU.
    Use the [Image Translation Completed webhook](684f8d9bcc4e44049347a12e) to monitor the translation
    progress, or pass the task ID to the [Get Image Translation Tasks API](684f8b2d535a9d048f234564) to
    retrieve the status and the translated images.
    **Note**:
    - Please wait 5 minutes after task creation before calling the Get endpoint, and retry at intervals
    over 10 seconds to avoid rate limiting.
    - Each task corresponds to the translation of 1 image into 1 target language.
    - You can create up to 20 tasks per call and 500 tasks per day. Any tasks beyond the daily limit
    will be rejected.

    Args:
        body (CreateImageTranslationTasksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateImageTranslationTasksResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateImageTranslationTasksRequest,

) -> Response[CreateImageTranslationTasksResponse]:
    """ Create Image Translation Tasks

     Initiates a translation task for one or more images. This asynchronous API queues the images for
    processing in the specified target language.
    Applicable only for sellers that sell across EU.
    Use the [Image Translation Completed webhook](684f8d9bcc4e44049347a12e) to monitor the translation
    progress, or pass the task ID to the [Get Image Translation Tasks API](684f8b2d535a9d048f234564) to
    retrieve the status and the translated images.
    **Note**:
    - Please wait 5 minutes after task creation before calling the Get endpoint, and retry at intervals
    over 10 seconds to avoid rate limiting.
    - Each task corresponds to the translation of 1 image into 1 target language.
    - You can create up to 20 tasks per call and 500 tasks per day. Any tasks beyond the daily limit
    will be rejected.

    Args:
        body (CreateImageTranslationTasksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateImageTranslationTasksResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateImageTranslationTasksRequest,

) -> CreateImageTranslationTasksResponse | None:
    """ Create Image Translation Tasks

     Initiates a translation task for one or more images. This asynchronous API queues the images for
    processing in the specified target language.
    Applicable only for sellers that sell across EU.
    Use the [Image Translation Completed webhook](684f8d9bcc4e44049347a12e) to monitor the translation
    progress, or pass the task ID to the [Get Image Translation Tasks API](684f8b2d535a9d048f234564) to
    retrieve the status and the translated images.
    **Note**:
    - Please wait 5 minutes after task creation before calling the Get endpoint, and retry at intervals
    over 10 seconds to avoid rate limiting.
    - Each task corresponds to the translation of 1 image into 1 target language.
    - You can create up to 20 tasks per call and 500 tasks per day. Any tasks beyond the daily limit
    will be rejected.

    Args:
        body (CreateImageTranslationTasksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateImageTranslationTasksResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
