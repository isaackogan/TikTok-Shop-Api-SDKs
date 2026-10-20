from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.predict_product_package_dimensions_and_weight_request import (
    PredictProductPackageDimensionsAndWeightRequest,
)
from ...models.predict_product_package_dimensions_and_weight_response import (
    PredictProductPackageDimensionsAndWeightResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PredictProductPackageDimensionsAndWeightRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202609/products/package/predict",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PredictProductPackageDimensionsAndWeightResponse | None:
    if response.status_code == 200:
        response_200 = PredictProductPackageDimensionsAndWeightResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PredictProductPackageDimensionsAndWeightResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PredictProductPackageDimensionsAndWeightRequest,
) -> Response[PredictProductPackageDimensionsAndWeightResponse]:
    """Predict Product Package Dimensions and Weight

     Predicts the package dimensions and weight for one candidate product based on its leaf category. The
    result is generated synchronously and can be used to prepare the package information in a create or
    edit product request. When no prediction is available, `data` is an empty object.

    Args:
        body (PredictProductPackageDimensionsAndWeightRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PredictProductPackageDimensionsAndWeightResponse]
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
    body: PredictProductPackageDimensionsAndWeightRequest,
) -> PredictProductPackageDimensionsAndWeightResponse | None:
    """Predict Product Package Dimensions and Weight

     Predicts the package dimensions and weight for one candidate product based on its leaf category. The
    result is generated synchronously and can be used to prepare the package information in a create or
    edit product request. When no prediction is available, `data` is an empty object.

    Args:
        body (PredictProductPackageDimensionsAndWeightRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PredictProductPackageDimensionsAndWeightResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PredictProductPackageDimensionsAndWeightRequest,
) -> Response[PredictProductPackageDimensionsAndWeightResponse]:
    """Predict Product Package Dimensions and Weight

     Predicts the package dimensions and weight for one candidate product based on its leaf category. The
    result is generated synchronously and can be used to prepare the package information in a create or
    edit product request. When no prediction is available, `data` is an empty object.

    Args:
        body (PredictProductPackageDimensionsAndWeightRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PredictProductPackageDimensionsAndWeightResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PredictProductPackageDimensionsAndWeightRequest,
) -> PredictProductPackageDimensionsAndWeightResponse | None:
    """Predict Product Package Dimensions and Weight

     Predicts the package dimensions and weight for one candidate product based on its leaf category. The
    result is generated synchronously and can be used to prepare the package information in a create or
    edit product request. When no prediction is available, `data` is an empty object.

    Args:
        body (PredictProductPackageDimensionsAndWeightRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PredictProductPackageDimensionsAndWeightResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
