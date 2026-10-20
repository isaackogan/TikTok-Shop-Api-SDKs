from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.submit_product_via_opportunity_request import SubmitProductViaOpportunityRequest
from ...models.submit_product_via_opportunity_response import SubmitProductViaOpportunityResponse
from typing import cast



def _get_kwargs(
    opportunity_id: str,
    *,
    body: SubmitProductViaOpportunityRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202604/opportunities/{opportunity_id}/submit".format(opportunity_id=quote(str(opportunity_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SubmitProductViaOpportunityResponse | None:
    if response.status_code == 200:
        response_200 = SubmitProductViaOpportunityResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SubmitProductViaOpportunityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitProductViaOpportunityRequest,

) -> Response[SubmitProductViaOpportunityResponse]:
    """ Submit Product via Opportunity

     Submit an existing product as a response to a specific opportunity lead. The product must belong to
    the authorized shop and be in `ACTIVATE` status. It will be linked to the opportunity and enter the
    standard submission review flow.

    If you need a new local product, call the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/create-product-202309) with `save_mode=LISTING`, use
    the returned `data.product_id`, and wait until the product reaches `ACTIVATE`. A product saved with
    `save_mode=AS_DRAFT` is not yet eligible. For a global seller that has not migrated to local
    replication, first call the [Create Global Product
    API](https://partner.tiktokshop.com/docv2/page/6509de61bace3e02b7489cba) to get a
    `global_product_id`, then call the [Publish Global Product
    API](https://partner.tiktokshop.com/docv2/page/publish-global-product-202309). From `data.products`,
    select the local product `id` for the authorized shop and wait until that product reaches `ACTIVATE`
    before submitting it here.

    After submission, use the [Get Submission Records
    API](https://partner.tiktokshop.com/docv2/page/get-submission-records-202604) and filter by
    `opportunity_id` or `product_id` to track the review outcome.

    Args:
        opportunity_id (str):
        body (SubmitProductViaOpportunityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitProductViaOpportunityResponse]
     """


    kwargs = _get_kwargs(
        opportunity_id=opportunity_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitProductViaOpportunityRequest,

) -> SubmitProductViaOpportunityResponse | None:
    """ Submit Product via Opportunity

     Submit an existing product as a response to a specific opportunity lead. The product must belong to
    the authorized shop and be in `ACTIVATE` status. It will be linked to the opportunity and enter the
    standard submission review flow.

    If you need a new local product, call the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/create-product-202309) with `save_mode=LISTING`, use
    the returned `data.product_id`, and wait until the product reaches `ACTIVATE`. A product saved with
    `save_mode=AS_DRAFT` is not yet eligible. For a global seller that has not migrated to local
    replication, first call the [Create Global Product
    API](https://partner.tiktokshop.com/docv2/page/6509de61bace3e02b7489cba) to get a
    `global_product_id`, then call the [Publish Global Product
    API](https://partner.tiktokshop.com/docv2/page/publish-global-product-202309). From `data.products`,
    select the local product `id` for the authorized shop and wait until that product reaches `ACTIVATE`
    before submitting it here.

    After submission, use the [Get Submission Records
    API](https://partner.tiktokshop.com/docv2/page/get-submission-records-202604) and filter by
    `opportunity_id` or `product_id` to track the review outcome.

    Args:
        opportunity_id (str):
        body (SubmitProductViaOpportunityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitProductViaOpportunityResponse
     """


    return sync_detailed(
        opportunity_id=opportunity_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitProductViaOpportunityRequest,

) -> Response[SubmitProductViaOpportunityResponse]:
    """ Submit Product via Opportunity

     Submit an existing product as a response to a specific opportunity lead. The product must belong to
    the authorized shop and be in `ACTIVATE` status. It will be linked to the opportunity and enter the
    standard submission review flow.

    If you need a new local product, call the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/create-product-202309) with `save_mode=LISTING`, use
    the returned `data.product_id`, and wait until the product reaches `ACTIVATE`. A product saved with
    `save_mode=AS_DRAFT` is not yet eligible. For a global seller that has not migrated to local
    replication, first call the [Create Global Product
    API](https://partner.tiktokshop.com/docv2/page/6509de61bace3e02b7489cba) to get a
    `global_product_id`, then call the [Publish Global Product
    API](https://partner.tiktokshop.com/docv2/page/publish-global-product-202309). From `data.products`,
    select the local product `id` for the authorized shop and wait until that product reaches `ACTIVATE`
    before submitting it here.

    After submission, use the [Get Submission Records
    API](https://partner.tiktokshop.com/docv2/page/get-submission-records-202604) and filter by
    `opportunity_id` or `product_id` to track the review outcome.

    Args:
        opportunity_id (str):
        body (SubmitProductViaOpportunityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitProductViaOpportunityResponse]
     """


    kwargs = _get_kwargs(
        opportunity_id=opportunity_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitProductViaOpportunityRequest,

) -> SubmitProductViaOpportunityResponse | None:
    """ Submit Product via Opportunity

     Submit an existing product as a response to a specific opportunity lead. The product must belong to
    the authorized shop and be in `ACTIVATE` status. It will be linked to the opportunity and enter the
    standard submission review flow.

    If you need a new local product, call the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/create-product-202309) with `save_mode=LISTING`, use
    the returned `data.product_id`, and wait until the product reaches `ACTIVATE`. A product saved with
    `save_mode=AS_DRAFT` is not yet eligible. For a global seller that has not migrated to local
    replication, first call the [Create Global Product
    API](https://partner.tiktokshop.com/docv2/page/6509de61bace3e02b7489cba) to get a
    `global_product_id`, then call the [Publish Global Product
    API](https://partner.tiktokshop.com/docv2/page/publish-global-product-202309). From `data.products`,
    select the local product `id` for the authorized shop and wait until that product reaches `ACTIVATE`
    before submitting it here.

    After submission, use the [Get Submission Records
    API](https://partner.tiktokshop.com/docv2/page/get-submission-records-202604) and filter by
    `opportunity_id` or `product_id` to track the review outcome.

    Args:
        opportunity_id (str):
        body (SubmitProductViaOpportunityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitProductViaOpportunityResponse
     """


    return (await asyncio_detailed(
        opportunity_id=opportunity_id,
client=client,
body=body,

    )).parsed
