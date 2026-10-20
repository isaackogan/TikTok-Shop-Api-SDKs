from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_publisher_sharing_links_in_batch_request import GeneratePublisherSharingLinksInBatchRequest
from ...models.generate_publisher_sharing_links_in_batch_response import GeneratePublisherSharingLinksInBatchResponse
from ...types import Response


def _get_kwargs(
    publisher_id: str,
    *,
    body: GeneratePublisherSharingLinksInBatchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202504/affiliate_sharing_links/publisher/{publisher_id}/generate_batch".format(
            publisher_id=quote(str(publisher_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GeneratePublisherSharingLinksInBatchResponse | None:
    if response.status_code == 200:
        response_200 = GeneratePublisherSharingLinksInBatchResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GeneratePublisherSharingLinksInBatchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    publisher_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GeneratePublisherSharingLinksInBatchRequest,
) -> Response[GeneratePublisherSharingLinksInBatchResponse]:
    """Generate Publisher Sharing Links in Batch

     You can use this API to generate material sharing links for a specific publisher. After that, you
    can share the link with the publisher. Right now, the material type must be `PRODUCT`.
    Please ensure that the material is included in the campaign by using [Generate Multi Affiliate
    Partner Campaign Product Links](generate-multi-affiliate-partner-campaign-product-links).

    Args:
        publisher_id (str):
        body (GeneratePublisherSharingLinksInBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeneratePublisherSharingLinksInBatchResponse]
    """

    kwargs = _get_kwargs(
        publisher_id=publisher_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    publisher_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GeneratePublisherSharingLinksInBatchRequest,
) -> GeneratePublisherSharingLinksInBatchResponse | None:
    """Generate Publisher Sharing Links in Batch

     You can use this API to generate material sharing links for a specific publisher. After that, you
    can share the link with the publisher. Right now, the material type must be `PRODUCT`.
    Please ensure that the material is included in the campaign by using [Generate Multi Affiliate
    Partner Campaign Product Links](generate-multi-affiliate-partner-campaign-product-links).

    Args:
        publisher_id (str):
        body (GeneratePublisherSharingLinksInBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeneratePublisherSharingLinksInBatchResponse
    """

    return sync_detailed(
        publisher_id=publisher_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    publisher_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GeneratePublisherSharingLinksInBatchRequest,
) -> Response[GeneratePublisherSharingLinksInBatchResponse]:
    """Generate Publisher Sharing Links in Batch

     You can use this API to generate material sharing links for a specific publisher. After that, you
    can share the link with the publisher. Right now, the material type must be `PRODUCT`.
    Please ensure that the material is included in the campaign by using [Generate Multi Affiliate
    Partner Campaign Product Links](generate-multi-affiliate-partner-campaign-product-links).

    Args:
        publisher_id (str):
        body (GeneratePublisherSharingLinksInBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeneratePublisherSharingLinksInBatchResponse]
    """

    kwargs = _get_kwargs(
        publisher_id=publisher_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    publisher_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GeneratePublisherSharingLinksInBatchRequest,
) -> GeneratePublisherSharingLinksInBatchResponse | None:
    """Generate Publisher Sharing Links in Batch

     You can use this API to generate material sharing links for a specific publisher. After that, you
    can share the link with the publisher. Right now, the material type must be `PRODUCT`.
    Please ensure that the material is included in the campaign by using [Generate Multi Affiliate
    Partner Campaign Product Links](generate-multi-affiliate-partner-campaign-product-links).

    Args:
        publisher_id (str):
        body (GeneratePublisherSharingLinksInBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeneratePublisherSharingLinksInBatchResponse
    """

    return (
        await asyncio_detailed(
            publisher_id=publisher_id,
            client=client,
            body=body,
        )
    ).parsed
