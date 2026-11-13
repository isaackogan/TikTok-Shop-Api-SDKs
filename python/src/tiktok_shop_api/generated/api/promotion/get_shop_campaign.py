from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_campaign_response import GetShopCampaignResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    shop_campaign_id: str,
    *,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/promotion/202611/shop_campaigns/{shop_campaign_id}".format(shop_campaign_id=quote(str(shop_campaign_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopCampaignResponse | None:
    if response.status_code == 200:
        response_200 = GetShopCampaignResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopCampaignResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    shop_campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Response[GetShopCampaignResponse]:
    """ Get Shop Campaign

     Get a shop campaign's basic information, registration period, shop participation requirements,
    benefits and fees, shop eligibility, and participation statistics. Shop details do not include
    product registration quotas, product registration rules, or product statistics.

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

    Missing or inconsistent data required to identify or return the campaign results in a system error,
    not a resource-unavailable error. Missing optional information only omits the corresponding fields.
    An existing campaign that the shop cannot register for is still returned with its eligibility or
    blocking reasons.
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
    campaign's localization rules. The campaign description field returns sanitized HTML, with scripts,
    event-handler attributes, and unsafe URLs removed. This guarantee applies only to the campaign
    description, not to other text fields or nested descriptions. Treat other text as text, not trusted
    HTML. Unavailable text is omitted rather than replaced with a placeholder name.

    A type mismatch, nonexistent or invisible campaign, or inapplicable region returns a resource-
    unavailable error rather than a successful empty result. Unknown eligibility or registration
    availability alone does not fail the query. registration_period.status is determined only from
    query_time and registration boundaries, not campaign_status. The registration interval includes its
    end time; campaign and fee validity intervals exclude their end times. Rules, benefits, and fee
    policies are the complete applicable configuration of a single campaign, not product or registration
    record lists, and are neither paginated nor truncated. Fee text and resources jointly express the
    terms; omission does not mean free participation.

    Args:
        shop_campaign_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopCampaignResponse]
     """


    kwargs = _get_kwargs(
        shop_campaign_id=shop_campaign_id,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    shop_campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> GetShopCampaignResponse | None:
    """ Get Shop Campaign

     Get a shop campaign's basic information, registration period, shop participation requirements,
    benefits and fees, shop eligibility, and participation statistics. Shop details do not include
    product registration quotas, product registration rules, or product statistics.

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

    Missing or inconsistent data required to identify or return the campaign results in a system error,
    not a resource-unavailable error. Missing optional information only omits the corresponding fields.
    An existing campaign that the shop cannot register for is still returned with its eligibility or
    blocking reasons.
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
    campaign's localization rules. The campaign description field returns sanitized HTML, with scripts,
    event-handler attributes, and unsafe URLs removed. This guarantee applies only to the campaign
    description, not to other text fields or nested descriptions. Treat other text as text, not trusted
    HTML. Unavailable text is omitted rather than replaced with a placeholder name.

    A type mismatch, nonexistent or invisible campaign, or inapplicable region returns a resource-
    unavailable error rather than a successful empty result. Unknown eligibility or registration
    availability alone does not fail the query. registration_period.status is determined only from
    query_time and registration boundaries, not campaign_status. The registration interval includes its
    end time; campaign and fee validity intervals exclude their end times. Rules, benefits, and fee
    policies are the complete applicable configuration of a single campaign, not product or registration
    record lists, and are neither paginated nor truncated. Fee text and resources jointly express the
    terms; omission does not mean free participation.

    Args:
        shop_campaign_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopCampaignResponse
     """


    return sync_detailed(
        shop_campaign_id=shop_campaign_id,
client=client,
locale=locale,

    ).parsed

async def asyncio_detailed(
    shop_campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Response[GetShopCampaignResponse]:
    """ Get Shop Campaign

     Get a shop campaign's basic information, registration period, shop participation requirements,
    benefits and fees, shop eligibility, and participation statistics. Shop details do not include
    product registration quotas, product registration rules, or product statistics.

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

    Missing or inconsistent data required to identify or return the campaign results in a system error,
    not a resource-unavailable error. Missing optional information only omits the corresponding fields.
    An existing campaign that the shop cannot register for is still returned with its eligibility or
    blocking reasons.
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
    campaign's localization rules. The campaign description field returns sanitized HTML, with scripts,
    event-handler attributes, and unsafe URLs removed. This guarantee applies only to the campaign
    description, not to other text fields or nested descriptions. Treat other text as text, not trusted
    HTML. Unavailable text is omitted rather than replaced with a placeholder name.

    A type mismatch, nonexistent or invisible campaign, or inapplicable region returns a resource-
    unavailable error rather than a successful empty result. Unknown eligibility or registration
    availability alone does not fail the query. registration_period.status is determined only from
    query_time and registration boundaries, not campaign_status. The registration interval includes its
    end time; campaign and fee validity intervals exclude their end times. Rules, benefits, and fee
    policies are the complete applicable configuration of a single campaign, not product or registration
    record lists, and are neither paginated nor truncated. Fee text and resources jointly express the
    terms; omission does not mean free participation.

    Args:
        shop_campaign_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopCampaignResponse]
     """


    kwargs = _get_kwargs(
        shop_campaign_id=shop_campaign_id,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    shop_campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> GetShopCampaignResponse | None:
    """ Get Shop Campaign

     Get a shop campaign's basic information, registration period, shop participation requirements,
    benefits and fees, shop eligibility, and participation statistics. Shop details do not include
    product registration quotas, product registration rules, or product statistics.

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

    Missing or inconsistent data required to identify or return the campaign results in a system error,
    not a resource-unavailable error. Missing optional information only omits the corresponding fields.
    An existing campaign that the shop cannot register for is still returned with its eligibility or
    blocking reasons.
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
    campaign's localization rules. The campaign description field returns sanitized HTML, with scripts,
    event-handler attributes, and unsafe URLs removed. This guarantee applies only to the campaign
    description, not to other text fields or nested descriptions. Treat other text as text, not trusted
    HTML. Unavailable text is omitted rather than replaced with a placeholder name.

    A type mismatch, nonexistent or invisible campaign, or inapplicable region returns a resource-
    unavailable error rather than a successful empty result. Unknown eligibility or registration
    availability alone does not fail the query. registration_period.status is determined only from
    query_time and registration boundaries, not campaign_status. The registration interval includes its
    end time; campaign and fee validity intervals exclude their end times. Rules, benefits, and fee
    policies are the complete applicable configuration of a single campaign, not product or registration
    record lists, and are neither paginated nor truncated. Fee text and resources jointly express the
    terms; omission does not mean free participation.

    Args:
        shop_campaign_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopCampaignResponse
     """


    return (await asyncio_detailed(
        shop_campaign_id=shop_campaign_id,
client=client,
locale=locale,

    )).parsed
