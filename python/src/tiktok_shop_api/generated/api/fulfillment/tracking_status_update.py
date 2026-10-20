from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.tracking_status_update_request import TrackingStatusUpdateRequest
from ...models.tracking_status_update_response import TrackingStatusUpdateResponse
from typing import cast



def _get_kwargs(
    *,
    body: TrackingStatusUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202609/order/sof/track/update",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TrackingStatusUpdateResponse | None:
    if response.status_code == 200:
        response_200 = TrackingStatusUpdateResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TrackingStatusUpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TrackingStatusUpdateRequest,

) -> Response[TrackingStatusUpdateResponse]:
    """ Tracking status update

     **This API is currently exclusive to the following markets: US, BR.**
    This API is suitable for merchants to deliver and carry orders by themselves, without shipping
    orders through third-party service providers, that is, without shipping packages through 3PL, but
    orders sent by merchants. Merchants are allowed to use this API to return such orders and update the
    order track. The Action Code and Failed Reason in the input parameter are enumerated, as detailed in
    the document: https://partner.tiktokshop.com/docv2/page/1cjht3qx

    Args:
        body (TrackingStatusUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrackingStatusUpdateResponse]
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
    body: TrackingStatusUpdateRequest,

) -> TrackingStatusUpdateResponse | None:
    """ Tracking status update

     **This API is currently exclusive to the following markets: US, BR.**
    This API is suitable for merchants to deliver and carry orders by themselves, without shipping
    orders through third-party service providers, that is, without shipping packages through 3PL, but
    orders sent by merchants. Merchants are allowed to use this API to return such orders and update the
    order track. The Action Code and Failed Reason in the input parameter are enumerated, as detailed in
    the document: https://partner.tiktokshop.com/docv2/page/1cjht3qx

    Args:
        body (TrackingStatusUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrackingStatusUpdateResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TrackingStatusUpdateRequest,

) -> Response[TrackingStatusUpdateResponse]:
    """ Tracking status update

     **This API is currently exclusive to the following markets: US, BR.**
    This API is suitable for merchants to deliver and carry orders by themselves, without shipping
    orders through third-party service providers, that is, without shipping packages through 3PL, but
    orders sent by merchants. Merchants are allowed to use this API to return such orders and update the
    order track. The Action Code and Failed Reason in the input parameter are enumerated, as detailed in
    the document: https://partner.tiktokshop.com/docv2/page/1cjht3qx

    Args:
        body (TrackingStatusUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrackingStatusUpdateResponse]
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
    body: TrackingStatusUpdateRequest,

) -> TrackingStatusUpdateResponse | None:
    """ Tracking status update

     **This API is currently exclusive to the following markets: US, BR.**
    This API is suitable for merchants to deliver and carry orders by themselves, without shipping
    orders through third-party service providers, that is, without shipping packages through 3PL, but
    orders sent by merchants. Merchants are allowed to use this API to return such orders and update the
    order track. The Action Code and Failed Reason in the input parameter are enumerated, as detailed in
    the document: https://partner.tiktokshop.com/docv2/page/1cjht3qx

    Args:
        body (TrackingStatusUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrackingStatusUpdateResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
