from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_fbt_merchant_mcf_status_response import GetFBTMerchantMCFStatusResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fbt/202601/merchants/mcf_status",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetFBTMerchantMCFStatusResponse | None:
    if response.status_code == 200:
        response_200 = GetFBTMerchantMCFStatusResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetFBTMerchantMCFStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetFBTMerchantMCFStatusResponse]:
    """ Get FBT Merchant MCF Status

     Checks whether a seller is onboarded to Fulfillment by TikTok (FBT) and enrolled in Multi-Channel
    Fulfillment (MCF). This API currently supports only sellers in the US. If both conditions are met,
    `mcf_status.is_mcf` is `1` (active).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFBTMerchantMCFStatusResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> GetFBTMerchantMCFStatusResponse | None:
    """ Get FBT Merchant MCF Status

     Checks whether a seller is onboarded to Fulfillment by TikTok (FBT) and enrolled in Multi-Channel
    Fulfillment (MCF). This API currently supports only sellers in the US. If both conditions are met,
    `mcf_status.is_mcf` is `1` (active).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFBTMerchantMCFStatusResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetFBTMerchantMCFStatusResponse]:
    """ Get FBT Merchant MCF Status

     Checks whether a seller is onboarded to Fulfillment by TikTok (FBT) and enrolled in Multi-Channel
    Fulfillment (MCF). This API currently supports only sellers in the US. If both conditions are met,
    `mcf_status.is_mcf` is `1` (active).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFBTMerchantMCFStatusResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> GetFBTMerchantMCFStatusResponse | None:
    """ Get FBT Merchant MCF Status

     Checks whether a seller is onboarded to Fulfillment by TikTok (FBT) and enrolled in Multi-Channel
    Fulfillment (MCF). This API currently supports only sellers in the US. If both conditions are met,
    `mcf_status.is_mcf` is `1` (active).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFBTMerchantMCFStatusResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
