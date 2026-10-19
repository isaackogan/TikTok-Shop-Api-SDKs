from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_package_handover_time_slots_response import GetPackageHandoverTimeSlotsResponse
from ...types import Response


def _get_kwargs(
    package_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fulfillment/202309/packages/{package_id}/handover_time_slots".format(
            package_id=quote(str(package_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPackageHandoverTimeSlotsResponse | None:
    if response.status_code == 200:
        response_200 = GetPackageHandoverTimeSlotsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPackageHandoverTimeSlotsResponse]:
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
) -> Response[GetPackageHandoverTimeSlotsResponse]:
    """Get Package Handover Time Slots

     Use this API to retrieve a specified package's door-to-door pickup time slots and handover
    availability for pickup, drop-off, and, in the UK, van collection. When available, the response also
    provides a URL for finding drop-off locations.

    Args:
        package_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPackageHandoverTimeSlotsResponse]
    """

    kwargs = _get_kwargs(
        package_id=package_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetPackageHandoverTimeSlotsResponse | None:
    """Get Package Handover Time Slots

     Use this API to retrieve a specified package's door-to-door pickup time slots and handover
    availability for pickup, drop-off, and, in the UK, van collection. When available, the response also
    provides a URL for finding drop-off locations.

    Args:
        package_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPackageHandoverTimeSlotsResponse
    """

    return sync_detailed(
        package_id=package_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPackageHandoverTimeSlotsResponse]:
    """Get Package Handover Time Slots

     Use this API to retrieve a specified package's door-to-door pickup time slots and handover
    availability for pickup, drop-off, and, in the UK, van collection. When available, the response also
    provides a URL for finding drop-off locations.

    Args:
        package_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPackageHandoverTimeSlotsResponse]
    """

    kwargs = _get_kwargs(
        package_id=package_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetPackageHandoverTimeSlotsResponse | None:
    """Get Package Handover Time Slots

     Use this API to retrieve a specified package's door-to-door pickup time slots and handover
    availability for pickup, drop-off, and, in the UK, van collection. When available, the response also
    provides a URL for finding drop-off locations.

    Args:
        package_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPackageHandoverTimeSlotsResponse
    """

    return (
        await asyncio_detailed(
            package_id=package_id,
            client=client,
        )
    ).parsed
