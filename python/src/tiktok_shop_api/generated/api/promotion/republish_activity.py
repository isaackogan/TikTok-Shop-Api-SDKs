from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.republish_activity_request import RepublishActivityRequest
from ...models.republish_activity_response import RepublishActivityResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    activity_id: str,
    *,
    body: RepublishActivityRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/promotion/202607/activities/{activity_id}/republish".format(activity_id=quote(str(activity_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RepublishActivityResponse | None:
    if response.status_code == 200:
        response_200 = RepublishActivityResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RepublishActivityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RepublishActivityRequest | Unset = UNSET,

) -> Response[RepublishActivityResponse]:
    """ Republish Activity

     Use this API to republish a product discount activity or a flash deal activity that expired or was
    deactivated within the last 7 days. This API only supports FIXED_PRICE, FLASHSALE, and
    DIRECT_DISCOUNT activities. You must provide a new effective period by passing the new begin_time
    and end_time. Products and SKUs already associated with the activity do not need to be added again.
    After the activity is republished, you can edit the activity and modify its products or SKUs as
    usual. We recommend using this API instead of recreating the activity to reduce requests to the API
    for adding products.

    Args:
        activity_id (str):
        body (RepublishActivityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RepublishActivityResponse]
     """


    kwargs = _get_kwargs(
        activity_id=activity_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RepublishActivityRequest | Unset = UNSET,

) -> RepublishActivityResponse | None:
    """ Republish Activity

     Use this API to republish a product discount activity or a flash deal activity that expired or was
    deactivated within the last 7 days. This API only supports FIXED_PRICE, FLASHSALE, and
    DIRECT_DISCOUNT activities. You must provide a new effective period by passing the new begin_time
    and end_time. Products and SKUs already associated with the activity do not need to be added again.
    After the activity is republished, you can edit the activity and modify its products or SKUs as
    usual. We recommend using this API instead of recreating the activity to reduce requests to the API
    for adding products.

    Args:
        activity_id (str):
        body (RepublishActivityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RepublishActivityResponse
     """


    return sync_detailed(
        activity_id=activity_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RepublishActivityRequest | Unset = UNSET,

) -> Response[RepublishActivityResponse]:
    """ Republish Activity

     Use this API to republish a product discount activity or a flash deal activity that expired or was
    deactivated within the last 7 days. This API only supports FIXED_PRICE, FLASHSALE, and
    DIRECT_DISCOUNT activities. You must provide a new effective period by passing the new begin_time
    and end_time. Products and SKUs already associated with the activity do not need to be added again.
    After the activity is republished, you can edit the activity and modify its products or SKUs as
    usual. We recommend using this API instead of recreating the activity to reduce requests to the API
    for adding products.

    Args:
        activity_id (str):
        body (RepublishActivityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RepublishActivityResponse]
     """


    kwargs = _get_kwargs(
        activity_id=activity_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RepublishActivityRequest | Unset = UNSET,

) -> RepublishActivityResponse | None:
    """ Republish Activity

     Use this API to republish a product discount activity or a flash deal activity that expired or was
    deactivated within the last 7 days. This API only supports FIXED_PRICE, FLASHSALE, and
    DIRECT_DISCOUNT activities. You must provide a new effective period by passing the new begin_time
    and end_time. Products and SKUs already associated with the activity do not need to be added again.
    After the activity is republished, you can edit the activity and modify its products or SKUs as
    usual. We recommend using this API instead of recreating the activity to reduce requests to the API
    for adding products.

    Args:
        activity_id (str):
        body (RepublishActivityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RepublishActivityResponse
     """


    return (await asyncio_detailed(
        activity_id=activity_id,
client=client,
body=body,

    )).parsed
