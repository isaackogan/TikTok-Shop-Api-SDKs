from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_product_listing_request import CheckProductListingRequest
from ...models.check_product_listing_response import CheckProductListingResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CheckProductListingRequest,
    is_diagnosis_required: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["is_diagnosis_required"] = is_diagnosis_required

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/products/listing_check",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CheckProductListingResponse | None:
    if response.status_code == 200:
        response_200 = CheckProductListingResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CheckProductListingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckProductListingRequest,
    is_diagnosis_required: bool | Unset = UNSET,
) -> Response[CheckProductListingResponse]:
    """Check Product Listing

     Identify any issues with your product properties in advance to ensure your product is ready for
    listing.
    Every product must meet TikTok Shop requirements before it can be listed. Before listing, you can
    submit all relevant product information to this API to check whether a listing meets these
    requirements. You'll receive a list of issues to resolve before listing. This process helps reduce
    the risk of failure when creating products.
    **Note**:
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        is_diagnosis_required (bool | Unset):
        body (CheckProductListingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckProductListingResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        is_diagnosis_required=is_diagnosis_required,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CheckProductListingRequest,
    is_diagnosis_required: bool | Unset = UNSET,
) -> CheckProductListingResponse | None:
    """Check Product Listing

     Identify any issues with your product properties in advance to ensure your product is ready for
    listing.
    Every product must meet TikTok Shop requirements before it can be listed. Before listing, you can
    submit all relevant product information to this API to check whether a listing meets these
    requirements. You'll receive a list of issues to resolve before listing. This process helps reduce
    the risk of failure when creating products.
    **Note**:
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        is_diagnosis_required (bool | Unset):
        body (CheckProductListingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckProductListingResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        is_diagnosis_required=is_diagnosis_required,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckProductListingRequest,
    is_diagnosis_required: bool | Unset = UNSET,
) -> Response[CheckProductListingResponse]:
    """Check Product Listing

     Identify any issues with your product properties in advance to ensure your product is ready for
    listing.
    Every product must meet TikTok Shop requirements before it can be listed. Before listing, you can
    submit all relevant product information to this API to check whether a listing meets these
    requirements. You'll receive a list of issues to resolve before listing. This process helps reduce
    the risk of failure when creating products.
    **Note**:
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        is_diagnosis_required (bool | Unset):
        body (CheckProductListingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckProductListingResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        is_diagnosis_required=is_diagnosis_required,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CheckProductListingRequest,
    is_diagnosis_required: bool | Unset = UNSET,
) -> CheckProductListingResponse | None:
    """Check Product Listing

     Identify any issues with your product properties in advance to ensure your product is ready for
    listing.
    Every product must meet TikTok Shop requirements before it can be listed. Before listing, you can
    submit all relevant product information to this API to check whether a listing meets these
    requirements. You'll receive a list of issues to resolve before listing. This process helps reduce
    the risk of failure when creating products.
    **Note**:
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        is_diagnosis_required (bool | Unset):
        body (CheckProductListingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckProductListingResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            is_diagnosis_required=is_diagnosis_required,
        )
    ).parsed
