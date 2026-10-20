from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.optimize_images_request import OptimizeImagesRequest
from ...models.optimize_images_response import OptimizeImagesResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: OptimizeImagesRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202404/images/optimize",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OptimizeImagesResponse | None:
    if response.status_code == 200:
        response_200 = OptimizeImagesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OptimizeImagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OptimizeImagesRequest | Unset = UNSET,

) -> Response[OptimizeImagesResponse]:
    """ Optimize Images

     Optimize images used in your TikTok Shop by changing the background to white.
    This is especially useful for images displayed in the product image gallery as it enhances product
    visibility.
    **Note**:
    - The images to be optimized must first be uploaded to TikTok Shop through the [Upload Product Image
    API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22). You will not be able to
    optimize any images that are not hosted by TikTok Shop.
    - Images that were previously optimized will not be processed again.
    - The optimization is processed asynchronously and typically completes within a few seconds. If no
    stored optimization result exists, `optimize_status` is `PROCESSING`, indicating that optimization
    is underway. If a stored final result already exists, the API may return it immediately. When
    `optimize_status` is `PROCESSING`, call the API again after a few seconds to get the final
    optimization status.

    Args:
        body (OptimizeImagesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OptimizeImagesResponse]
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
    body: OptimizeImagesRequest | Unset = UNSET,

) -> OptimizeImagesResponse | None:
    """ Optimize Images

     Optimize images used in your TikTok Shop by changing the background to white.
    This is especially useful for images displayed in the product image gallery as it enhances product
    visibility.
    **Note**:
    - The images to be optimized must first be uploaded to TikTok Shop through the [Upload Product Image
    API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22). You will not be able to
    optimize any images that are not hosted by TikTok Shop.
    - Images that were previously optimized will not be processed again.
    - The optimization is processed asynchronously and typically completes within a few seconds. If no
    stored optimization result exists, `optimize_status` is `PROCESSING`, indicating that optimization
    is underway. If a stored final result already exists, the API may return it immediately. When
    `optimize_status` is `PROCESSING`, call the API again after a few seconds to get the final
    optimization status.

    Args:
        body (OptimizeImagesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OptimizeImagesResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OptimizeImagesRequest | Unset = UNSET,

) -> Response[OptimizeImagesResponse]:
    """ Optimize Images

     Optimize images used in your TikTok Shop by changing the background to white.
    This is especially useful for images displayed in the product image gallery as it enhances product
    visibility.
    **Note**:
    - The images to be optimized must first be uploaded to TikTok Shop through the [Upload Product Image
    API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22). You will not be able to
    optimize any images that are not hosted by TikTok Shop.
    - Images that were previously optimized will not be processed again.
    - The optimization is processed asynchronously and typically completes within a few seconds. If no
    stored optimization result exists, `optimize_status` is `PROCESSING`, indicating that optimization
    is underway. If a stored final result already exists, the API may return it immediately. When
    `optimize_status` is `PROCESSING`, call the API again after a few seconds to get the final
    optimization status.

    Args:
        body (OptimizeImagesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OptimizeImagesResponse]
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
    body: OptimizeImagesRequest | Unset = UNSET,

) -> OptimizeImagesResponse | None:
    """ Optimize Images

     Optimize images used in your TikTok Shop by changing the background to white.
    This is especially useful for images displayed in the product image gallery as it enhances product
    visibility.
    **Note**:
    - The images to be optimized must first be uploaded to TikTok Shop through the [Upload Product Image
    API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22). You will not be able to
    optimize any images that are not hosted by TikTok Shop.
    - Images that were previously optimized will not be processed again.
    - The optimization is processed asynchronously and typically completes within a few seconds. If no
    stored optimization result exists, `optimize_status` is `PROCESSING`, indicating that optimization
    is underway. If a stored final result already exists, the API may return it immediately. When
    `optimize_status` is `PROCESSING`, call the API again after a few seconds to get the final
    optimization status.

    Args:
        body (OptimizeImagesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OptimizeImagesResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
