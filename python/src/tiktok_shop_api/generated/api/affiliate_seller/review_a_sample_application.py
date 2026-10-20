from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.review_a_sample_application_request import ReviewASampleApplicationRequest
from ...models.review_a_sample_application_response import ReviewASampleApplicationResponse
from ...types import Response


def _get_kwargs(
    application_id: str,
    *,
    body: ReviewASampleApplicationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202507/sample_applications/{application_id}/review".format(
            application_id=quote(str(application_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ReviewASampleApplicationResponse | None:
    if response.status_code == 200:
        response_200 = ReviewASampleApplicationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ReviewASampleApplicationResponse]:
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
    body: ReviewASampleApplicationRequest,
) -> Response[ReviewASampleApplicationResponse]:
    """Review a Sample Application

     This API allows the seller to approve or reject a creator's sample application in an open
    collaboration. Only applications in the PENDING status can be approved or rejected. When rejecting
    an application, the seller must provide a supported rejection reason.

    Args:
        application_id (str):
        body (ReviewASampleApplicationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReviewASampleApplicationResponse]
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
    body: ReviewASampleApplicationRequest,
) -> ReviewASampleApplicationResponse | None:
    """Review a Sample Application

     This API allows the seller to approve or reject a creator's sample application in an open
    collaboration. Only applications in the PENDING status can be approved or rejected. When rejecting
    an application, the seller must provide a supported rejection reason.

    Args:
        application_id (str):
        body (ReviewASampleApplicationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReviewASampleApplicationResponse
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
    body: ReviewASampleApplicationRequest,
) -> Response[ReviewASampleApplicationResponse]:
    """Review a Sample Application

     This API allows the seller to approve or reject a creator's sample application in an open
    collaboration. Only applications in the PENDING status can be approved or rejected. When rejecting
    an application, the seller must provide a supported rejection reason.

    Args:
        application_id (str):
        body (ReviewASampleApplicationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReviewASampleApplicationResponse]
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
    body: ReviewASampleApplicationRequest,
) -> ReviewASampleApplicationResponse | None:
    """Review a Sample Application

     This API allows the seller to approve or reject a creator's sample application in an open
    collaboration. Only applications in the PENDING status can be approved or rejected. When rejecting
    an application, the seller must provide a supported rejection reason.

    Args:
        application_id (str):
        body (ReviewASampleApplicationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReviewASampleApplicationResponse
    """

    return (
        await asyncio_detailed(
            application_id=application_id,
            client=client,
            body=body,
        )
    ).parsed
