from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.submit_size_chart_appeal_request import SubmitSizeChartAppealRequest
from ...models.submit_size_chart_appeal_response import SubmitSizeChartAppealResponse
from typing import cast



def _get_kwargs(
    *,
    body: SubmitSizeChartAppealRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202604/appeals/submit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SubmitSizeChartAppealResponse | None:
    if response.status_code == 200:
        response_200 = SubmitSizeChartAppealResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SubmitSizeChartAppealResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubmitSizeChartAppealRequest,

) -> Response[SubmitSizeChartAppealResponse]:
    """ Submit Size Chart Appeal

     #### Appeal Size Chart Verification
    Initiates an appeal process for a product that was blocked during the listing phase due to a size
    chart verification failure.
    This API is used when a seller believes their product was incorrectly blocked by our automated size
    chart validation system. The validation checks for three potential issues:
    1. Whether the size chart contains all mandatory dimensions.
    2. Whether the size chart covers all Stock-Keeping Units (SKUs) for sale.
    3. Whether the numerical values within the size chart are valid.
    If the validation system detects an issue, the product listing will be blocked. By using this API,
    sellers can submit an appeal. If the appeal is approved, the block will be lifted, and the seller
    can re-list the product.
    Use the `[Appeal Status Webhook]` to monitor the appeal's progress, or pass the `appeal_id` to the
    `[Get Appeal Status API]` to retrieve the current status.
    Note:
    - Please wait at least 5 minutes after submitting an appeal before checking its status via the API
    to ensure the data is synchronized.
    - You can submit up to 50 appeals per day. Any requests exceeding this limit will be rejected.

    Args:
        body (SubmitSizeChartAppealRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitSizeChartAppealResponse]
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
    body: SubmitSizeChartAppealRequest,

) -> SubmitSizeChartAppealResponse | None:
    """ Submit Size Chart Appeal

     #### Appeal Size Chart Verification
    Initiates an appeal process for a product that was blocked during the listing phase due to a size
    chart verification failure.
    This API is used when a seller believes their product was incorrectly blocked by our automated size
    chart validation system. The validation checks for three potential issues:
    1. Whether the size chart contains all mandatory dimensions.
    2. Whether the size chart covers all Stock-Keeping Units (SKUs) for sale.
    3. Whether the numerical values within the size chart are valid.
    If the validation system detects an issue, the product listing will be blocked. By using this API,
    sellers can submit an appeal. If the appeal is approved, the block will be lifted, and the seller
    can re-list the product.
    Use the `[Appeal Status Webhook]` to monitor the appeal's progress, or pass the `appeal_id` to the
    `[Get Appeal Status API]` to retrieve the current status.
    Note:
    - Please wait at least 5 minutes after submitting an appeal before checking its status via the API
    to ensure the data is synchronized.
    - You can submit up to 50 appeals per day. Any requests exceeding this limit will be rejected.

    Args:
        body (SubmitSizeChartAppealRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitSizeChartAppealResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubmitSizeChartAppealRequest,

) -> Response[SubmitSizeChartAppealResponse]:
    """ Submit Size Chart Appeal

     #### Appeal Size Chart Verification
    Initiates an appeal process for a product that was blocked during the listing phase due to a size
    chart verification failure.
    This API is used when a seller believes their product was incorrectly blocked by our automated size
    chart validation system. The validation checks for three potential issues:
    1. Whether the size chart contains all mandatory dimensions.
    2. Whether the size chart covers all Stock-Keeping Units (SKUs) for sale.
    3. Whether the numerical values within the size chart are valid.
    If the validation system detects an issue, the product listing will be blocked. By using this API,
    sellers can submit an appeal. If the appeal is approved, the block will be lifted, and the seller
    can re-list the product.
    Use the `[Appeal Status Webhook]` to monitor the appeal's progress, or pass the `appeal_id` to the
    `[Get Appeal Status API]` to retrieve the current status.
    Note:
    - Please wait at least 5 minutes after submitting an appeal before checking its status via the API
    to ensure the data is synchronized.
    - You can submit up to 50 appeals per day. Any requests exceeding this limit will be rejected.

    Args:
        body (SubmitSizeChartAppealRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitSizeChartAppealResponse]
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
    body: SubmitSizeChartAppealRequest,

) -> SubmitSizeChartAppealResponse | None:
    """ Submit Size Chart Appeal

     #### Appeal Size Chart Verification
    Initiates an appeal process for a product that was blocked during the listing phase due to a size
    chart verification failure.
    This API is used when a seller believes their product was incorrectly blocked by our automated size
    chart validation system. The validation checks for three potential issues:
    1. Whether the size chart contains all mandatory dimensions.
    2. Whether the size chart covers all Stock-Keeping Units (SKUs) for sale.
    3. Whether the numerical values within the size chart are valid.
    If the validation system detects an issue, the product listing will be blocked. By using this API,
    sellers can submit an appeal. If the appeal is approved, the block will be lifted, and the seller
    can re-list the product.
    Use the `[Appeal Status Webhook]` to monitor the appeal's progress, or pass the `appeal_id` to the
    `[Get Appeal Status API]` to retrieve the current status.
    Note:
    - Please wait at least 5 minutes after submitting an appeal before checking its status via the API
    to ensure the data is synchronized.
    - You can submit up to 50 appeals per day. Any requests exceeding this limit will be rejected.

    Args:
        body (SubmitSizeChartAppealRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitSizeChartAppealResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
