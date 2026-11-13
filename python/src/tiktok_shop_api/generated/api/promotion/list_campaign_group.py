from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_campaign_group_response import ListCampaignGroupResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    campaign_name: str | Unset = UNSET,
    is_invited: bool | Unset = UNSET,
    only_pending_registrations: bool | Unset = UNSET,
    list_scope: str | Unset = UNSET,
    registration_regions: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size

    params["campaign_name"] = campaign_name

    params["is_invited"] = is_invited

    params["only_pending_registrations"] = only_pending_registrations

    params["list_scope"] = list_scope

    json_registration_regions: list[str] | Unset = UNSET
    if not isinstance(registration_regions, Unset):
        json_registration_regions = registration_regions


    params["registration_regions"] = json_registration_regions

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/promotion/202611/campaign_groups",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListCampaignGroupResponse | None:
    if response.status_code == 200:
        response_200 = ListCampaignGroupResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListCampaignGroupResponse]:
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
    is_invited: bool | Unset = UNSET,
    only_pending_registrations: bool | Unset = UNSET,
    list_scope: str | Unset = UNSET,
    registration_regions: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[ListCampaignGroupResponse]:
    """ List Campaign Group

     List campaign groups visible to the shop. NORMAL groups return campaigns summaries, while LONG_TERM
    groups return linked_campaign_groups. These two fields are mutually exclusive and are both omitted
    for an unknown type. Campaign summaries within a group are not paginated separately. An empty
    summary list does not guarantee that the group contains no campaigns.

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

    Uses the seller-facing campaign group filters and ordering. In the standard flow, priority is given
    to pinned groups, long-term campaigns, registration availability, featured campaigns, campaign
    level, and start time. The pending-confirmation filter prioritizes the most recent join time. EU
    aggregation prioritizes long-term campaigns, followed by pending-confirmation time, registration
    availability, featured campaigns, campaign level, and start time. Custom sorting is not supported.
    Ties retain source order; stable ID ordering is not guaranteed. This query does not mark campaigns
    as visited or update the visit record used by the seller interface to identify new campaigns.

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
        is_invited (bool | Unset):
        only_pending_registrations (bool | Unset):
        list_scope (str | Unset):
        registration_regions (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCampaignGroupResponse]
     """


    kwargs = _get_kwargs(
        page_token=page_token,
page_size=page_size,
campaign_name=campaign_name,
is_invited=is_invited,
only_pending_registrations=only_pending_registrations,
list_scope=list_scope,
registration_regions=registration_regions,
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
    is_invited: bool | Unset = UNSET,
    only_pending_registrations: bool | Unset = UNSET,
    list_scope: str | Unset = UNSET,
    registration_regions: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> ListCampaignGroupResponse | None:
    """ List Campaign Group

     List campaign groups visible to the shop. NORMAL groups return campaigns summaries, while LONG_TERM
    groups return linked_campaign_groups. These two fields are mutually exclusive and are both omitted
    for an unknown type. Campaign summaries within a group are not paginated separately. An empty
    summary list does not guarantee that the group contains no campaigns.

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

    Uses the seller-facing campaign group filters and ordering. In the standard flow, priority is given
    to pinned groups, long-term campaigns, registration availability, featured campaigns, campaign
    level, and start time. The pending-confirmation filter prioritizes the most recent join time. EU
    aggregation prioritizes long-term campaigns, followed by pending-confirmation time, registration
    availability, featured campaigns, campaign level, and start time. Custom sorting is not supported.
    Ties retain source order; stable ID ordering is not guaranteed. This query does not mark campaigns
    as visited or update the visit record used by the seller interface to identify new campaigns.

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
        is_invited (bool | Unset):
        only_pending_registrations (bool | Unset):
        list_scope (str | Unset):
        registration_regions (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCampaignGroupResponse
     """


    return sync_detailed(
        client=client,
page_token=page_token,
page_size=page_size,
campaign_name=campaign_name,
is_invited=is_invited,
only_pending_registrations=only_pending_registrations,
list_scope=list_scope,
registration_regions=registration_regions,
locale=locale,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    campaign_name: str | Unset = UNSET,
    is_invited: bool | Unset = UNSET,
    only_pending_registrations: bool | Unset = UNSET,
    list_scope: str | Unset = UNSET,
    registration_regions: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[ListCampaignGroupResponse]:
    """ List Campaign Group

     List campaign groups visible to the shop. NORMAL groups return campaigns summaries, while LONG_TERM
    groups return linked_campaign_groups. These two fields are mutually exclusive and are both omitted
    for an unknown type. Campaign summaries within a group are not paginated separately. An empty
    summary list does not guarantee that the group contains no campaigns.

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

    Uses the seller-facing campaign group filters and ordering. In the standard flow, priority is given
    to pinned groups, long-term campaigns, registration availability, featured campaigns, campaign
    level, and start time. The pending-confirmation filter prioritizes the most recent join time. EU
    aggregation prioritizes long-term campaigns, followed by pending-confirmation time, registration
    availability, featured campaigns, campaign level, and start time. Custom sorting is not supported.
    Ties retain source order; stable ID ordering is not guaranteed. This query does not mark campaigns
    as visited or update the visit record used by the seller interface to identify new campaigns.

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
        is_invited (bool | Unset):
        only_pending_registrations (bool | Unset):
        list_scope (str | Unset):
        registration_regions (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCampaignGroupResponse]
     """


    kwargs = _get_kwargs(
        page_token=page_token,
page_size=page_size,
campaign_name=campaign_name,
is_invited=is_invited,
only_pending_registrations=only_pending_registrations,
list_scope=list_scope,
registration_regions=registration_regions,
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
    is_invited: bool | Unset = UNSET,
    only_pending_registrations: bool | Unset = UNSET,
    list_scope: str | Unset = UNSET,
    registration_regions: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> ListCampaignGroupResponse | None:
    """ List Campaign Group

     List campaign groups visible to the shop. NORMAL groups return campaigns summaries, while LONG_TERM
    groups return linked_campaign_groups. These two fields are mutually exclusive and are both omitted
    for an unknown type. Campaign summaries within a group are not paginated separately. An empty
    summary list does not guarantee that the group contains no campaigns.

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

    Uses the seller-facing campaign group filters and ordering. In the standard flow, priority is given
    to pinned groups, long-term campaigns, registration availability, featured campaigns, campaign
    level, and start time. The pending-confirmation filter prioritizes the most recent join time. EU
    aggregation prioritizes long-term campaigns, followed by pending-confirmation time, registration
    availability, featured campaigns, campaign level, and start time. Custom sorting is not supported.
    Ties retain source order; stable ID ordering is not guaranteed. This query does not mark campaigns
    as visited or update the visit record used by the seller interface to identify new campaigns.

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
        is_invited (bool | Unset):
        only_pending_registrations (bool | Unset):
        list_scope (str | Unset):
        registration_regions (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCampaignGroupResponse
     """


    return (await asyncio_detailed(
        client=client,
page_token=page_token,
page_size=page_size,
campaign_name=campaign_name,
is_invited=is_invited,
only_pending_registrations=only_pending_registrations,
list_scope=list_scope,
registration_regions=registration_regions,
locale=locale,

    )).parsed
