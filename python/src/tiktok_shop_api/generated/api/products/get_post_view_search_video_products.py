from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_post_view_search_video_products_response import GetPostViewSearchVideoProductsResponse
from typing import cast



def _get_kwargs(
    video_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202611/search_videos/{video_id}/products".format(video_id=quote(str(video_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetPostViewSearchVideoProductsResponse | None:
    if response.status_code == 200:
        response_200 = GetPostViewSearchVideoProductsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetPostViewSearchVideoProductsResponse]:
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

) -> Response[GetPostViewSearchVideoProductsResponse]:
    """ Get Post-view Search Video Products

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Returns
    the current product associations supplied by the relation service, without truncating the response
    to
    five. An empty array means none are associated. Product IDs identify associations, not product
    details
    or a guarantee of exposure.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPostViewSearchVideoProductsResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetPostViewSearchVideoProductsResponse | None:
    """ Get Post-view Search Video Products

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Returns
    the current product associations supplied by the relation service, without truncating the response
    to
    five. An empty array means none are associated. Product IDs identify associations, not product
    details
    or a guarantee of exposure.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPostViewSearchVideoProductsResponse
     """


    return sync_detailed(
        video_id=video_id,
client=client,

    ).parsed

async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetPostViewSearchVideoProductsResponse]:
    """ Get Post-view Search Video Products

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Returns
    the current product associations supplied by the relation service, without truncating the response
    to
    five. An empty array means none are associated. Product IDs identify associations, not product
    details
    or a guarantee of exposure.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPostViewSearchVideoProductsResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetPostViewSearchVideoProductsResponse | None:
    """ Get Post-view Search Video Products

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Returns
    the current product associations supplied by the relation service, without truncating the response
    to
    five. An empty array means none are associated. Product IDs identify associations, not product
    details
    or a guarantee of exposure.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPostViewSearchVideoProductsResponse
     """


    return (await asyncio_detailed(
        video_id=video_id,
client=client,

    )).parsed
