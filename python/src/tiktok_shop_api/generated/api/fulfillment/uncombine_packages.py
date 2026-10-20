from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.uncombine_packages_request import UncombinePackagesRequest
from ...models.uncombine_packages_response import UncombinePackagesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    package_id: str,
    *,
    body: UncombinePackagesRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202309/packages/{package_id}/uncombine".format(
            package_id=quote(str(package_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UncombinePackagesResponse | None:
    if response.status_code == 200:
        response_200 = UncombinePackagesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UncombinePackagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UncombinePackagesRequest | Unset = UNSET,
) -> Response[UncombinePackagesResponse]:
    """Uncombine Packages

     Use this API to uncombine one or more orders from an already combined package.

    Args:
        package_id (str):
        body (UncombinePackagesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UncombinePackagesResponse]
    """

    kwargs = _get_kwargs(
        package_id=package_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UncombinePackagesRequest | Unset = UNSET,
) -> UncombinePackagesResponse | None:
    """Uncombine Packages

     Use this API to uncombine one or more orders from an already combined package.

    Args:
        package_id (str):
        body (UncombinePackagesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UncombinePackagesResponse
    """

    return sync_detailed(
        package_id=package_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UncombinePackagesRequest | Unset = UNSET,
) -> Response[UncombinePackagesResponse]:
    """Uncombine Packages

     Use this API to uncombine one or more orders from an already combined package.

    Args:
        package_id (str):
        body (UncombinePackagesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UncombinePackagesResponse]
    """

    kwargs = _get_kwargs(
        package_id=package_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UncombinePackagesRequest | Unset = UNSET,
) -> UncombinePackagesResponse | None:
    """Uncombine Packages

     Use this API to uncombine one or more orders from an already combined package.

    Args:
        package_id (str):
        body (UncombinePackagesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UncombinePackagesResponse
    """

    return (
        await asyncio_detailed(
            package_id=package_id,
            client=client,
            body=body,
        )
    ).parsed
