from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.print_inbound_order_labels_request import PrintInboundOrderLabelsRequest
from ...models.print_inbound_order_labels_response import PrintInboundOrderLabelsResponse
from typing import cast



def _get_kwargs(
    *,
    body: PrintInboundOrderLabelsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202602/inbound_orders/label_print",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PrintInboundOrderLabelsResponse | None:
    if response.status_code == 200:
        response_200 = PrintInboundOrderLabelsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PrintInboundOrderLabelsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PrintInboundOrderLabelsRequest,

) -> Response[PrintInboundOrderLabelsResponse]:
    """ Print Inbound Order Labels

     This API generates label files for an inbound order using an **asynchronous Long-Running Operation
    (LRO)**. The inbound order must be shipped or in a later eligible status and must not be canceled.

    **Format applicability**
    * `carton_label_format` controls the carton or pallet label layout only when `print_items` includes
    `CARTON_PALLET_LABEL`.
    * `barcode_format` controls the goods-barcode label layout only when `print_items` includes
    `FBT_BARCODE`.

    The selected `print_items` and both resolved format values are part of the print task identifier, so
    keep the same selections in every polling request.

    **Workflow**
    1. **Initiate.** Send a request with the child inbound `order_id` and the desired `print_items`. The
    API returns `PROCESSING` while the label file is being generated; a completed task for the same
    request values may return `SUCCESS` immediately.
    2. **Poll.** If `task_status` is `PROCESSING`, repeat the request with the same `order_id`,
    `print_items`, `carton_label_format`, and `barcode_format` values. Poll every 3–5 seconds.
    3. **Complete.** When `task_status` is `SUCCESS`, `download_url` contains the generated ZIP file.

    Args:
        body (PrintInboundOrderLabelsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrintInboundOrderLabelsResponse]
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
    body: PrintInboundOrderLabelsRequest,

) -> PrintInboundOrderLabelsResponse | None:
    """ Print Inbound Order Labels

     This API generates label files for an inbound order using an **asynchronous Long-Running Operation
    (LRO)**. The inbound order must be shipped or in a later eligible status and must not be canceled.

    **Format applicability**
    * `carton_label_format` controls the carton or pallet label layout only when `print_items` includes
    `CARTON_PALLET_LABEL`.
    * `barcode_format` controls the goods-barcode label layout only when `print_items` includes
    `FBT_BARCODE`.

    The selected `print_items` and both resolved format values are part of the print task identifier, so
    keep the same selections in every polling request.

    **Workflow**
    1. **Initiate.** Send a request with the child inbound `order_id` and the desired `print_items`. The
    API returns `PROCESSING` while the label file is being generated; a completed task for the same
    request values may return `SUCCESS` immediately.
    2. **Poll.** If `task_status` is `PROCESSING`, repeat the request with the same `order_id`,
    `print_items`, `carton_label_format`, and `barcode_format` values. Poll every 3–5 seconds.
    3. **Complete.** When `task_status` is `SUCCESS`, `download_url` contains the generated ZIP file.

    Args:
        body (PrintInboundOrderLabelsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PrintInboundOrderLabelsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PrintInboundOrderLabelsRequest,

) -> Response[PrintInboundOrderLabelsResponse]:
    """ Print Inbound Order Labels

     This API generates label files for an inbound order using an **asynchronous Long-Running Operation
    (LRO)**. The inbound order must be shipped or in a later eligible status and must not be canceled.

    **Format applicability**
    * `carton_label_format` controls the carton or pallet label layout only when `print_items` includes
    `CARTON_PALLET_LABEL`.
    * `barcode_format` controls the goods-barcode label layout only when `print_items` includes
    `FBT_BARCODE`.

    The selected `print_items` and both resolved format values are part of the print task identifier, so
    keep the same selections in every polling request.

    **Workflow**
    1. **Initiate.** Send a request with the child inbound `order_id` and the desired `print_items`. The
    API returns `PROCESSING` while the label file is being generated; a completed task for the same
    request values may return `SUCCESS` immediately.
    2. **Poll.** If `task_status` is `PROCESSING`, repeat the request with the same `order_id`,
    `print_items`, `carton_label_format`, and `barcode_format` values. Poll every 3–5 seconds.
    3. **Complete.** When `task_status` is `SUCCESS`, `download_url` contains the generated ZIP file.

    Args:
        body (PrintInboundOrderLabelsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrintInboundOrderLabelsResponse]
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
    body: PrintInboundOrderLabelsRequest,

) -> PrintInboundOrderLabelsResponse | None:
    """ Print Inbound Order Labels

     This API generates label files for an inbound order using an **asynchronous Long-Running Operation
    (LRO)**. The inbound order must be shipped or in a later eligible status and must not be canceled.

    **Format applicability**
    * `carton_label_format` controls the carton or pallet label layout only when `print_items` includes
    `CARTON_PALLET_LABEL`.
    * `barcode_format` controls the goods-barcode label layout only when `print_items` includes
    `FBT_BARCODE`.

    The selected `print_items` and both resolved format values are part of the print task identifier, so
    keep the same selections in every polling request.

    **Workflow**
    1. **Initiate.** Send a request with the child inbound `order_id` and the desired `print_items`. The
    API returns `PROCESSING` while the label file is being generated; a completed task for the same
    request values may return `SUCCESS` immediately.
    2. **Poll.** If `task_status` is `PROCESSING`, repeat the request with the same `order_id`,
    `print_items`, `carton_label_format`, and `barcode_format` values. Poll every 3–5 seconds.
    3. **Complete.** When `task_status` is `SUCCESS`, `download_url` contains the generated ZIP file.

    Args:
        body (PrintInboundOrderLabelsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PrintInboundOrderLabelsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
