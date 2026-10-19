from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_reject_reasons_response import GetRejectReasonsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    locale: str | Unset = UNSET,
    return_or_cancel_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["locale"] = locale

    params["return_or_cancel_id"] = return_or_cancel_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/return_refund/202309/reject_reasons",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRejectReasonsResponse | None:
    if response.status_code == 200:
        response_200 = GetRejectReasonsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRejectReasonsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    return_or_cancel_id: str,
) -> Response[GetRejectReasonsResponse]:
    """Get Reject Reasons

     Use this API to retrieve the seller reject-reason options currently applicable to the specified
    aftersales request. Use the returned name value as the reject reason key when calling the
    corresponding seller reject API.

    Args:
        locale (str | Unset):
        return_or_cancel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRejectReasonsResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        return_or_cancel_id=return_or_cancel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    return_or_cancel_id: str,
) -> GetRejectReasonsResponse | None:
    """Get Reject Reasons

     Use this API to retrieve the seller reject-reason options currently applicable to the specified
    aftersales request. Use the returned name value as the reject reason key when calling the
    corresponding seller reject API.

    Args:
        locale (str | Unset):
        return_or_cancel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRejectReasonsResponse
    """

    return sync_detailed(
        client=client,
        locale=locale,
        return_or_cancel_id=return_or_cancel_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    return_or_cancel_id: str,
) -> Response[GetRejectReasonsResponse]:
    """Get Reject Reasons

     Use this API to retrieve the seller reject-reason options currently applicable to the specified
    aftersales request. Use the returned name value as the reject reason key when calling the
    corresponding seller reject API.

    Args:
        locale (str | Unset):
        return_or_cancel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRejectReasonsResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        return_or_cancel_id=return_or_cancel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    return_or_cancel_id: str,
) -> GetRejectReasonsResponse | None:
    """Get Reject Reasons

     Use this API to retrieve the seller reject-reason options currently applicable to the specified
    aftersales request. Use the returned name value as the reject reason key when calling the
    corresponding seller reject API.

    Args:
        locale (str | Unset):
        return_or_cancel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRejectReasonsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            locale=locale,
            return_or_cancel_id=return_or_cancel_id,
        )
    ).parsed
