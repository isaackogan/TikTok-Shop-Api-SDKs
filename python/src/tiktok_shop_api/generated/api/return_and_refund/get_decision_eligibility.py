from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_decision_eligibility_check_decisions_item import GetDecisionEligibilityCheckDecisionsItem
from ...models.get_decision_eligibility_response import GetDecisionEligibilityResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    return_or_cancel_id: str,
    check_decisions: list[GetDecisionEligibilityCheckDecisionsItem] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["return_or_cancel_id"] = return_or_cancel_id

    json_check_decisions: list[str] | Unset = UNSET
    if not isinstance(check_decisions, Unset):
        json_check_decisions = []
        for check_decisions_item_data in check_decisions:
            check_decisions_item = check_decisions_item_data.value
            json_check_decisions.append(check_decisions_item)


    params["check_decisions"] = json_check_decisions

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/return_refund/202601/decision_eligibility",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetDecisionEligibilityResponse | None:
    if response.status_code == 200:
        response_200 = GetDecisionEligibilityResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetDecisionEligibilityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    return_or_cancel_id: str,
    check_decisions: list[GetDecisionEligibilityCheckDecisionsItem] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[GetDecisionEligibilityResponse]:
    """ Get Decision Eligibility

     Use this API to evaluate which seller decisions are currently allowed for the specified aftersales
    request. The API returns one result per requested decision, including whether the decision is
    currently eligible and any rejection reasons that are applicable for an eligible reject decision.

    Args:
        return_or_cancel_id (str):
        check_decisions (list[GetDecisionEligibilityCheckDecisionsItem] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDecisionEligibilityResponse]
     """


    kwargs = _get_kwargs(
        return_or_cancel_id=return_or_cancel_id,
check_decisions=check_decisions,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    return_or_cancel_id: str,
    check_decisions: list[GetDecisionEligibilityCheckDecisionsItem] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> GetDecisionEligibilityResponse | None:
    """ Get Decision Eligibility

     Use this API to evaluate which seller decisions are currently allowed for the specified aftersales
    request. The API returns one result per requested decision, including whether the decision is
    currently eligible and any rejection reasons that are applicable for an eligible reject decision.

    Args:
        return_or_cancel_id (str):
        check_decisions (list[GetDecisionEligibilityCheckDecisionsItem] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDecisionEligibilityResponse
     """


    return sync_detailed(
        client=client,
return_or_cancel_id=return_or_cancel_id,
check_decisions=check_decisions,
locale=locale,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    return_or_cancel_id: str,
    check_decisions: list[GetDecisionEligibilityCheckDecisionsItem] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[GetDecisionEligibilityResponse]:
    """ Get Decision Eligibility

     Use this API to evaluate which seller decisions are currently allowed for the specified aftersales
    request. The API returns one result per requested decision, including whether the decision is
    currently eligible and any rejection reasons that are applicable for an eligible reject decision.

    Args:
        return_or_cancel_id (str):
        check_decisions (list[GetDecisionEligibilityCheckDecisionsItem] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDecisionEligibilityResponse]
     """


    kwargs = _get_kwargs(
        return_or_cancel_id=return_or_cancel_id,
check_decisions=check_decisions,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    return_or_cancel_id: str,
    check_decisions: list[GetDecisionEligibilityCheckDecisionsItem] | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> GetDecisionEligibilityResponse | None:
    """ Get Decision Eligibility

     Use this API to evaluate which seller decisions are currently allowed for the specified aftersales
    request. The API returns one result per requested decision, including whether the decision is
    currently eligible and any rejection reasons that are applicable for an eligible reject decision.

    Args:
        return_or_cancel_id (str):
        check_decisions (list[GetDecisionEligibilityCheckDecisionsItem] | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDecisionEligibilityResponse
     """


    return (await asyncio_detailed(
        client=client,
return_or_cancel_id=return_or_cancel_id,
check_decisions=check_decisions,
locale=locale,

    )).parsed
