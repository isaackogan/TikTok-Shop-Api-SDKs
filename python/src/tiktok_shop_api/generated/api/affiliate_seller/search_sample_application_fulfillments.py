from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_sample_application_fulfillments_request import SearchSampleApplicationFulfillmentsRequest
from ...models.search_sample_application_fulfillments_response import SearchSampleApplicationFulfillmentsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    application_id: str,
    *,
    body: SearchSampleApplicationFulfillmentsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202409/sample_applications/{application_id}/fulfillments/search".format(
            application_id=quote(str(application_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SearchSampleApplicationFulfillmentsResponse | None:
    if response.status_code == 200:
        response_200 = SearchSampleApplicationFulfillmentsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchSampleApplicationFulfillmentsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchSampleApplicationFulfillmentsRequest | Unset = UNSET,
) -> Response[SearchSampleApplicationFulfillmentsResponse]:
    """Search Sample Application Fulfillments

     You, the seller, can use this API to get the fulfillment status of the specific sample application
    and whether the fulfillment resulted in orders. This allows Sellers to track the current progress or
    analyze the results of their sample distribution program.

    Args:
        application_id (str):
        body (SearchSampleApplicationFulfillmentsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSampleApplicationFulfillmentsResponse]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    application_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchSampleApplicationFulfillmentsRequest | Unset = UNSET,
) -> SearchSampleApplicationFulfillmentsResponse | None:
    """Search Sample Application Fulfillments

     You, the seller, can use this API to get the fulfillment status of the specific sample application
    and whether the fulfillment resulted in orders. This allows Sellers to track the current progress or
    analyze the results of their sample distribution program.

    Args:
        application_id (str):
        body (SearchSampleApplicationFulfillmentsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSampleApplicationFulfillmentsResponse
    """

    return sync_detailed(
        application_id=application_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    application_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchSampleApplicationFulfillmentsRequest | Unset = UNSET,
) -> Response[SearchSampleApplicationFulfillmentsResponse]:
    """Search Sample Application Fulfillments

     You, the seller, can use this API to get the fulfillment status of the specific sample application
    and whether the fulfillment resulted in orders. This allows Sellers to track the current progress or
    analyze the results of their sample distribution program.

    Args:
        application_id (str):
        body (SearchSampleApplicationFulfillmentsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSampleApplicationFulfillmentsResponse]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchSampleApplicationFulfillmentsRequest | Unset = UNSET,
) -> SearchSampleApplicationFulfillmentsResponse | None:
    """Search Sample Application Fulfillments

     You, the seller, can use this API to get the fulfillment status of the specific sample application
    and whether the fulfillment resulted in orders. This allows Sellers to track the current progress or
    analyze the results of their sample distribution program.

    Args:
        application_id (str):
        body (SearchSampleApplicationFulfillmentsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSampleApplicationFulfillmentsResponse
    """

    return (
        await asyncio_detailed(
            application_id=application_id,
            client=client,
            body=body,
        )
    ).parsed
