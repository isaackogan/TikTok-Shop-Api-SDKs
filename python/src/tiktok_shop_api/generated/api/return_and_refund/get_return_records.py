from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_return_records_response import GetReturnRecordsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    return_id: str,
    *,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/return_refund/202309/returns/{return_id}/records".format(return_id=quote(str(return_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetReturnRecordsResponse | None:
    if response.status_code == 200:
        response_200 = GetReturnRecordsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetReturnRecordsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    return_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Response[GetReturnRecordsResponse]:
    """ Get Return Records

     Use this API to retrieve the record entries for a specific return request. Each item in data.records
    represents an action or lifecycle event for the specified return_id.

    Args:
        return_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReturnRecordsResponse]
     """


    kwargs = _get_kwargs(
        return_id=return_id,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    return_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> GetReturnRecordsResponse | None:
    """ Get Return Records

     Use this API to retrieve the record entries for a specific return request. Each item in data.records
    represents an action or lifecycle event for the specified return_id.

    Args:
        return_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReturnRecordsResponse
     """


    return sync_detailed(
        return_id=return_id,
client=client,
locale=locale,

    ).parsed

async def asyncio_detailed(
    return_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Response[GetReturnRecordsResponse]:
    """ Get Return Records

     Use this API to retrieve the record entries for a specific return request. Each item in data.records
    represents an action or lifecycle event for the specified return_id.

    Args:
        return_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReturnRecordsResponse]
     """


    kwargs = _get_kwargs(
        return_id=return_id,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    return_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> GetReturnRecordsResponse | None:
    """ Get Return Records

     Use this API to retrieve the record entries for a specific return request. Each item in data.records
    represents an action or lifecycle event for the specified return_id.

    Args:
        return_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReturnRecordsResponse
     """


    return (await asyncio_detailed(
        return_id=return_id,
client=client,
locale=locale,

    )).parsed
