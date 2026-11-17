from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.change_post_view_search_video_products_request import ChangePostViewSearchVideoProductsRequest
from ...models.change_post_view_search_video_products_response import ChangePostViewSearchVideoProductsResponse
from typing import cast



def _get_kwargs(
    video_id: str,
    *,
    body: ChangePostViewSearchVideoProductsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202611/search_videos/{video_id}/products".format(video_id=quote(str(video_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChangePostViewSearchVideoProductsResponse | None:
    if response.status_code == 200:
        response_200 = ChangePostViewSearchVideoProductsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChangePostViewSearchVideoProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ChangePostViewSearchVideoProductsRequest,

) -> Response[ChangePostViewSearchVideoProductsResponse]:
    """ Change Post-view Search Video Products

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Binds or unbinds multiple products for one video. Each product ID must
    occur once. The estimated final association count must not exceed 5, consistent with the seller-
    facing
    configuration limit; this is not a per-request operation-count limit. Concurrent changes or failed
    removals can exceed that estimate. Operations may partially succeed and are not transactional.
    Inspect
    each item status and data.errors. Query current associations after an unknown outcome and reconcile
    only the remaining changes; the query does not prove a particular request succeeded. Concurrent
    changes to the same video may overwrite keyword updates. Avoid simultaneous writes for one video.
    Comments are unchanged.

    Args:
        video_id (str):
        body (ChangePostViewSearchVideoProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangePostViewSearchVideoProductsResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ChangePostViewSearchVideoProductsRequest,

) -> ChangePostViewSearchVideoProductsResponse | None:
    """ Change Post-view Search Video Products

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Binds or unbinds multiple products for one video. Each product ID must
    occur once. The estimated final association count must not exceed 5, consistent with the seller-
    facing
    configuration limit; this is not a per-request operation-count limit. Concurrent changes or failed
    removals can exceed that estimate. Operations may partially succeed and are not transactional.
    Inspect
    each item status and data.errors. Query current associations after an unknown outcome and reconcile
    only the remaining changes; the query does not prove a particular request succeeded. Concurrent
    changes to the same video may overwrite keyword updates. Avoid simultaneous writes for one video.
    Comments are unchanged.

    Args:
        video_id (str):
        body (ChangePostViewSearchVideoProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangePostViewSearchVideoProductsResponse
     """


    return sync_detailed(
        video_id=video_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ChangePostViewSearchVideoProductsRequest,

) -> Response[ChangePostViewSearchVideoProductsResponse]:
    """ Change Post-view Search Video Products

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Binds or unbinds multiple products for one video. Each product ID must
    occur once. The estimated final association count must not exceed 5, consistent with the seller-
    facing
    configuration limit; this is not a per-request operation-count limit. Concurrent changes or failed
    removals can exceed that estimate. Operations may partially succeed and are not transactional.
    Inspect
    each item status and data.errors. Query current associations after an unknown outcome and reconcile
    only the remaining changes; the query does not prove a particular request succeeded. Concurrent
    changes to the same video may overwrite keyword updates. Avoid simultaneous writes for one video.
    Comments are unchanged.

    Args:
        video_id (str):
        body (ChangePostViewSearchVideoProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangePostViewSearchVideoProductsResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ChangePostViewSearchVideoProductsRequest,

) -> ChangePostViewSearchVideoProductsResponse | None:
    """ Change Post-view Search Video Products

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Binds or unbinds multiple products for one video. Each product ID must
    occur once. The estimated final association count must not exceed 5, consistent with the seller-
    facing
    configuration limit; this is not a per-request operation-count limit. Concurrent changes or failed
    removals can exceed that estimate. Operations may partially succeed and are not transactional.
    Inspect
    each item status and data.errors. Query current associations after an unknown outcome and reconcile
    only the remaining changes; the query does not prove a particular request succeeded. Concurrent
    changes to the same video may overwrite keyword updates. Avoid simultaneous writes for one video.
    Comments are unchanged.

    Args:
        video_id (str):
        body (ChangePostViewSearchVideoProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangePostViewSearchVideoProductsResponse
     """


    return (await asyncio_detailed(
        video_id=video_id,
client=client,
body=body,

    )).parsed
