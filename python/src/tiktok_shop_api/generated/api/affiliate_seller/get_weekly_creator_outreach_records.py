from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_weekly_creator_outreach_records_request import GetWeeklyCreatorOutreachRecordsRequest
from ...models.get_weekly_creator_outreach_records_response import GetWeeklyCreatorOutreachRecordsResponse
from typing import cast



def _get_kwargs(
    *,
    body: GetWeeklyCreatorOutreachRecordsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202608/creator_outreach/records/query",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetWeeklyCreatorOutreachRecordsResponse | None:
    if response.status_code == 200:
        response_200 = GetWeeklyCreatorOutreachRecordsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetWeeklyCreatorOutreachRecordsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetWeeklyCreatorOutreachRecordsRequest,

) -> Response[GetWeeklyCreatorOutreachRecordsResponse]:
    """ Get Weekly Creator Outreach Records

     Query weekly detailed outreach‑invitation records for a specified seller, including whether IM
    messages/invitations were sent to a unconnected creator, and whether the creator added products or
    replied to IM messages.

    Args:
        body (GetWeeklyCreatorOutreachRecordsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWeeklyCreatorOutreachRecordsResponse]
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
    body: GetWeeklyCreatorOutreachRecordsRequest,

) -> GetWeeklyCreatorOutreachRecordsResponse | None:
    """ Get Weekly Creator Outreach Records

     Query weekly detailed outreach‑invitation records for a specified seller, including whether IM
    messages/invitations were sent to a unconnected creator, and whether the creator added products or
    replied to IM messages.

    Args:
        body (GetWeeklyCreatorOutreachRecordsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWeeklyCreatorOutreachRecordsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetWeeklyCreatorOutreachRecordsRequest,

) -> Response[GetWeeklyCreatorOutreachRecordsResponse]:
    """ Get Weekly Creator Outreach Records

     Query weekly detailed outreach‑invitation records for a specified seller, including whether IM
    messages/invitations were sent to a unconnected creator, and whether the creator added products or
    replied to IM messages.

    Args:
        body (GetWeeklyCreatorOutreachRecordsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWeeklyCreatorOutreachRecordsResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetWeeklyCreatorOutreachRecordsRequest,

) -> GetWeeklyCreatorOutreachRecordsResponse | None:
    """ Get Weekly Creator Outreach Records

     Query weekly detailed outreach‑invitation records for a specified seller, including whether IM
    messages/invitations were sent to a unconnected creator, and whether the creator added products or
    replied to IM messages.

    Args:
        body (GetWeeklyCreatorOutreachRecordsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWeeklyCreatorOutreachRecordsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
