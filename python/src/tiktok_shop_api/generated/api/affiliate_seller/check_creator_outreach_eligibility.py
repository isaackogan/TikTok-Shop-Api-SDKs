from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_creator_outreach_eligibility_request import CheckCreatorOutreachEligibilityRequest
from ...models.check_creator_outreach_eligibility_response import CheckCreatorOutreachEligibilityResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CheckCreatorOutreachEligibilityRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202610/creator_outreach/eligibility/check",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CheckCreatorOutreachEligibilityResponse | None:
    if response.status_code == 200:
        response_200 = CheckCreatorOutreachEligibilityResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CheckCreatorOutreachEligibilityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckCreatorOutreachEligibilityRequest,
) -> Response[CheckCreatorOutreachEligibilityResponse]:
    """Check Creator Outreach Eligibility

     Check whether creators meet the shop's connection and quota requirements before initiating creator
    outreach.

    Args:
        body (CheckCreatorOutreachEligibilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckCreatorOutreachEligibilityResponse]
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
    body: CheckCreatorOutreachEligibilityRequest,
) -> CheckCreatorOutreachEligibilityResponse | None:
    """Check Creator Outreach Eligibility

     Check whether creators meet the shop's connection and quota requirements before initiating creator
    outreach.

    Args:
        body (CheckCreatorOutreachEligibilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckCreatorOutreachEligibilityResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckCreatorOutreachEligibilityRequest,
) -> Response[CheckCreatorOutreachEligibilityResponse]:
    """Check Creator Outreach Eligibility

     Check whether creators meet the shop's connection and quota requirements before initiating creator
    outreach.

    Args:
        body (CheckCreatorOutreachEligibilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckCreatorOutreachEligibilityResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CheckCreatorOutreachEligibilityRequest,
) -> CheckCreatorOutreachEligibilityResponse | None:
    """Check Creator Outreach Eligibility

     Check whether creators meet the shop's connection and quota requirements before initiating creator
    outreach.

    Args:
        body (CheckCreatorOutreachEligibilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckCreatorOutreachEligibilityResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
