from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_authorized_shops_response import GetAuthorizedShopsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/authorization/202309/shops",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAuthorizedShopsResponse | None:
    if response.status_code == 200:
        response_200 = GetAuthorizedShopsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAuthorizedShopsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAuthorizedShopsResponse]:
    """Get Authorized Shops

     Retrieves the list of shops that a seller has authorized for an app.
    Seller authorization is required before an app can access the data of a shop. Use this API to check
    which shops are currently authorized for an app and obtain the corresponding shop cipher for use as
    an input parameter in shop related APIs.
    For more information about seller authorization, refer to [Seller authorization
    guide](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0).
    Target seller: All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAuthorizedShopsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetAuthorizedShopsResponse | None:
    """Get Authorized Shops

     Retrieves the list of shops that a seller has authorized for an app.
    Seller authorization is required before an app can access the data of a shop. Use this API to check
    which shops are currently authorized for an app and obtain the corresponding shop cipher for use as
    an input parameter in shop related APIs.
    For more information about seller authorization, refer to [Seller authorization
    guide](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0).
    Target seller: All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAuthorizedShopsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAuthorizedShopsResponse]:
    """Get Authorized Shops

     Retrieves the list of shops that a seller has authorized for an app.
    Seller authorization is required before an app can access the data of a shop. Use this API to check
    which shops are currently authorized for an app and obtain the corresponding shop cipher for use as
    an input parameter in shop related APIs.
    For more information about seller authorization, refer to [Seller authorization
    guide](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0).
    Target seller: All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAuthorizedShopsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetAuthorizedShopsResponse | None:
    """Get Authorized Shops

     Retrieves the list of shops that a seller has authorized for an app.
    Seller authorization is required before an app can access the data of a shop. Use this API to check
    which shops are currently authorized for an app and obtain the corresponding shop cipher for use as
    an input parameter in shop related APIs.
    For more information about seller authorization, refer to [Seller authorization
    guide](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0).
    Target seller: All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAuthorizedShopsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
