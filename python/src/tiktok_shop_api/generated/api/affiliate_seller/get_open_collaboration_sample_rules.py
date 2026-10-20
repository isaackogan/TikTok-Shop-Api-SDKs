from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_open_collaboration_sample_rules_response import GetOpenCollaborationSampleRulesResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    product_ids: list[str],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product_ids = product_ids

    params["product_ids"] = json_product_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202410/open_collaborations/sample_rules",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetOpenCollaborationSampleRulesResponse | None:
    if response.status_code == 200:
        response_200 = GetOpenCollaborationSampleRulesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetOpenCollaborationSampleRulesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> Response[GetOpenCollaborationSampleRulesResponse]:
    """Get Open Collaboration Sample Rules

     Use this API to get the status and the details of the sample rules for products under an open
    collaboration. With this API, you can efficiently review the sample distribution criteria for
    products within the open collaboration context.

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOpenCollaborationSampleRulesResponse]
    """

    kwargs = _get_kwargs(
        product_ids=product_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> GetOpenCollaborationSampleRulesResponse | None:
    """Get Open Collaboration Sample Rules

     Use this API to get the status and the details of the sample rules for products under an open
    collaboration. With this API, you can efficiently review the sample distribution criteria for
    products within the open collaboration context.

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOpenCollaborationSampleRulesResponse
    """

    return sync_detailed(
        client=client,
        product_ids=product_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> Response[GetOpenCollaborationSampleRulesResponse]:
    """Get Open Collaboration Sample Rules

     Use this API to get the status and the details of the sample rules for products under an open
    collaboration. With this API, you can efficiently review the sample distribution criteria for
    products within the open collaboration context.

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOpenCollaborationSampleRulesResponse]
    """

    kwargs = _get_kwargs(
        product_ids=product_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> GetOpenCollaborationSampleRulesResponse | None:
    """Get Open Collaboration Sample Rules

     Use this API to get the status and the details of the sample rules for products under an open
    collaboration. With this API, you can efficiently review the sample distribution criteria for
    products within the open collaboration context.

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOpenCollaborationSampleRulesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            product_ids=product_ids,
        )
    ).parsed
