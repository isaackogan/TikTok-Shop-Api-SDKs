from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.end_session_request import EndSessionRequest
from ...models.end_session_response import EndSessionResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    conversation_id: str,
    session_id: str,
    *,
    body: EndSessionRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/customer_service/202605/conversations/{conversation_id}/sessions/{session_id}/end".format(conversation_id=quote(str(conversation_id), safe=""),session_id=quote(str(session_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EndSessionResponse | None:
    if response.status_code == 200:
        response_200 = EndSessionResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EndSessionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conversation_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EndSessionRequest | Unset = UNSET,

) -> Response[EndSessionResponse]:
    """ End Session

     Use this API to end an active customer service session assigned to an agent.

    Args:
        conversation_id (str):
        session_id (str):
        body (EndSessionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndSessionResponse]
     """


    kwargs = _get_kwargs(
        conversation_id=conversation_id,
session_id=session_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    conversation_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EndSessionRequest | Unset = UNSET,

) -> EndSessionResponse | None:
    """ End Session

     Use this API to end an active customer service session assigned to an agent.

    Args:
        conversation_id (str):
        session_id (str):
        body (EndSessionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndSessionResponse
     """


    return sync_detailed(
        conversation_id=conversation_id,
session_id=session_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    conversation_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EndSessionRequest | Unset = UNSET,

) -> Response[EndSessionResponse]:
    """ End Session

     Use this API to end an active customer service session assigned to an agent.

    Args:
        conversation_id (str):
        session_id (str):
        body (EndSessionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndSessionResponse]
     """


    kwargs = _get_kwargs(
        conversation_id=conversation_id,
session_id=session_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    conversation_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EndSessionRequest | Unset = UNSET,

) -> EndSessionResponse | None:
    """ End Session

     Use this API to end an active customer service session assigned to an agent.

    Args:
        conversation_id (str):
        session_id (str):
        body (EndSessionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndSessionResponse
     """


    return (await asyncio_detailed(
        conversation_id=conversation_id,
session_id=session_id,
client=client,
body=body,

    )).parsed
