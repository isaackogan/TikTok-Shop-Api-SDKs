from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_message_templates_response import GetMessageTemplatesResponse
from typing import cast



def _get_kwargs(
    *,
    locale: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customer_engagement/202412/message_templates",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetMessageTemplatesResponse | None:
    if response.status_code == 200:
        response_200 = GetMessageTemplatesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetMessageTemplatesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: str,

) -> Response[GetMessageTemplatesResponse]:
    """ Get Message Templates

     Get a library of customer engagement message templates predefined by TikTok Shop, which you can use
    directly in your customer engagement communications.

    Args:
        locale (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMessageTemplatesResponse]
     """


    kwargs = _get_kwargs(
        locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    locale: str,

) -> GetMessageTemplatesResponse | None:
    """ Get Message Templates

     Get a library of customer engagement message templates predefined by TikTok Shop, which you can use
    directly in your customer engagement communications.

    Args:
        locale (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMessageTemplatesResponse
     """


    return sync_detailed(
        client=client,
locale=locale,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: str,

) -> Response[GetMessageTemplatesResponse]:
    """ Get Message Templates

     Get a library of customer engagement message templates predefined by TikTok Shop, which you can use
    directly in your customer engagement communications.

    Args:
        locale (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMessageTemplatesResponse]
     """


    kwargs = _get_kwargs(
        locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    locale: str,

) -> GetMessageTemplatesResponse | None:
    """ Get Message Templates

     Get a library of customer engagement message templates predefined by TikTok Shop, which you can use
    directly in your customer engagement communications.

    Args:
        locale (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMessageTemplatesResponse
     """


    return (await asyncio_detailed(
        client=client,
locale=locale,

    )).parsed
