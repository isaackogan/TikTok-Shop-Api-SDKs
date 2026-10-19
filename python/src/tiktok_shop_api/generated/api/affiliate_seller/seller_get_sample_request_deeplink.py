from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.seller_get_sample_request_deeplink_response import SellerGetSampleRequestDeeplinkResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    product_id: str,
    sku_id: str,
    campaign_id: str | Unset = UNSET,
    collaboration_id: str | Unset = UNSET,
    valid_days: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["product_id"] = product_id

    params["sku_id"] = sku_id

    params["campaign_id"] = campaign_id

    params["collaboration_id"] = collaboration_id

    params["valid_days"] = valid_days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202512/sample_applications/deeplink",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SellerGetSampleRequestDeeplinkResponse | None:
    if response.status_code == 200:
        response_200 = SellerGetSampleRequestDeeplinkResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SellerGetSampleRequestDeeplinkResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,
    sku_id: str,
    campaign_id: str | Unset = UNSET,
    collaboration_id: str | Unset = UNSET,
    valid_days: int | Unset = UNSET,
) -> Response[SellerGetSampleRequestDeeplinkResponse]:
    """Seller Get Sample Request Deeplink

     Use this API to get a TikTok deeplink, use this deeplink to launch the TikTok app and land the user
    on the sample request page.
    - The seller can encode the deeplink into an QR code and send it to a creator via email.

    Args:
        product_id (str):
        sku_id (str):
        campaign_id (str | Unset):
        collaboration_id (str | Unset):
        valid_days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SellerGetSampleRequestDeeplinkResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        sku_id=sku_id,
        campaign_id=campaign_id,
        collaboration_id=collaboration_id,
        valid_days=valid_days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,
    sku_id: str,
    campaign_id: str | Unset = UNSET,
    collaboration_id: str | Unset = UNSET,
    valid_days: int | Unset = UNSET,
) -> SellerGetSampleRequestDeeplinkResponse | None:
    """Seller Get Sample Request Deeplink

     Use this API to get a TikTok deeplink, use this deeplink to launch the TikTok app and land the user
    on the sample request page.
    - The seller can encode the deeplink into an QR code and send it to a creator via email.

    Args:
        product_id (str):
        sku_id (str):
        campaign_id (str | Unset):
        collaboration_id (str | Unset):
        valid_days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SellerGetSampleRequestDeeplinkResponse
    """

    return sync_detailed(
        client=client,
        product_id=product_id,
        sku_id=sku_id,
        campaign_id=campaign_id,
        collaboration_id=collaboration_id,
        valid_days=valid_days,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,
    sku_id: str,
    campaign_id: str | Unset = UNSET,
    collaboration_id: str | Unset = UNSET,
    valid_days: int | Unset = UNSET,
) -> Response[SellerGetSampleRequestDeeplinkResponse]:
    """Seller Get Sample Request Deeplink

     Use this API to get a TikTok deeplink, use this deeplink to launch the TikTok app and land the user
    on the sample request page.
    - The seller can encode the deeplink into an QR code and send it to a creator via email.

    Args:
        product_id (str):
        sku_id (str):
        campaign_id (str | Unset):
        collaboration_id (str | Unset):
        valid_days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SellerGetSampleRequestDeeplinkResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        sku_id=sku_id,
        campaign_id=campaign_id,
        collaboration_id=collaboration_id,
        valid_days=valid_days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,
    sku_id: str,
    campaign_id: str | Unset = UNSET,
    collaboration_id: str | Unset = UNSET,
    valid_days: int | Unset = UNSET,
) -> SellerGetSampleRequestDeeplinkResponse | None:
    """Seller Get Sample Request Deeplink

     Use this API to get a TikTok deeplink, use this deeplink to launch the TikTok app and land the user
    on the sample request page.
    - The seller can encode the deeplink into an QR code and send it to a creator via email.

    Args:
        product_id (str):
        sku_id (str):
        campaign_id (str | Unset):
        collaboration_id (str | Unset):
        valid_days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SellerGetSampleRequestDeeplinkResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            product_id=product_id,
            sku_id=sku_id,
            campaign_id=campaign_id,
            collaboration_id=collaboration_id,
            valid_days=valid_days,
        )
    ).parsed
