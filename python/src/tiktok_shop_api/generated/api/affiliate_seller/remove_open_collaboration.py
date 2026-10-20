from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_open_collaboration_request import RemoveOpenCollaborationRequest
from ...models.remove_open_collaboration_response import RemoveOpenCollaborationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: str,
    *,
    body: RemoveOpenCollaborationRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/affiliate_seller/202409/open_collaborations/products/{product_id}".format(
            product_id=quote(str(product_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RemoveOpenCollaborationResponse | None:
    if response.status_code == 200:
        response_200 = RemoveOpenCollaborationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RemoveOpenCollaborationResponse]:
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
    body: RemoveOpenCollaborationRequest | Unset = UNSET,
) -> Response[RemoveOpenCollaborationResponse]:
    """Remove Open Collaboration

     Remove a product's open collaboration. You can remove only an open collaboration with `status ==
    NORMAL`. Use the published `POST /affiliate_seller/202409/open_collaborations/search` endpoint to
    find the product's open collaboration and confirm that its status is `NORMAL` before calling this
    API. To protect creators' interests, termination is not immediate and takes effect at the returned
    `terminated_effective_time`. After that time, call the same search endpoint to verify that the open
    collaboration is no longer returned.

    Args:
        product_id (str):
        body (RemoveOpenCollaborationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveOpenCollaborationResponse]
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
    body: RemoveOpenCollaborationRequest | Unset = UNSET,
) -> RemoveOpenCollaborationResponse | None:
    """Remove Open Collaboration

     Remove a product's open collaboration. You can remove only an open collaboration with `status ==
    NORMAL`. Use the published `POST /affiliate_seller/202409/open_collaborations/search` endpoint to
    find the product's open collaboration and confirm that its status is `NORMAL` before calling this
    API. To protect creators' interests, termination is not immediate and takes effect at the returned
    `terminated_effective_time`. After that time, call the same search endpoint to verify that the open
    collaboration is no longer returned.

    Args:
        product_id (str):
        body (RemoveOpenCollaborationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveOpenCollaborationResponse
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
    body: RemoveOpenCollaborationRequest | Unset = UNSET,
) -> Response[RemoveOpenCollaborationResponse]:
    """Remove Open Collaboration

     Remove a product's open collaboration. You can remove only an open collaboration with `status ==
    NORMAL`. Use the published `POST /affiliate_seller/202409/open_collaborations/search` endpoint to
    find the product's open collaboration and confirm that its status is `NORMAL` before calling this
    API. To protect creators' interests, termination is not immediate and takes effect at the returned
    `terminated_effective_time`. After that time, call the same search endpoint to verify that the open
    collaboration is no longer returned.

    Args:
        product_id (str):
        body (RemoveOpenCollaborationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveOpenCollaborationResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveOpenCollaborationRequest | Unset = UNSET,
) -> RemoveOpenCollaborationResponse | None:
    """Remove Open Collaboration

     Remove a product's open collaboration. You can remove only an open collaboration with `status ==
    NORMAL`. Use the published `POST /affiliate_seller/202409/open_collaborations/search` endpoint to
    find the product's open collaboration and confirm that its status is `NORMAL` before calling this
    API. To protect creators' interests, termination is not immediate and takes effect at the returned
    `terminated_effective_time`. After that time, call the same search endpoint to verify that the open
    collaboration is no longer returned.

    Args:
        product_id (str):
        body (RemoveOpenCollaborationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveOpenCollaborationResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            body=body,
        )
    ).parsed
