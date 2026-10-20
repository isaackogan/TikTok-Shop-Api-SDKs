from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.check_tik_tok_shipping_and_collection_by_tik_tok_coverage_response import CheckTikTokShippingAndCollectionByTikTokCoverageResponse
from typing import cast



def _get_kwargs(
    *,
    tracking_number: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["tracking_number"] = tracking_number


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fulfillment/202508/tts_tracking_validation",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CheckTikTokShippingAndCollectionByTikTokCoverageResponse | None:
    if response.status_code == 200:
        response_200 = CheckTikTokShippingAndCollectionByTikTokCoverageResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CheckTikTokShippingAndCollectionByTikTokCoverageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    tracking_number: str,

) -> Response[CheckTikTokShippingAndCollectionByTikTokCoverageResponse]:
    """ Check TikTok Shipping and Collection by TikTok Coverage

     Enables a seller or warehouse to validate whether a tracking number is covered by TikTok Shipping
    (TTS) or Collection by TikTok (CBT).

    Available only in the **US Market**.

    Args:
        tracking_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckTikTokShippingAndCollectionByTikTokCoverageResponse]
     """


    kwargs = _get_kwargs(
        tracking_number=tracking_number,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    tracking_number: str,

) -> CheckTikTokShippingAndCollectionByTikTokCoverageResponse | None:
    """ Check TikTok Shipping and Collection by TikTok Coverage

     Enables a seller or warehouse to validate whether a tracking number is covered by TikTok Shipping
    (TTS) or Collection by TikTok (CBT).

    Available only in the **US Market**.

    Args:
        tracking_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckTikTokShippingAndCollectionByTikTokCoverageResponse
     """


    return sync_detailed(
        client=client,
tracking_number=tracking_number,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    tracking_number: str,

) -> Response[CheckTikTokShippingAndCollectionByTikTokCoverageResponse]:
    """ Check TikTok Shipping and Collection by TikTok Coverage

     Enables a seller or warehouse to validate whether a tracking number is covered by TikTok Shipping
    (TTS) or Collection by TikTok (CBT).

    Available only in the **US Market**.

    Args:
        tracking_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckTikTokShippingAndCollectionByTikTokCoverageResponse]
     """


    kwargs = _get_kwargs(
        tracking_number=tracking_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    tracking_number: str,

) -> CheckTikTokShippingAndCollectionByTikTokCoverageResponse | None:
    """ Check TikTok Shipping and Collection by TikTok Coverage

     Enables a seller or warehouse to validate whether a tracking number is covered by TikTok Shipping
    (TTS) or Collection by TikTok (CBT).

    Available only in the **US Market**.

    Args:
        tracking_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckTikTokShippingAndCollectionByTikTokCoverageResponse
     """


    return (await asyncio_detailed(
        client=client,
tracking_number=tracking_number,

    )).parsed
