from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.validate_ai_report_query_configuration_request import ValidateAIReportQueryConfigurationRequest
from ...models.validate_ai_report_query_configuration_response import ValidateAIReportQueryConfigurationResponse
from typing import cast



def _get_kwargs(
    *,
    body: ValidateAIReportQueryConfigurationRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/analytics/202611/ai_report/query_config/validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ValidateAIReportQueryConfigurationResponse | None:
    if response.status_code == 200:
        response_200 = ValidateAIReportQueryConfigurationResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ValidateAIReportQueryConfigurationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ValidateAIReportQueryConfigurationRequest,

) -> Response[ValidateAIReportQueryConfigurationResponse]:
    """ Validate AI Report Query Configuration

     Validate the query configuration without fetching report rows. Invalid request parameters, such as
    malformed dates or unknown catalog codes, return a nonzero response code. When request parameters
    are accepted but the metric, dimension, filter or detail-field combination is rejected, the response
    has code=0 and data.is_valid=false with reason_code and reason_message. A valid combination returns
    data.is_valid=true and omits reason_code and reason_message. Only one rejection is returned; this
    API does not list every conflict. Validation does not reserve a data snapshot or guarantee that a
    later query will succeed if configuration or data availability changes. Sorting defaults match Data
    Query.

    Args:
        body (ValidateAIReportQueryConfigurationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidateAIReportQueryConfigurationResponse]
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
    body: ValidateAIReportQueryConfigurationRequest,

) -> ValidateAIReportQueryConfigurationResponse | None:
    """ Validate AI Report Query Configuration

     Validate the query configuration without fetching report rows. Invalid request parameters, such as
    malformed dates or unknown catalog codes, return a nonzero response code. When request parameters
    are accepted but the metric, dimension, filter or detail-field combination is rejected, the response
    has code=0 and data.is_valid=false with reason_code and reason_message. A valid combination returns
    data.is_valid=true and omits reason_code and reason_message. Only one rejection is returned; this
    API does not list every conflict. Validation does not reserve a data snapshot or guarantee that a
    later query will succeed if configuration or data availability changes. Sorting defaults match Data
    Query.

    Args:
        body (ValidateAIReportQueryConfigurationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidateAIReportQueryConfigurationResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ValidateAIReportQueryConfigurationRequest,

) -> Response[ValidateAIReportQueryConfigurationResponse]:
    """ Validate AI Report Query Configuration

     Validate the query configuration without fetching report rows. Invalid request parameters, such as
    malformed dates or unknown catalog codes, return a nonzero response code. When request parameters
    are accepted but the metric, dimension, filter or detail-field combination is rejected, the response
    has code=0 and data.is_valid=false with reason_code and reason_message. A valid combination returns
    data.is_valid=true and omits reason_code and reason_message. Only one rejection is returned; this
    API does not list every conflict. Validation does not reserve a data snapshot or guarantee that a
    later query will succeed if configuration or data availability changes. Sorting defaults match Data
    Query.

    Args:
        body (ValidateAIReportQueryConfigurationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidateAIReportQueryConfigurationResponse]
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
    body: ValidateAIReportQueryConfigurationRequest,

) -> ValidateAIReportQueryConfigurationResponse | None:
    """ Validate AI Report Query Configuration

     Validate the query configuration without fetching report rows. Invalid request parameters, such as
    malformed dates or unknown catalog codes, return a nonzero response code. When request parameters
    are accepted but the metric, dimension, filter or detail-field combination is rejected, the response
    has code=0 and data.is_valid=false with reason_code and reason_message. A valid combination returns
    data.is_valid=true and omits reason_code and reason_message. Only one rejection is returned; this
    API does not list every conflict. Validation does not reserve a data snapshot or guarantee that a
    later query will succeed if configuration or data availability changes. Sorting defaults match Data
    Query.

    Args:
        body (ValidateAIReportQueryConfigurationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidateAIReportQueryConfigurationResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
