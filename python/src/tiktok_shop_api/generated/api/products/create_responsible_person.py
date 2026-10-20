from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_responsible_person_request import CreateResponsiblePersonRequest
from ...models.create_responsible_person_response import CreateResponsiblePersonResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreateResponsiblePersonRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202409/compliance/responsible_persons",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateResponsiblePersonResponse | None:
    if response.status_code == 200:
        response_200 = CreateResponsiblePersonResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateResponsiblePersonResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateResponsiblePersonRequest,

) -> Response[CreateResponsiblePersonResponse]:
    """ Create Responsible Person

     Add a new EU responsible person who ensures a seller's products comply with EU regulations. The
    provided information will be automatically translated into all EU languages supported by TikTok
    Shop.
    - Use the [Search Responsible Persons API](67066a55f17b7d02f95d2fb1) to obtain the translations.
    - Use the [Partial Edit Responsible Person API](67066a5587019802fdce19b3) to edit the translations,
    if necessary.
    - When creating a product, pass the returned `responsible_person_id` to associate the product with
    the responsible person.

    Target seller: Local sellers operating in EU countries

    Args:
        body (CreateResponsiblePersonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateResponsiblePersonResponse]
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
    body: CreateResponsiblePersonRequest,

) -> CreateResponsiblePersonResponse | None:
    """ Create Responsible Person

     Add a new EU responsible person who ensures a seller's products comply with EU regulations. The
    provided information will be automatically translated into all EU languages supported by TikTok
    Shop.
    - Use the [Search Responsible Persons API](67066a55f17b7d02f95d2fb1) to obtain the translations.
    - Use the [Partial Edit Responsible Person API](67066a5587019802fdce19b3) to edit the translations,
    if necessary.
    - When creating a product, pass the returned `responsible_person_id` to associate the product with
    the responsible person.

    Target seller: Local sellers operating in EU countries

    Args:
        body (CreateResponsiblePersonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateResponsiblePersonResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateResponsiblePersonRequest,

) -> Response[CreateResponsiblePersonResponse]:
    """ Create Responsible Person

     Add a new EU responsible person who ensures a seller's products comply with EU regulations. The
    provided information will be automatically translated into all EU languages supported by TikTok
    Shop.
    - Use the [Search Responsible Persons API](67066a55f17b7d02f95d2fb1) to obtain the translations.
    - Use the [Partial Edit Responsible Person API](67066a5587019802fdce19b3) to edit the translations,
    if necessary.
    - When creating a product, pass the returned `responsible_person_id` to associate the product with
    the responsible person.

    Target seller: Local sellers operating in EU countries

    Args:
        body (CreateResponsiblePersonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateResponsiblePersonResponse]
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
    body: CreateResponsiblePersonRequest,

) -> CreateResponsiblePersonResponse | None:
    """ Create Responsible Person

     Add a new EU responsible person who ensures a seller's products comply with EU regulations. The
    provided information will be automatically translated into all EU languages supported by TikTok
    Shop.
    - Use the [Search Responsible Persons API](67066a55f17b7d02f95d2fb1) to obtain the translations.
    - Use the [Partial Edit Responsible Person API](67066a5587019802fdce19b3) to edit the translations,
    if necessary.
    - When creating a product, pass the returned `responsible_person_id` to associate the product with
    the responsible person.

    Target seller: Local sellers operating in EU countries

    Args:
        body (CreateResponsiblePersonRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateResponsiblePersonResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
