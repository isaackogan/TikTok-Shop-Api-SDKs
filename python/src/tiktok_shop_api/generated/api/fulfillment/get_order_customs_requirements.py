from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_order_customs_requirements_request import GetOrderCustomsRequirementsRequest
from ...models.get_order_customs_requirements_response import GetOrderCustomsRequirementsResponse
from typing import cast



def _get_kwargs(
    *,
    body: GetOrderCustomsRequirementsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202607/orders/customs_info/query",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOrderCustomsRequirementsResponse | None:
    if response.status_code == 200:
        response_200 = GetOrderCustomsRequirementsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOrderCustomsRequirementsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetOrderCustomsRequirementsRequest,

) -> Response[GetOrderCustomsRequirementsResponse]:
    """ Get Order Customs Requirements

     This API is used to query whether an order requires extra customs clearance information, whether
    such information has been submitted, and the list of submitted customs clearance information.
    If extra customs clearance information is required but not yet provided, the merchant must complete
    and submit it before shipment can proceed.

    Args:
        body (GetOrderCustomsRequirementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderCustomsRequirementsResponse]
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
    body: GetOrderCustomsRequirementsRequest,

) -> GetOrderCustomsRequirementsResponse | None:
    """ Get Order Customs Requirements

     This API is used to query whether an order requires extra customs clearance information, whether
    such information has been submitted, and the list of submitted customs clearance information.
    If extra customs clearance information is required but not yet provided, the merchant must complete
    and submit it before shipment can proceed.

    Args:
        body (GetOrderCustomsRequirementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrderCustomsRequirementsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetOrderCustomsRequirementsRequest,

) -> Response[GetOrderCustomsRequirementsResponse]:
    """ Get Order Customs Requirements

     This API is used to query whether an order requires extra customs clearance information, whether
    such information has been submitted, and the list of submitted customs clearance information.
    If extra customs clearance information is required but not yet provided, the merchant must complete
    and submit it before shipment can proceed.

    Args:
        body (GetOrderCustomsRequirementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderCustomsRequirementsResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetOrderCustomsRequirementsRequest,

) -> GetOrderCustomsRequirementsResponse | None:
    """ Get Order Customs Requirements

     This API is used to query whether an order requires extra customs clearance information, whether
    such information has been submitted, and the list of submitted customs clearance information.
    If extra customs clearance information is required but not yet provided, the merchant must complete
    and submit it before shipment can proceed.

    Args:
        body (GetOrderCustomsRequirementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrderCustomsRequirementsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
