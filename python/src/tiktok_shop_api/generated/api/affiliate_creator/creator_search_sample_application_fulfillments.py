from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.creator_search_sample_application_fulfillments_request import (
    CreatorSearchSampleApplicationFulfillmentsRequest,
)
from ...models.creator_search_sample_application_fulfillments_response import (
    CreatorSearchSampleApplicationFulfillmentsResponse,
)
from ...models.creator_search_sample_application_fulfillments_sort_field import (
    CreatorSearchSampleApplicationFulfillmentsSortField,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreatorSearchSampleApplicationFulfillmentsRequest,
    sort_order: str | Unset = UNSET,
    sort_field: CreatorSearchSampleApplicationFulfillmentsSortField | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["sort_order"] = sort_order

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sort_field"] = json_sort_field

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202409/sample_applications/fulfillments/search",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreatorSearchSampleApplicationFulfillmentsResponse | None:
    if response.status_code == 200:
        response_200 = CreatorSearchSampleApplicationFulfillmentsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreatorSearchSampleApplicationFulfillmentsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatorSearchSampleApplicationFulfillmentsRequest,
    sort_order: str | Unset = UNSET,
    sort_field: CreatorSearchSampleApplicationFulfillmentsSortField | Unset = UNSET,
) -> Response[CreatorSearchSampleApplicationFulfillmentsResponse]:
    """Creator Search Sample Application Fulfillments

     You, the creator, can use this API to query the fulfillment status for the received sample
    applications.

    Args:
        sort_order (str | Unset):
        sort_field (CreatorSearchSampleApplicationFulfillmentsSortField | Unset):
        body (CreatorSearchSampleApplicationFulfillmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatorSearchSampleApplicationFulfillmentsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        sort_order=sort_order,
        sort_field=sort_field,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreatorSearchSampleApplicationFulfillmentsRequest,
    sort_order: str | Unset = UNSET,
    sort_field: CreatorSearchSampleApplicationFulfillmentsSortField | Unset = UNSET,
) -> CreatorSearchSampleApplicationFulfillmentsResponse | None:
    """Creator Search Sample Application Fulfillments

     You, the creator, can use this API to query the fulfillment status for the received sample
    applications.

    Args:
        sort_order (str | Unset):
        sort_field (CreatorSearchSampleApplicationFulfillmentsSortField | Unset):
        body (CreatorSearchSampleApplicationFulfillmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatorSearchSampleApplicationFulfillmentsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        sort_order=sort_order,
        sort_field=sort_field,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatorSearchSampleApplicationFulfillmentsRequest,
    sort_order: str | Unset = UNSET,
    sort_field: CreatorSearchSampleApplicationFulfillmentsSortField | Unset = UNSET,
) -> Response[CreatorSearchSampleApplicationFulfillmentsResponse]:
    """Creator Search Sample Application Fulfillments

     You, the creator, can use this API to query the fulfillment status for the received sample
    applications.

    Args:
        sort_order (str | Unset):
        sort_field (CreatorSearchSampleApplicationFulfillmentsSortField | Unset):
        body (CreatorSearchSampleApplicationFulfillmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatorSearchSampleApplicationFulfillmentsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        sort_order=sort_order,
        sort_field=sort_field,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreatorSearchSampleApplicationFulfillmentsRequest,
    sort_order: str | Unset = UNSET,
    sort_field: CreatorSearchSampleApplicationFulfillmentsSortField | Unset = UNSET,
) -> CreatorSearchSampleApplicationFulfillmentsResponse | None:
    """Creator Search Sample Application Fulfillments

     You, the creator, can use this API to query the fulfillment status for the received sample
    applications.

    Args:
        sort_order (str | Unset):
        sort_field (CreatorSearchSampleApplicationFulfillmentsSortField | Unset):
        body (CreatorSearchSampleApplicationFulfillmentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatorSearchSampleApplicationFulfillmentsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            sort_order=sort_order,
            sort_field=sort_field,
        )
    ).parsed
