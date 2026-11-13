from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_registered_campaign_counts_response import GetRegisteredCampaignCountsResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/promotion/202611/registered_campaigns/counts",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetRegisteredCampaignCountsResponse | None:
    if response.status_code == 200:
        response_200 = GetRegisteredCampaignCountsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetRegisteredCampaignCountsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetRegisteredCampaignCountsResponse]:
    """ Get Registered Campaign Counts

     Get the shop's registered campaign counts: all_count, upcoming_count, active_count, and ended_count.
    ACTIVE covers the entire process from registration opening to campaign completion, not just
    execution. This operation has no list filters, so the result is not total_count for a particular
    filtered list. It uses the standard statistics scope, including manual and other registration
    methods. Queries specific to legacy automatic enrollment management are not supported. Categories
    are independent and are not guaranteed to sum to all_count. Successful data may be empty when all
    counts are unavailable.

    Requires SHOP authorization and shop_cipher. The shop, its seller, and its region are determined
    from the verified authorization context and cannot be supplied or overridden by the caller. Cross-
    shop access in the EU is limited to eligible shops belonging to the same seller and does not allow
    access to another seller's data.

    This is a query operation. It does not register for or withdraw from campaigns, sign agreements, or
    change campaign settings. Visibility, invitations, existing registrations, campaign status, and
    registration stage do not independently establish whether registration is currently allowed. An
    omitted eligibility result means unknown; it must not be interpreted as false, zero, free
    participation, an unlimited quota, or permission to register. Explicit false, zero, and empty arrays
    retain their meanings. Text is for display; automated decisions should use structured statuses and
    recognized reason codes.

    Invalid parameters, unknown request enum values, authorization failures, rate limits, and dependency
    failures use the platform's standard error mechanism. A known failure is not returned as a
    successful empty result. Campaign business processes determine status changes; this query does not
    change status or guarantee that every intermediate status occurs. Response enums may gain values in
    the future. Clients should preserve unknown values and handle them conservatively.

    Timestamps use RFC 3339 UTC with three fractional-second digits. See each field's description for
    interval boundaries and omission semantics. Statistics may be delayed or incomplete; no
    transactional snapshot is guaranteed across fields or pages. Query again before making a subsequent
    business decision.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRegisteredCampaignCountsResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> GetRegisteredCampaignCountsResponse | None:
    """ Get Registered Campaign Counts

     Get the shop's registered campaign counts: all_count, upcoming_count, active_count, and ended_count.
    ACTIVE covers the entire process from registration opening to campaign completion, not just
    execution. This operation has no list filters, so the result is not total_count for a particular
    filtered list. It uses the standard statistics scope, including manual and other registration
    methods. Queries specific to legacy automatic enrollment management are not supported. Categories
    are independent and are not guaranteed to sum to all_count. Successful data may be empty when all
    counts are unavailable.

    Requires SHOP authorization and shop_cipher. The shop, its seller, and its region are determined
    from the verified authorization context and cannot be supplied or overridden by the caller. Cross-
    shop access in the EU is limited to eligible shops belonging to the same seller and does not allow
    access to another seller's data.

    This is a query operation. It does not register for or withdraw from campaigns, sign agreements, or
    change campaign settings. Visibility, invitations, existing registrations, campaign status, and
    registration stage do not independently establish whether registration is currently allowed. An
    omitted eligibility result means unknown; it must not be interpreted as false, zero, free
    participation, an unlimited quota, or permission to register. Explicit false, zero, and empty arrays
    retain their meanings. Text is for display; automated decisions should use structured statuses and
    recognized reason codes.

    Invalid parameters, unknown request enum values, authorization failures, rate limits, and dependency
    failures use the platform's standard error mechanism. A known failure is not returned as a
    successful empty result. Campaign business processes determine status changes; this query does not
    change status or guarantee that every intermediate status occurs. Response enums may gain values in
    the future. Clients should preserve unknown values and handle them conservatively.

    Timestamps use RFC 3339 UTC with three fractional-second digits. See each field's description for
    interval boundaries and omission semantics. Statistics may be delayed or incomplete; no
    transactional snapshot is guaranteed across fields or pages. Query again before making a subsequent
    business decision.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRegisteredCampaignCountsResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetRegisteredCampaignCountsResponse]:
    """ Get Registered Campaign Counts

     Get the shop's registered campaign counts: all_count, upcoming_count, active_count, and ended_count.
    ACTIVE covers the entire process from registration opening to campaign completion, not just
    execution. This operation has no list filters, so the result is not total_count for a particular
    filtered list. It uses the standard statistics scope, including manual and other registration
    methods. Queries specific to legacy automatic enrollment management are not supported. Categories
    are independent and are not guaranteed to sum to all_count. Successful data may be empty when all
    counts are unavailable.

    Requires SHOP authorization and shop_cipher. The shop, its seller, and its region are determined
    from the verified authorization context and cannot be supplied or overridden by the caller. Cross-
    shop access in the EU is limited to eligible shops belonging to the same seller and does not allow
    access to another seller's data.

    This is a query operation. It does not register for or withdraw from campaigns, sign agreements, or
    change campaign settings. Visibility, invitations, existing registrations, campaign status, and
    registration stage do not independently establish whether registration is currently allowed. An
    omitted eligibility result means unknown; it must not be interpreted as false, zero, free
    participation, an unlimited quota, or permission to register. Explicit false, zero, and empty arrays
    retain their meanings. Text is for display; automated decisions should use structured statuses and
    recognized reason codes.

    Invalid parameters, unknown request enum values, authorization failures, rate limits, and dependency
    failures use the platform's standard error mechanism. A known failure is not returned as a
    successful empty result. Campaign business processes determine status changes; this query does not
    change status or guarantee that every intermediate status occurs. Response enums may gain values in
    the future. Clients should preserve unknown values and handle them conservatively.

    Timestamps use RFC 3339 UTC with three fractional-second digits. See each field's description for
    interval boundaries and omission semantics. Statistics may be delayed or incomplete; no
    transactional snapshot is guaranteed across fields or pages. Query again before making a subsequent
    business decision.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRegisteredCampaignCountsResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> GetRegisteredCampaignCountsResponse | None:
    """ Get Registered Campaign Counts

     Get the shop's registered campaign counts: all_count, upcoming_count, active_count, and ended_count.
    ACTIVE covers the entire process from registration opening to campaign completion, not just
    execution. This operation has no list filters, so the result is not total_count for a particular
    filtered list. It uses the standard statistics scope, including manual and other registration
    methods. Queries specific to legacy automatic enrollment management are not supported. Categories
    are independent and are not guaranteed to sum to all_count. Successful data may be empty when all
    counts are unavailable.

    Requires SHOP authorization and shop_cipher. The shop, its seller, and its region are determined
    from the verified authorization context and cannot be supplied or overridden by the caller. Cross-
    shop access in the EU is limited to eligible shops belonging to the same seller and does not allow
    access to another seller's data.

    This is a query operation. It does not register for or withdraw from campaigns, sign agreements, or
    change campaign settings. Visibility, invitations, existing registrations, campaign status, and
    registration stage do not independently establish whether registration is currently allowed. An
    omitted eligibility result means unknown; it must not be interpreted as false, zero, free
    participation, an unlimited quota, or permission to register. Explicit false, zero, and empty arrays
    retain their meanings. Text is for display; automated decisions should use structured statuses and
    recognized reason codes.

    Invalid parameters, unknown request enum values, authorization failures, rate limits, and dependency
    failures use the platform's standard error mechanism. A known failure is not returned as a
    successful empty result. Campaign business processes determine status changes; this query does not
    change status or guarantee that every intermediate status occurs. Response enums may gain values in
    the future. Clients should preserve unknown values and handle them conservatively.

    Timestamps use RFC 3339 UTC with three fractional-second digits. See each field's description for
    interval boundaries and omission semantics. Statistics may be delayed or incomplete; no
    transactional snapshot is guaranteed across fields or pages. Query again before making a subsequent
    business decision.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRegisteredCampaignCountsResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
