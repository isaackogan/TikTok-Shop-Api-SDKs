from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_activity_response import GetActivityResponse
from ...types import Response


def _get_kwargs(
    activity_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/promotion/202309/activities/{activity_id}".format(
            activity_id=quote(str(activity_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetActivityResponse | None:
    if response.status_code == 200:
        response_200 = GetActivityResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetActivityResponse]:
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
) -> Response[GetActivityResponse]:
    """Get Activity

     Get the details of a promotion activity. Product information for `FIXED_PRICE`, `DIRECT_DISCOUNT`,
    and `FLASHSALE` activities that ended more than 180 days ago will not be returned. For coupon
    activities, use [Get Coupon](6699dce0de15e502ed219e37).

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetActivityResponse]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetActivityResponse | None:
    """Get Activity

     Get the details of a promotion activity. Product information for `FIXED_PRICE`, `DIRECT_DISCOUNT`,
    and `FLASHSALE` activities that ended more than 180 days ago will not be returned. For coupon
    activities, use [Get Coupon](6699dce0de15e502ed219e37).

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetActivityResponse
    """

    return sync_detailed(
        activity_id=activity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetActivityResponse]:
    """Get Activity

     Get the details of a promotion activity. Product information for `FIXED_PRICE`, `DIRECT_DISCOUNT`,
    and `FLASHSALE` activities that ended more than 180 days ago will not be returned. For coupon
    activities, use [Get Coupon](6699dce0de15e502ed219e37).

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetActivityResponse]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetActivityResponse | None:
    """Get Activity

     Get the details of a promotion activity. Product information for `FIXED_PRICE`, `DIRECT_DISCOUNT`,
    and `FLASHSALE` activities that ended more than 180 days ago will not be returned. For coupon
    activities, use [Get Coupon](6699dce0de15e502ed219e37).

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetActivityResponse
    """

    return (
        await asyncio_detailed(
            activity_id=activity_id,
            client=client,
        )
    ).parsed
