from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_price_request import UpdatePriceRequest
from ...models.update_price_response import UpdatePriceResponse
from typing import cast



def _get_kwargs(
    product_id: str,
    *,
    body: UpdatePriceRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/products/{product_id}/prices/update".format(product_id=quote(str(product_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdatePriceResponse | None:
    if response.status_code == 200:
        response_200 = UpdatePriceResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdatePriceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePriceRequest,

) -> Response[UpdatePriceResponse]:
    """ Update Price

     Update the price of multiple SKUs belonging to a product in the `ACTIVATE` status and not included
    in any ongoing promotions.
    **Note**: The `data` response field is always empty as there is no additional response data.

    Args:
        product_id (str):
        body (UpdatePriceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePriceResponse]
     """


    kwargs = _get_kwargs(
        product_id=product_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePriceRequest,

) -> UpdatePriceResponse | None:
    """ Update Price

     Update the price of multiple SKUs belonging to a product in the `ACTIVATE` status and not included
    in any ongoing promotions.
    **Note**: The `data` response field is always empty as there is no additional response data.

    Args:
        product_id (str):
        body (UpdatePriceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePriceResponse
     """


    return sync_detailed(
        product_id=product_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePriceRequest,

) -> Response[UpdatePriceResponse]:
    """ Update Price

     Update the price of multiple SKUs belonging to a product in the `ACTIVATE` status and not included
    in any ongoing promotions.
    **Note**: The `data` response field is always empty as there is no additional response data.

    Args:
        product_id (str):
        body (UpdatePriceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePriceResponse]
     """


    kwargs = _get_kwargs(
        product_id=product_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePriceRequest,

) -> UpdatePriceResponse | None:
    """ Update Price

     Update the price of multiple SKUs belonging to a product in the `ACTIVATE` status and not included
    in any ongoing promotions.
    **Note**: The `data` response field is always empty as there is no additional response data.

    Args:
        product_id (str):
        body (UpdatePriceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePriceResponse
     """


    return (await asyncio_detailed(
        product_id=product_id,
client=client,
body=body,

    )).parsed
