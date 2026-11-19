from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_ai_report_dimension_options_request import SearchAIReportDimensionOptionsRequest
from ...models.search_ai_report_dimension_options_response import SearchAIReportDimensionOptionsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchAIReportDimensionOptionsRequest,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/analytics/202611/ai_report/dimension_options/search",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchAIReportDimensionOptionsResponse | None:
    if response.status_code == 200:
        response_200 = SearchAIReportDimensionOptionsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchAIReportDimensionOptionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAIReportDimensionOptionsRequest,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> Response[SearchAIReportDimensionOptionsResponse]:
    """ Search AI Report Dimension Options

     Find filter values for a dimension returned by the catalog. Fixed attribute options are returned
    together in configured order; keyword, dates, metrics and pagination do not restrict this finite
    list. For product_id with a nonempty keyword, search product text and return matches by product ID
    descending; for sku_id with a nonempty keyword, look up an exact numeric SKU ID and return at most
    one match. These two lookup modes do not use dates or metric_codes. Other entity searches, including
    product_id or sku_id without a keyword, require start_date and end_date and use metric data. They
    aggregate metric data over the requested date range and sort by the first supplied metric
    descending, with grouping keys ascending to break ties. When metric_codes is omitted or empty, they
    sort by grouping keys ascending. These searches do not group or sort by time buckets. Entity results
    use pagination. Creator searches accept an application-scoped creator.creator_open_id, not keyword;
    an unknown Creator candidate has no selectable identity. main_order_id candidate lookup is
    unsupported.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchAIReportDimensionOptionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchAIReportDimensionOptionsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_token=page_token,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAIReportDimensionOptionsRequest,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> SearchAIReportDimensionOptionsResponse | None:
    """ Search AI Report Dimension Options

     Find filter values for a dimension returned by the catalog. Fixed attribute options are returned
    together in configured order; keyword, dates, metrics and pagination do not restrict this finite
    list. For product_id with a nonempty keyword, search product text and return matches by product ID
    descending; for sku_id with a nonempty keyword, look up an exact numeric SKU ID and return at most
    one match. These two lookup modes do not use dates or metric_codes. Other entity searches, including
    product_id or sku_id without a keyword, require start_date and end_date and use metric data. They
    aggregate metric data over the requested date range and sort by the first supplied metric
    descending, with grouping keys ascending to break ties. When metric_codes is omitted or empty, they
    sort by grouping keys ascending. These searches do not group or sort by time buckets. Entity results
    use pagination. Creator searches accept an application-scoped creator.creator_open_id, not keyword;
    an unknown Creator candidate has no selectable identity. main_order_id candidate lookup is
    unsupported.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchAIReportDimensionOptionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchAIReportDimensionOptionsResponse
     """


    return sync_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAIReportDimensionOptionsRequest,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> Response[SearchAIReportDimensionOptionsResponse]:
    """ Search AI Report Dimension Options

     Find filter values for a dimension returned by the catalog. Fixed attribute options are returned
    together in configured order; keyword, dates, metrics and pagination do not restrict this finite
    list. For product_id with a nonempty keyword, search product text and return matches by product ID
    descending; for sku_id with a nonempty keyword, look up an exact numeric SKU ID and return at most
    one match. These two lookup modes do not use dates or metric_codes. Other entity searches, including
    product_id or sku_id without a keyword, require start_date and end_date and use metric data. They
    aggregate metric data over the requested date range and sort by the first supplied metric
    descending, with grouping keys ascending to break ties. When metric_codes is omitted or empty, they
    sort by grouping keys ascending. These searches do not group or sort by time buckets. Entity results
    use pagination. Creator searches accept an application-scoped creator.creator_open_id, not keyword;
    an unknown Creator candidate has no selectable identity. main_order_id candidate lookup is
    unsupported.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchAIReportDimensionOptionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchAIReportDimensionOptionsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_token=page_token,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAIReportDimensionOptionsRequest,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> SearchAIReportDimensionOptionsResponse | None:
    """ Search AI Report Dimension Options

     Find filter values for a dimension returned by the catalog. Fixed attribute options are returned
    together in configured order; keyword, dates, metrics and pagination do not restrict this finite
    list. For product_id with a nonempty keyword, search product text and return matches by product ID
    descending; for sku_id with a nonempty keyword, look up an exact numeric SKU ID and return at most
    one match. These two lookup modes do not use dates or metric_codes. Other entity searches, including
    product_id or sku_id without a keyword, require start_date and end_date and use metric data. They
    aggregate metric data over the requested date range and sort by the first supplied metric
    descending, with grouping keys ascending to break ties. When metric_codes is omitted or empty, they
    sort by grouping keys ascending. These searches do not group or sort by time buckets. Entity results
    use pagination. Creator searches accept an application-scoped creator.creator_open_id, not keyword;
    an unknown Creator candidate has no selectable identity. main_order_id candidate lookup is
    unsupported.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchAIReportDimensionOptionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchAIReportDimensionOptionsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,

    )).parsed
