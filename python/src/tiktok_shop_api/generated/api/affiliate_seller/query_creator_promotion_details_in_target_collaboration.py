from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.query_creator_promotion_details_in_target_collaboration_request import QueryCreatorPromotionDetailsInTargetCollaborationRequest
from ...models.query_creator_promotion_details_in_target_collaboration_response import QueryCreatorPromotionDetailsInTargetCollaborationResponse
from typing import cast



def _get_kwargs(
    *,
    body: QueryCreatorPromotionDetailsInTargetCollaborationRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202608/target_collaborations/creator_promotion_details/query",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> QueryCreatorPromotionDetailsInTargetCollaborationResponse | None:
    if response.status_code == 200:
        response_200 = QueryCreatorPromotionDetailsInTargetCollaborationResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[QueryCreatorPromotionDetailsInTargetCollaborationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QueryCreatorPromotionDetailsInTargetCollaborationRequest,

) -> Response[QueryCreatorPromotionDetailsInTargetCollaborationResponse]:
    """ Query Creator Promotion Details in Target Collaboration

     Query the creator commission rate, number of promotional video contents and number of live‑stream
    promotions for specified creator, specified invitation and specified product.

    Args:
        body (QueryCreatorPromotionDetailsInTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryCreatorPromotionDetailsInTargetCollaborationResponse]
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
    body: QueryCreatorPromotionDetailsInTargetCollaborationRequest,

) -> QueryCreatorPromotionDetailsInTargetCollaborationResponse | None:
    """ Query Creator Promotion Details in Target Collaboration

     Query the creator commission rate, number of promotional video contents and number of live‑stream
    promotions for specified creator, specified invitation and specified product.

    Args:
        body (QueryCreatorPromotionDetailsInTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueryCreatorPromotionDetailsInTargetCollaborationResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QueryCreatorPromotionDetailsInTargetCollaborationRequest,

) -> Response[QueryCreatorPromotionDetailsInTargetCollaborationResponse]:
    """ Query Creator Promotion Details in Target Collaboration

     Query the creator commission rate, number of promotional video contents and number of live‑stream
    promotions for specified creator, specified invitation and specified product.

    Args:
        body (QueryCreatorPromotionDetailsInTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryCreatorPromotionDetailsInTargetCollaborationResponse]
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
    body: QueryCreatorPromotionDetailsInTargetCollaborationRequest,

) -> QueryCreatorPromotionDetailsInTargetCollaborationResponse | None:
    """ Query Creator Promotion Details in Target Collaboration

     Query the creator commission rate, number of promotional video contents and number of live‑stream
    promotions for specified creator, specified invitation and specified product.

    Args:
        body (QueryCreatorPromotionDetailsInTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueryCreatorPromotionDetailsInTargetCollaborationResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
