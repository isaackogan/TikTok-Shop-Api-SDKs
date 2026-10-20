from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_fbt_merchant_onboarded_regions_response import GetFBTMerchantOnboardedRegionsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fbt/202409/merchants/onboarded_regions",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetFBTMerchantOnboardedRegionsResponse | None:
    if response.status_code == 200:
        response_200 = GetFBTMerchantOnboardedRegionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetFBTMerchantOnboardedRegionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetFBTMerchantOnboardedRegionsResponse]:
    """Get FBT Merchant Onboarded Regions

     This API verifies whether a seller is registered as a Fulfillment by TikTok (FBT) merchant. If the
    seller is onboarded, the API returns the regions where the merchant is authorized to operate under
    the FBT system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFBTMerchantOnboardedRegionsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetFBTMerchantOnboardedRegionsResponse | None:
    """Get FBT Merchant Onboarded Regions

     This API verifies whether a seller is registered as a Fulfillment by TikTok (FBT) merchant. If the
    seller is onboarded, the API returns the regions where the merchant is authorized to operate under
    the FBT system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFBTMerchantOnboardedRegionsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetFBTMerchantOnboardedRegionsResponse]:
    """Get FBT Merchant Onboarded Regions

     This API verifies whether a seller is registered as a Fulfillment by TikTok (FBT) merchant. If the
    seller is onboarded, the API returns the regions where the merchant is authorized to operate under
    the FBT system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFBTMerchantOnboardedRegionsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetFBTMerchantOnboardedRegionsResponse | None:
    """Get FBT Merchant Onboarded Regions

     This API verifies whether a seller is registered as a Fulfillment by TikTok (FBT) merchant. If the
    seller is onboarded, the API returns the regions where the merchant is authorized to operate under
    the FBT system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFBTMerchantOnboardedRegionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
