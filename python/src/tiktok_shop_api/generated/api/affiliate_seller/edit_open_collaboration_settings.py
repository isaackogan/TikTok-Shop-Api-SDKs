from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_open_collaboration_settings_request import EditOpenCollaborationSettingsRequest
from ...models.edit_open_collaboration_settings_response import EditOpenCollaborationSettingsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: EditOpenCollaborationSettingsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202405/open_collaboration_settings",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EditOpenCollaborationSettingsResponse | None:
    if response.status_code == 200:
        response_200 = EditOpenCollaborationSettingsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EditOpenCollaborationSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EditOpenCollaborationSettingsRequest | Unset = UNSET,
) -> Response[EditOpenCollaborationSettingsResponse]:
    """Edit Open Collaboration Settings

     This API is used to edit a Seller's open collaboration settings. It allows you to enroll your
    existing product catalog and all future products into an open collaboration plan. It also allows you
    to turn this setting off at any point. By default, this option is turned off for all Sellers.

    Args:
        body (EditOpenCollaborationSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditOpenCollaborationSettingsResponse]
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
    body: EditOpenCollaborationSettingsRequest | Unset = UNSET,
) -> EditOpenCollaborationSettingsResponse | None:
    """Edit Open Collaboration Settings

     This API is used to edit a Seller's open collaboration settings. It allows you to enroll your
    existing product catalog and all future products into an open collaboration plan. It also allows you
    to turn this setting off at any point. By default, this option is turned off for all Sellers.

    Args:
        body (EditOpenCollaborationSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditOpenCollaborationSettingsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EditOpenCollaborationSettingsRequest | Unset = UNSET,
) -> Response[EditOpenCollaborationSettingsResponse]:
    """Edit Open Collaboration Settings

     This API is used to edit a Seller's open collaboration settings. It allows you to enroll your
    existing product catalog and all future products into an open collaboration plan. It also allows you
    to turn this setting off at any point. By default, this option is turned off for all Sellers.

    Args:
        body (EditOpenCollaborationSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditOpenCollaborationSettingsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: EditOpenCollaborationSettingsRequest | Unset = UNSET,
) -> EditOpenCollaborationSettingsResponse | None:
    """Edit Open Collaboration Settings

     This API is used to edit a Seller's open collaboration settings. It allows you to enroll your
    existing product catalog and all future products into an open collaboration plan. It also allows you
    to turn this setting off at any point. By default, this option is turned off for all Sellers.

    Args:
        body (EditOpenCollaborationSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditOpenCollaborationSettingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
