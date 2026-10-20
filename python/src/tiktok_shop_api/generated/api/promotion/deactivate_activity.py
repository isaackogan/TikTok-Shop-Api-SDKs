from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.deactivate_activity_request import DeactivateActivityRequest
from ...models.deactivate_activity_response import DeactivateActivityResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    activity_id: str,
    *,
    body: DeactivateActivityRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/promotion/202309/activities/{activity_id}/deactivate".format(activity_id=quote(str(activity_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeactivateActivityResponse | None:
    if response.status_code == 200:
        response_200 = DeactivateActivityResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeactivateActivityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeactivateActivityRequest | Unset = UNSET,

) -> Response[DeactivateActivityResponse]:
    """ Deactivate Activity

     Deactivate an ongoing or upcoming activity.

    Args:
        activity_id (str):
        body (DeactivateActivityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeactivateActivityResponse]
     """


    kwargs = _get_kwargs(
        activity_id=activity_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeactivateActivityRequest | Unset = UNSET,

) -> DeactivateActivityResponse | None:
    """ Deactivate Activity

     Deactivate an ongoing or upcoming activity.

    Args:
        activity_id (str):
        body (DeactivateActivityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeactivateActivityResponse
     """


    return sync_detailed(
        activity_id=activity_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeactivateActivityRequest | Unset = UNSET,

) -> Response[DeactivateActivityResponse]:
    """ Deactivate Activity

     Deactivate an ongoing or upcoming activity.

    Args:
        activity_id (str):
        body (DeactivateActivityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeactivateActivityResponse]
     """


    kwargs = _get_kwargs(
        activity_id=activity_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeactivateActivityRequest | Unset = UNSET,

) -> DeactivateActivityResponse | None:
    """ Deactivate Activity

     Deactivate an ongoing or upcoming activity.

    Args:
        activity_id (str):
        body (DeactivateActivityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeactivateActivityResponse
     """


    return (await asyncio_detailed(
        activity_id=activity_id,
client=client,
body=body,

    )).parsed
