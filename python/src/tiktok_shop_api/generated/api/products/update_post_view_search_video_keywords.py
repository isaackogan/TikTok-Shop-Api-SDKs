from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_post_view_search_video_keywords_request import UpdatePostViewSearchVideoKeywordsRequest
from ...models.update_post_view_search_video_keywords_response import UpdatePostViewSearchVideoKeywordsResponse
from typing import cast



def _get_kwargs(
    video_id: str,
    *,
    body: UpdatePostViewSearchVideoKeywordsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/product/202611/search_videos/{video_id}/keywords".format(video_id=quote(str(video_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdatePostViewSearchVideoKeywordsResponse | None:
    if response.status_code == 200:
        response_200 = UpdatePostViewSearchVideoKeywordsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdatePostViewSearchVideoKeywordsResponse]:
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
    body: UpdatePostViewSearchVideoKeywordsRequest,

) -> Response[UpdatePostViewSearchVideoKeywordsResponse]:
    """ Update Post-view Search Video Keywords

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Replaces the complete keyword set with at most 5 entries; an empty array
    clears it. Products and comments are unchanged. Concurrent updates can overwrite each other. After
    an
    unknown outcome, query the current keywords and reconcile the complete desired set before deciding
    whether to submit again; the query does not identify which request wrote the state.

    Args:
        video_id (str):
        body (UpdatePostViewSearchVideoKeywordsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePostViewSearchVideoKeywordsResponse]
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
    body: UpdatePostViewSearchVideoKeywordsRequest,

) -> UpdatePostViewSearchVideoKeywordsResponse | None:
    """ Update Post-view Search Video Keywords

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Replaces the complete keyword set with at most 5 entries; an empty array
    clears it. Products and comments are unchanged. Concurrent updates can overwrite each other. After
    an
    unknown outcome, query the current keywords and reconcile the complete desired set before deciding
    whether to submit again; the query does not identify which request wrote the state.

    Args:
        video_id (str):
        body (UpdatePostViewSearchVideoKeywordsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePostViewSearchVideoKeywordsResponse
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
    body: UpdatePostViewSearchVideoKeywordsRequest,

) -> Response[UpdatePostViewSearchVideoKeywordsResponse]:
    """ Update Post-view Search Video Keywords

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Replaces the complete keyword set with at most 5 entries; an empty array
    clears it. Products and comments are unchanged. Concurrent updates can overwrite each other. After
    an
    unknown outcome, query the current keywords and reconcile the complete desired set before deciding
    whether to submit again; the query does not identify which request wrote the state.

    Args:
        video_id (str):
        body (UpdatePostViewSearchVideoKeywordsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePostViewSearchVideoKeywordsResponse]
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
    body: UpdatePostViewSearchVideoKeywordsRequest,

) -> UpdatePostViewSearchVideoKeywordsResponse | None:
    """ Update Post-view Search Video Keywords

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Replaces the complete keyword set with at most 5 entries; an empty array
    clears it. Products and comments are unchanged. Concurrent updates can overwrite each other. After
    an
    unknown outcome, query the current keywords and reconcile the complete desired set before deciding
    whether to submit again; the query does not identify which request wrote the state.

    Args:
        video_id (str):
        body (UpdatePostViewSearchVideoKeywordsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePostViewSearchVideoKeywordsResponse
     """


    return (await asyncio_detailed(
        video_id=video_id,
client=client,
body=body,

    )).parsed
