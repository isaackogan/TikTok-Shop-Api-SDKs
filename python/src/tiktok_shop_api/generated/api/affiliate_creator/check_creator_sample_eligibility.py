from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.check_creator_sample_eligibility_response import CheckCreatorSampleEligibilityResponse
from typing import cast



def _get_kwargs(
    *,
    product_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["product_id"] = product_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_creator/202412/samples/labels",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CheckCreatorSampleEligibilityResponse | None:
    if response.status_code == 200:
        response_200 = CheckCreatorSampleEligibilityResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CheckCreatorSampleEligibilityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,

) -> Response[CheckCreatorSampleEligibilityResponse]:
    """ Check Creator Sample Eligibility

     Check if a creator can apply for a sample of a specific product.

    Args:
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckCreatorSampleEligibilityResponse]
     """


    kwargs = _get_kwargs(
        product_id=product_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,

) -> CheckCreatorSampleEligibilityResponse | None:
    """ Check Creator Sample Eligibility

     Check if a creator can apply for a sample of a specific product.

    Args:
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckCreatorSampleEligibilityResponse
     """


    return sync_detailed(
        client=client,
product_id=product_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,

) -> Response[CheckCreatorSampleEligibilityResponse]:
    """ Check Creator Sample Eligibility

     Check if a creator can apply for a sample of a specific product.

    Args:
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckCreatorSampleEligibilityResponse]
     """


    kwargs = _get_kwargs(
        product_id=product_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,

) -> CheckCreatorSampleEligibilityResponse | None:
    """ Check Creator Sample Eligibility

     Check if a creator can apply for a sample of a specific product.

    Args:
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckCreatorSampleEligibilityResponse
     """


    return (await asyncio_detailed(
        client=client,
product_id=product_id,

    )).parsed
