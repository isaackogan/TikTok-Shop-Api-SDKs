from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.edit_open_collaboration_sample_rule_request import EditOpenCollaborationSampleRuleRequest
from ...models.edit_open_collaboration_sample_rule_response import EditOpenCollaborationSampleRuleResponse
from typing import cast



def _get_kwargs(
    *,
    body: EditOpenCollaborationSampleRuleRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202410/open_collaborations/sample_rules",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EditOpenCollaborationSampleRuleResponse | None:
    if response.status_code == 200:
        response_200 = EditOpenCollaborationSampleRuleResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EditOpenCollaborationSampleRuleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EditOpenCollaborationSampleRuleRequest,

) -> Response[EditOpenCollaborationSampleRuleResponse]:
    """ Edit Open Collaboration Sample Rule

     Use this API to manage sample rules in open collaborations, like valid time periods, or thresholds
    for creators to request samples. You can create, update, or deactivate rules.

    Args:
        body (EditOpenCollaborationSampleRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditOpenCollaborationSampleRuleResponse]
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
    body: EditOpenCollaborationSampleRuleRequest,

) -> EditOpenCollaborationSampleRuleResponse | None:
    """ Edit Open Collaboration Sample Rule

     Use this API to manage sample rules in open collaborations, like valid time periods, or thresholds
    for creators to request samples. You can create, update, or deactivate rules.

    Args:
        body (EditOpenCollaborationSampleRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditOpenCollaborationSampleRuleResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EditOpenCollaborationSampleRuleRequest,

) -> Response[EditOpenCollaborationSampleRuleResponse]:
    """ Edit Open Collaboration Sample Rule

     Use this API to manage sample rules in open collaborations, like valid time periods, or thresholds
    for creators to request samples. You can create, update, or deactivate rules.

    Args:
        body (EditOpenCollaborationSampleRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditOpenCollaborationSampleRuleResponse]
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
    body: EditOpenCollaborationSampleRuleRequest,

) -> EditOpenCollaborationSampleRuleResponse | None:
    """ Edit Open Collaboration Sample Rule

     Use this API to manage sample rules in open collaborations, like valid time periods, or thresholds
    for creators to request samples. You can create, update, or deactivate rules.

    Args:
        body (EditOpenCollaborationSampleRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditOpenCollaborationSampleRuleResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
