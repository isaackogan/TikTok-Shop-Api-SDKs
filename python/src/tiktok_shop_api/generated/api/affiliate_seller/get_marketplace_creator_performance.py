from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_marketplace_creator_performance_data_groups_item import (
    GetMarketplaceCreatorPerformanceDataGroupsItem,
)
from ...models.get_marketplace_creator_performance_response import GetMarketplaceCreatorPerformanceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    creator_user_id: str,
    *,
    data_groups: list[GetMarketplaceCreatorPerformanceDataGroupsItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_data_groups: list[str] | Unset = UNSET
    if not isinstance(data_groups, Unset):
        json_data_groups = []
        for data_groups_item_data in data_groups:
            data_groups_item = data_groups_item_data.value
            json_data_groups.append(data_groups_item)

    params["data_groups"] = json_data_groups

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202608/marketplace_creators/{creator_user_id}".format(
            creator_user_id=quote(str(creator_user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetMarketplaceCreatorPerformanceResponse | None:
    if response.status_code == 200:
        response_200 = GetMarketplaceCreatorPerformanceResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetMarketplaceCreatorPerformanceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    creator_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_groups: list[GetMarketplaceCreatorPerformanceDataGroupsItem] | Unset = UNSET,
) -> Response[GetMarketplaceCreatorPerformanceResponse]:
    """Get Marketplace Creator Performance

     Returns marketplace information and performance metrics for the specified creator.

    Args:
        creator_user_id (str):
        data_groups (list[GetMarketplaceCreatorPerformanceDataGroupsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketplaceCreatorPerformanceResponse]
    """

    kwargs = _get_kwargs(
        creator_user_id=creator_user_id,
        data_groups=data_groups,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    creator_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_groups: list[GetMarketplaceCreatorPerformanceDataGroupsItem] | Unset = UNSET,
) -> GetMarketplaceCreatorPerformanceResponse | None:
    """Get Marketplace Creator Performance

     Returns marketplace information and performance metrics for the specified creator.

    Args:
        creator_user_id (str):
        data_groups (list[GetMarketplaceCreatorPerformanceDataGroupsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketplaceCreatorPerformanceResponse
    """

    return sync_detailed(
        creator_user_id=creator_user_id,
        client=client,
        data_groups=data_groups,
    ).parsed


async def asyncio_detailed(
    creator_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_groups: list[GetMarketplaceCreatorPerformanceDataGroupsItem] | Unset = UNSET,
) -> Response[GetMarketplaceCreatorPerformanceResponse]:
    """Get Marketplace Creator Performance

     Returns marketplace information and performance metrics for the specified creator.

    Args:
        creator_user_id (str):
        data_groups (list[GetMarketplaceCreatorPerformanceDataGroupsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketplaceCreatorPerformanceResponse]
    """

    kwargs = _get_kwargs(
        creator_user_id=creator_user_id,
        data_groups=data_groups,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    creator_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_groups: list[GetMarketplaceCreatorPerformanceDataGroupsItem] | Unset = UNSET,
) -> GetMarketplaceCreatorPerformanceResponse | None:
    """Get Marketplace Creator Performance

     Returns marketplace information and performance metrics for the specified creator.

    Args:
        creator_user_id (str):
        data_groups (list[GetMarketplaceCreatorPerformanceDataGroupsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketplaceCreatorPerformanceResponse
    """

    return (
        await asyncio_detailed(
            creator_user_id=creator_user_id,
            client=client,
            data_groups=data_groups,
        )
    ).parsed
