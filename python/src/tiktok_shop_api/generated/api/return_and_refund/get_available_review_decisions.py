from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_available_review_decisions_check_decisions_item import GetAvailableReviewDecisionsCheckDecisionsItem
from ...models.get_available_review_decisions_response import GetAvailableReviewDecisionsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    seller_id: int,
    return_or_cancel_id: str,
    locale: str | Unset = UNSET,
    check_decisions: list[GetAvailableReviewDecisionsCheckDecisionsItem] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["seller_id"] = seller_id

    params["return_or_cancel_id"] = return_or_cancel_id

    params["locale"] = locale

    json_check_decisions: list[str] | Unset = UNSET
    if not isinstance(check_decisions, Unset):
        json_check_decisions = []
        for check_decisions_item_data in check_decisions:
            check_decisions_item = check_decisions_item_data.value
            json_check_decisions.append(check_decisions_item)


    params["check_decisions"] = json_check_decisions


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/return_refund/202606/review_decision",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAvailableReviewDecisionsResponse | None:
    if response.status_code == 200:
        response_200 = GetAvailableReviewDecisionsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAvailableReviewDecisionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    seller_id: int,
    return_or_cancel_id: str,
    locale: str | Unset = UNSET,
    check_decisions: list[GetAvailableReviewDecisionsCheckDecisionsItem] | Unset = UNSET,

) -> Response[GetAvailableReviewDecisionsResponse]:
    """ Get Available Review Decisions

     Description of [GET]/return_refund/:version/Get_Review_Decision

    Args:
        seller_id (int):
        return_or_cancel_id (str):
        locale (str | Unset):
        check_decisions (list[GetAvailableReviewDecisionsCheckDecisionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAvailableReviewDecisionsResponse]
     """


    kwargs = _get_kwargs(
        seller_id=seller_id,
return_or_cancel_id=return_or_cancel_id,
locale=locale,
check_decisions=check_decisions,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    seller_id: int,
    return_or_cancel_id: str,
    locale: str | Unset = UNSET,
    check_decisions: list[GetAvailableReviewDecisionsCheckDecisionsItem] | Unset = UNSET,

) -> GetAvailableReviewDecisionsResponse | None:
    """ Get Available Review Decisions

     Description of [GET]/return_refund/:version/Get_Review_Decision

    Args:
        seller_id (int):
        return_or_cancel_id (str):
        locale (str | Unset):
        check_decisions (list[GetAvailableReviewDecisionsCheckDecisionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAvailableReviewDecisionsResponse
     """


    return sync_detailed(
        client=client,
seller_id=seller_id,
return_or_cancel_id=return_or_cancel_id,
locale=locale,
check_decisions=check_decisions,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    seller_id: int,
    return_or_cancel_id: str,
    locale: str | Unset = UNSET,
    check_decisions: list[GetAvailableReviewDecisionsCheckDecisionsItem] | Unset = UNSET,

) -> Response[GetAvailableReviewDecisionsResponse]:
    """ Get Available Review Decisions

     Description of [GET]/return_refund/:version/Get_Review_Decision

    Args:
        seller_id (int):
        return_or_cancel_id (str):
        locale (str | Unset):
        check_decisions (list[GetAvailableReviewDecisionsCheckDecisionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAvailableReviewDecisionsResponse]
     """


    kwargs = _get_kwargs(
        seller_id=seller_id,
return_or_cancel_id=return_or_cancel_id,
locale=locale,
check_decisions=check_decisions,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    seller_id: int,
    return_or_cancel_id: str,
    locale: str | Unset = UNSET,
    check_decisions: list[GetAvailableReviewDecisionsCheckDecisionsItem] | Unset = UNSET,

) -> GetAvailableReviewDecisionsResponse | None:
    """ Get Available Review Decisions

     Description of [GET]/return_refund/:version/Get_Review_Decision

    Args:
        seller_id (int):
        return_or_cancel_id (str):
        locale (str | Unset):
        check_decisions (list[GetAvailableReviewDecisionsCheckDecisionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAvailableReviewDecisionsResponse
     """


    return (await asyncio_detailed(
        client=client,
seller_id=seller_id,
return_or_cancel_id=return_or_cancel_id,
locale=locale,
check_decisions=check_decisions,

    )).parsed
