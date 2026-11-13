from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_registered_campaign_response import ListRegisteredCampaignResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    campaign_name: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    campaign_statuses: list[str] | Unset = UNSET,
    campaign_regions: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size

    params["campaign_name"] = campaign_name

    json_types: list[str] | Unset = UNSET
    if not isinstance(types, Unset):
        json_types = types


    params["types"] = json_types

    json_campaign_statuses: list[str] | Unset = UNSET
    if not isinstance(campaign_statuses, Unset):
        json_campaign_statuses = campaign_statuses


    params["campaign_statuses"] = json_campaign_statuses

    json_campaign_regions: list[str] | Unset = UNSET
    if not isinstance(campaign_regions, Unset):
        json_campaign_regions = campaign_regions


    params["campaign_regions"] = json_campaign_regions

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/promotion/202611/registered_campaigns",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListRegisteredCampaignResponse | None:
    if response.status_code == 200:
        response_200 = ListRegisteredCampaignResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListRegisteredCampaignResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    campaign_name: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    campaign_statuses: list[str] | Unset = UNSET,
    campaign_regions: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[ListRegisteredCampaignResponse]:
    """ List Registered Campaign

     List the shop's registered campaign summaries, with registration statistics and product negotiation
    statistics where applicable to the campaign type. A registration relationship does not guarantee
    approval or effective benefits. This release does not expose filters for registration source,
    automatic enrollment-specific scenarios, or subtypes.

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

    Use each campaign ID together with type: PRODUCT uses GetProductCampaign, SHOP uses GetShopCampaign,
    LIVESTREAM uses GetLivestreamCampaign, and SHORT_VIDEO uses GetShortVideoCampaign. Do not infer a
    detail endpoint for an unknown type.

    locale uses BCP-47 and defaults to en-US; en-GB uses English text. Text falls back according to the
    campaign's localization rules and may contain rich text; HTML sanitization is not guaranteed.
    Unavailable text is omitted rather than replaced with a placeholder name.

    The default order places ACTIVE campaigns first, then orders campaigns within each status-priority
    group by registration end time descending. Equal registration end times retain source order; stable
    ID ordering is not guaranteed. The same ordering applies to single-shop queries and the combined EU
    shop scope before pagination. ACTIVE uses the campaign lifecycle definition, not only the event
    execution period. Unknown types or statuses are not additionally removed by this API. Different
    filters are combined with AND; values within each filter array use OR. Custom sorting is not
    supported. Results contain registered campaigns within the current query scope and may not cover all
    historical registrations. A page may contain more items than page_size.

    For the first page, omit page_token or pass an empty string. For subsequent pages, pass
    next_page_token unchanged and keep the authorized shop, filters, and page_size unchanged. An empty
    next_page_token means there are no further pages within the current query scope; it does not
    guarantee that all historical campaigns or campaigns accessible across shops have been retrieved. An
    empty page is not necessarily the last page. Do not stop pagination based on the number of returned
    items.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        campaign_name (str | Unset):
        types (list[str] | Unset):
        campaign_statuses (list[str] | Unset):
        campaign_regions (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListRegisteredCampaignResponse]
     """


    kwargs = _get_kwargs(
        page_token=page_token,
page_size=page_size,
campaign_name=campaign_name,
types=types,
campaign_statuses=campaign_statuses,
campaign_regions=campaign_regions,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    campaign_name: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    campaign_statuses: list[str] | Unset = UNSET,
    campaign_regions: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> ListRegisteredCampaignResponse | None:
    """ List Registered Campaign

     List the shop's registered campaign summaries, with registration statistics and product negotiation
    statistics where applicable to the campaign type. A registration relationship does not guarantee
    approval or effective benefits. This release does not expose filters for registration source,
    automatic enrollment-specific scenarios, or subtypes.

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

    Use each campaign ID together with type: PRODUCT uses GetProductCampaign, SHOP uses GetShopCampaign,
    LIVESTREAM uses GetLivestreamCampaign, and SHORT_VIDEO uses GetShortVideoCampaign. Do not infer a
    detail endpoint for an unknown type.

    locale uses BCP-47 and defaults to en-US; en-GB uses English text. Text falls back according to the
    campaign's localization rules and may contain rich text; HTML sanitization is not guaranteed.
    Unavailable text is omitted rather than replaced with a placeholder name.

    The default order places ACTIVE campaigns first, then orders campaigns within each status-priority
    group by registration end time descending. Equal registration end times retain source order; stable
    ID ordering is not guaranteed. The same ordering applies to single-shop queries and the combined EU
    shop scope before pagination. ACTIVE uses the campaign lifecycle definition, not only the event
    execution period. Unknown types or statuses are not additionally removed by this API. Different
    filters are combined with AND; values within each filter array use OR. Custom sorting is not
    supported. Results contain registered campaigns within the current query scope and may not cover all
    historical registrations. A page may contain more items than page_size.

    For the first page, omit page_token or pass an empty string. For subsequent pages, pass
    next_page_token unchanged and keep the authorized shop, filters, and page_size unchanged. An empty
    next_page_token means there are no further pages within the current query scope; it does not
    guarantee that all historical campaigns or campaigns accessible across shops have been retrieved. An
    empty page is not necessarily the last page. Do not stop pagination based on the number of returned
    items.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        campaign_name (str | Unset):
        types (list[str] | Unset):
        campaign_statuses (list[str] | Unset):
        campaign_regions (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListRegisteredCampaignResponse
     """


    return sync_detailed(
        client=client,
page_token=page_token,
page_size=page_size,
campaign_name=campaign_name,
types=types,
campaign_statuses=campaign_statuses,
campaign_regions=campaign_regions,
locale=locale,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    campaign_name: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    campaign_statuses: list[str] | Unset = UNSET,
    campaign_regions: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[ListRegisteredCampaignResponse]:
    """ List Registered Campaign

     List the shop's registered campaign summaries, with registration statistics and product negotiation
    statistics where applicable to the campaign type. A registration relationship does not guarantee
    approval or effective benefits. This release does not expose filters for registration source,
    automatic enrollment-specific scenarios, or subtypes.

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

    Use each campaign ID together with type: PRODUCT uses GetProductCampaign, SHOP uses GetShopCampaign,
    LIVESTREAM uses GetLivestreamCampaign, and SHORT_VIDEO uses GetShortVideoCampaign. Do not infer a
    detail endpoint for an unknown type.

    locale uses BCP-47 and defaults to en-US; en-GB uses English text. Text falls back according to the
    campaign's localization rules and may contain rich text; HTML sanitization is not guaranteed.
    Unavailable text is omitted rather than replaced with a placeholder name.

    The default order places ACTIVE campaigns first, then orders campaigns within each status-priority
    group by registration end time descending. Equal registration end times retain source order; stable
    ID ordering is not guaranteed. The same ordering applies to single-shop queries and the combined EU
    shop scope before pagination. ACTIVE uses the campaign lifecycle definition, not only the event
    execution period. Unknown types or statuses are not additionally removed by this API. Different
    filters are combined with AND; values within each filter array use OR. Custom sorting is not
    supported. Results contain registered campaigns within the current query scope and may not cover all
    historical registrations. A page may contain more items than page_size.

    For the first page, omit page_token or pass an empty string. For subsequent pages, pass
    next_page_token unchanged and keep the authorized shop, filters, and page_size unchanged. An empty
    next_page_token means there are no further pages within the current query scope; it does not
    guarantee that all historical campaigns or campaigns accessible across shops have been retrieved. An
    empty page is not necessarily the last page. Do not stop pagination based on the number of returned
    items.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        campaign_name (str | Unset):
        types (list[str] | Unset):
        campaign_statuses (list[str] | Unset):
        campaign_regions (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListRegisteredCampaignResponse]
     """


    kwargs = _get_kwargs(
        page_token=page_token,
page_size=page_size,
campaign_name=campaign_name,
types=types,
campaign_statuses=campaign_statuses,
campaign_regions=campaign_regions,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    campaign_name: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    campaign_statuses: list[str] | Unset = UNSET,
    campaign_regions: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> ListRegisteredCampaignResponse | None:
    """ List Registered Campaign

     List the shop's registered campaign summaries, with registration statistics and product negotiation
    statistics where applicable to the campaign type. A registration relationship does not guarantee
    approval or effective benefits. This release does not expose filters for registration source,
    automatic enrollment-specific scenarios, or subtypes.

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

    Use each campaign ID together with type: PRODUCT uses GetProductCampaign, SHOP uses GetShopCampaign,
    LIVESTREAM uses GetLivestreamCampaign, and SHORT_VIDEO uses GetShortVideoCampaign. Do not infer a
    detail endpoint for an unknown type.

    locale uses BCP-47 and defaults to en-US; en-GB uses English text. Text falls back according to the
    campaign's localization rules and may contain rich text; HTML sanitization is not guaranteed.
    Unavailable text is omitted rather than replaced with a placeholder name.

    The default order places ACTIVE campaigns first, then orders campaigns within each status-priority
    group by registration end time descending. Equal registration end times retain source order; stable
    ID ordering is not guaranteed. The same ordering applies to single-shop queries and the combined EU
    shop scope before pagination. ACTIVE uses the campaign lifecycle definition, not only the event
    execution period. Unknown types or statuses are not additionally removed by this API. Different
    filters are combined with AND; values within each filter array use OR. Custom sorting is not
    supported. Results contain registered campaigns within the current query scope and may not cover all
    historical registrations. A page may contain more items than page_size.

    For the first page, omit page_token or pass an empty string. For subsequent pages, pass
    next_page_token unchanged and keep the authorized shop, filters, and page_size unchanged. An empty
    next_page_token means there are no further pages within the current query scope; it does not
    guarantee that all historical campaigns or campaigns accessible across shops have been retrieved. An
    empty page is not necessarily the last page. Do not stop pagination based on the number of returned
    items.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        campaign_name (str | Unset):
        types (list[str] | Unset):
        campaign_statuses (list[str] | Unset):
        campaign_regions (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListRegisteredCampaignResponse
     """


    return (await asyncio_detailed(
        client=client,
page_token=page_token,
page_size=page_size,
campaign_name=campaign_name,
types=types,
campaign_statuses=campaign_statuses,
campaign_regions=campaign_regions,
locale=locale,

    )).parsed
