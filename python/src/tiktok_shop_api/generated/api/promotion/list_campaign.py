from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_campaign_response import ListCampaignResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    campaign_group_id: str,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    eligibility_filter: str | Unset = UNSET,
    only_pending_registrations: bool | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["campaign_group_id"] = campaign_group_id

    params["page_token"] = page_token

    params["page_size"] = page_size

    params["eligibility_filter"] = eligibility_filter

    params["only_pending_registrations"] = only_pending_registrations

    json_types: list[str] | Unset = UNSET
    if not isinstance(types, Unset):
        json_types = types


    params["types"] = json_types

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/promotion/202611/campaigns",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListCampaignResponse | None:
    if response.status_code == 200:
        response_200 = ListCampaignResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListCampaignResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    campaign_group_id: str,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    eligibility_filter: str | Unset = UNSET,
    only_pending_registrations: bool | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[ListCampaignResponse]:
    """ List Campaign

     List unified Campaign summaries visible to the shop within a specified campaign group.
    campaign_group_id is a required query parameter. Supports product, shop, livestream, and short video
    campaigns without expanding their full details.

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

    For a single-shop query, the default order prioritizes campaigns available for registration when
    that assessment is present for both campaigns, followed by pinned campaigns, the most recent
    pending-confirmation time descending, invited campaigns, and creation time descending. With
    only_pending_registrations=true, the most recent pending-confirmation time takes precedence over
    those default priorities. After page selection, any applicable campaign-group display priority
    orders configured campaigns first in their configured sequence; other items retain their relative
    order. Equal priorities retain source order; stable ID ordering is not guaranteed. EU cross-shop
    queries apply the query order separately to each shop, then merge results and apply the display
    priority within the returned page; no global ordering across shops is guaranteed. Custom sorting is
    not supported. No additional sorting, deduplication, or truncation is applied by this API. List-
    level eligibility is not the full detail-level assessment; use type to select the detail endpoint.
    EU cross-shop aggregation may return more items than page_size. total_count is not guaranteed to be
    an exact deduplicated total across all accessible shops, and complete traversal of that scope is not
    guaranteed even when the data remains unchanged.

    For the first page, omit page_token or pass an empty string. For subsequent pages, pass
    next_page_token unchanged and keep the authorized shop, filters, and page_size unchanged. An empty
    next_page_token means there are no further pages within the current query scope; it does not
    guarantee that all historical campaigns or campaigns accessible across shops have been retrieved. An
    empty page is not necessarily the last page. Do not stop pagination based on the number of returned
    items.

    Args:
        campaign_group_id (str):
        page_token (str | Unset):
        page_size (int | Unset):
        eligibility_filter (str | Unset):
        only_pending_registrations (bool | Unset):
        types (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCampaignResponse]
     """


    kwargs = _get_kwargs(
        campaign_group_id=campaign_group_id,
page_token=page_token,
page_size=page_size,
eligibility_filter=eligibility_filter,
only_pending_registrations=only_pending_registrations,
types=types,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    campaign_group_id: str,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    eligibility_filter: str | Unset = UNSET,
    only_pending_registrations: bool | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> ListCampaignResponse | None:
    """ List Campaign

     List unified Campaign summaries visible to the shop within a specified campaign group.
    campaign_group_id is a required query parameter. Supports product, shop, livestream, and short video
    campaigns without expanding their full details.

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

    For a single-shop query, the default order prioritizes campaigns available for registration when
    that assessment is present for both campaigns, followed by pinned campaigns, the most recent
    pending-confirmation time descending, invited campaigns, and creation time descending. With
    only_pending_registrations=true, the most recent pending-confirmation time takes precedence over
    those default priorities. After page selection, any applicable campaign-group display priority
    orders configured campaigns first in their configured sequence; other items retain their relative
    order. Equal priorities retain source order; stable ID ordering is not guaranteed. EU cross-shop
    queries apply the query order separately to each shop, then merge results and apply the display
    priority within the returned page; no global ordering across shops is guaranteed. Custom sorting is
    not supported. No additional sorting, deduplication, or truncation is applied by this API. List-
    level eligibility is not the full detail-level assessment; use type to select the detail endpoint.
    EU cross-shop aggregation may return more items than page_size. total_count is not guaranteed to be
    an exact deduplicated total across all accessible shops, and complete traversal of that scope is not
    guaranteed even when the data remains unchanged.

    For the first page, omit page_token or pass an empty string. For subsequent pages, pass
    next_page_token unchanged and keep the authorized shop, filters, and page_size unchanged. An empty
    next_page_token means there are no further pages within the current query scope; it does not
    guarantee that all historical campaigns or campaigns accessible across shops have been retrieved. An
    empty page is not necessarily the last page. Do not stop pagination based on the number of returned
    items.

    Args:
        campaign_group_id (str):
        page_token (str | Unset):
        page_size (int | Unset):
        eligibility_filter (str | Unset):
        only_pending_registrations (bool | Unset):
        types (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCampaignResponse
     """


    return sync_detailed(
        client=client,
campaign_group_id=campaign_group_id,
page_token=page_token,
page_size=page_size,
eligibility_filter=eligibility_filter,
only_pending_registrations=only_pending_registrations,
types=types,
locale=locale,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    campaign_group_id: str,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    eligibility_filter: str | Unset = UNSET,
    only_pending_registrations: bool | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[ListCampaignResponse]:
    """ List Campaign

     List unified Campaign summaries visible to the shop within a specified campaign group.
    campaign_group_id is a required query parameter. Supports product, shop, livestream, and short video
    campaigns without expanding their full details.

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

    For a single-shop query, the default order prioritizes campaigns available for registration when
    that assessment is present for both campaigns, followed by pinned campaigns, the most recent
    pending-confirmation time descending, invited campaigns, and creation time descending. With
    only_pending_registrations=true, the most recent pending-confirmation time takes precedence over
    those default priorities. After page selection, any applicable campaign-group display priority
    orders configured campaigns first in their configured sequence; other items retain their relative
    order. Equal priorities retain source order; stable ID ordering is not guaranteed. EU cross-shop
    queries apply the query order separately to each shop, then merge results and apply the display
    priority within the returned page; no global ordering across shops is guaranteed. Custom sorting is
    not supported. No additional sorting, deduplication, or truncation is applied by this API. List-
    level eligibility is not the full detail-level assessment; use type to select the detail endpoint.
    EU cross-shop aggregation may return more items than page_size. total_count is not guaranteed to be
    an exact deduplicated total across all accessible shops, and complete traversal of that scope is not
    guaranteed even when the data remains unchanged.

    For the first page, omit page_token or pass an empty string. For subsequent pages, pass
    next_page_token unchanged and keep the authorized shop, filters, and page_size unchanged. An empty
    next_page_token means there are no further pages within the current query scope; it does not
    guarantee that all historical campaigns or campaigns accessible across shops have been retrieved. An
    empty page is not necessarily the last page. Do not stop pagination based on the number of returned
    items.

    Args:
        campaign_group_id (str):
        page_token (str | Unset):
        page_size (int | Unset):
        eligibility_filter (str | Unset):
        only_pending_registrations (bool | Unset):
        types (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCampaignResponse]
     """


    kwargs = _get_kwargs(
        campaign_group_id=campaign_group_id,
page_token=page_token,
page_size=page_size,
eligibility_filter=eligibility_filter,
only_pending_registrations=only_pending_registrations,
types=types,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    campaign_group_id: str,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    eligibility_filter: str | Unset = UNSET,
    only_pending_registrations: bool | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> ListCampaignResponse | None:
    """ List Campaign

     List unified Campaign summaries visible to the shop within a specified campaign group.
    campaign_group_id is a required query parameter. Supports product, shop, livestream, and short video
    campaigns without expanding their full details.

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

    For a single-shop query, the default order prioritizes campaigns available for registration when
    that assessment is present for both campaigns, followed by pinned campaigns, the most recent
    pending-confirmation time descending, invited campaigns, and creation time descending. With
    only_pending_registrations=true, the most recent pending-confirmation time takes precedence over
    those default priorities. After page selection, any applicable campaign-group display priority
    orders configured campaigns first in their configured sequence; other items retain their relative
    order. Equal priorities retain source order; stable ID ordering is not guaranteed. EU cross-shop
    queries apply the query order separately to each shop, then merge results and apply the display
    priority within the returned page; no global ordering across shops is guaranteed. Custom sorting is
    not supported. No additional sorting, deduplication, or truncation is applied by this API. List-
    level eligibility is not the full detail-level assessment; use type to select the detail endpoint.
    EU cross-shop aggregation may return more items than page_size. total_count is not guaranteed to be
    an exact deduplicated total across all accessible shops, and complete traversal of that scope is not
    guaranteed even when the data remains unchanged.

    For the first page, omit page_token or pass an empty string. For subsequent pages, pass
    next_page_token unchanged and keep the authorized shop, filters, and page_size unchanged. An empty
    next_page_token means there are no further pages within the current query scope; it does not
    guarantee that all historical campaigns or campaigns accessible across shops have been retrieved. An
    empty page is not necessarily the last page. Do not stop pagination based on the number of returned
    items.

    Args:
        campaign_group_id (str):
        page_token (str | Unset):
        page_size (int | Unset):
        eligibility_filter (str | Unset):
        only_pending_registrations (bool | Unset):
        types (list[str] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCampaignResponse
     """


    return (await asyncio_detailed(
        client=client,
campaign_group_id=campaign_group_id,
page_token=page_token,
page_size=page_size,
eligibility_filter=eligibility_filter,
only_pending_registrations=only_pending_registrations,
types=types,
locale=locale,

    )).parsed
