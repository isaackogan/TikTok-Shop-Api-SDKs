from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.partial_edit_responsible_person_request import PartialEditResponsiblePersonRequest
from ...models.partial_edit_responsible_person_response import PartialEditResponsiblePersonResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    responsible_person_id: str,
    *,
    body: PartialEditResponsiblePersonRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202409/compliance/responsible_persons/{responsible_person_id}/partial_edit".format(responsible_person_id=quote(str(responsible_person_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PartialEditResponsiblePersonResponse | None:
    if response.status_code == 200:
        response_200 = PartialEditResponsiblePersonResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PartialEditResponsiblePersonResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    responsible_person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditResponsiblePersonRequest | Unset = UNSET,

) -> Response[PartialEditResponsiblePersonResponse]:
    """ Partial Edit Responsible Person

     Edit the details of an EU responsible person in the EU languages supported by TikTok Shop. Include
    the locale code to edit the responsible person's information in a particular language.
    Target seller: Local sellers operating in EU countries
    **Note**:
    - Updates are handled per top-level property, so all non-empty fields within an updated object must
    be supplied to prevent overwriting with blanks.
    - For top-level properties (e.g. `name`, `email`) that are not nested in an object, you can update
    them individually. Omitting these properties in the request will leave them unchanged.
    - If you need to edit any nested property within an object, you must provide values for all nested
    properties of that object. Any omitted nested properties will be overwritten with blanks. For
    example, if you want to update `phone_number.local_number`, you must also include the `country_code`
    property to avoid data loss for that property.

    Args:
        responsible_person_id (str):
        body (PartialEditResponsiblePersonRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartialEditResponsiblePersonResponse]
     """


    kwargs = _get_kwargs(
        responsible_person_id=responsible_person_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    responsible_person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditResponsiblePersonRequest | Unset = UNSET,

) -> PartialEditResponsiblePersonResponse | None:
    """ Partial Edit Responsible Person

     Edit the details of an EU responsible person in the EU languages supported by TikTok Shop. Include
    the locale code to edit the responsible person's information in a particular language.
    Target seller: Local sellers operating in EU countries
    **Note**:
    - Updates are handled per top-level property, so all non-empty fields within an updated object must
    be supplied to prevent overwriting with blanks.
    - For top-level properties (e.g. `name`, `email`) that are not nested in an object, you can update
    them individually. Omitting these properties in the request will leave them unchanged.
    - If you need to edit any nested property within an object, you must provide values for all nested
    properties of that object. Any omitted nested properties will be overwritten with blanks. For
    example, if you want to update `phone_number.local_number`, you must also include the `country_code`
    property to avoid data loss for that property.

    Args:
        responsible_person_id (str):
        body (PartialEditResponsiblePersonRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartialEditResponsiblePersonResponse
     """


    return sync_detailed(
        responsible_person_id=responsible_person_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    responsible_person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditResponsiblePersonRequest | Unset = UNSET,

) -> Response[PartialEditResponsiblePersonResponse]:
    """ Partial Edit Responsible Person

     Edit the details of an EU responsible person in the EU languages supported by TikTok Shop. Include
    the locale code to edit the responsible person's information in a particular language.
    Target seller: Local sellers operating in EU countries
    **Note**:
    - Updates are handled per top-level property, so all non-empty fields within an updated object must
    be supplied to prevent overwriting with blanks.
    - For top-level properties (e.g. `name`, `email`) that are not nested in an object, you can update
    them individually. Omitting these properties in the request will leave them unchanged.
    - If you need to edit any nested property within an object, you must provide values for all nested
    properties of that object. Any omitted nested properties will be overwritten with blanks. For
    example, if you want to update `phone_number.local_number`, you must also include the `country_code`
    property to avoid data loss for that property.

    Args:
        responsible_person_id (str):
        body (PartialEditResponsiblePersonRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartialEditResponsiblePersonResponse]
     """


    kwargs = _get_kwargs(
        responsible_person_id=responsible_person_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    responsible_person_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditResponsiblePersonRequest | Unset = UNSET,

) -> PartialEditResponsiblePersonResponse | None:
    """ Partial Edit Responsible Person

     Edit the details of an EU responsible person in the EU languages supported by TikTok Shop. Include
    the locale code to edit the responsible person's information in a particular language.
    Target seller: Local sellers operating in EU countries
    **Note**:
    - Updates are handled per top-level property, so all non-empty fields within an updated object must
    be supplied to prevent overwriting with blanks.
    - For top-level properties (e.g. `name`, `email`) that are not nested in an object, you can update
    them individually. Omitting these properties in the request will leave them unchanged.
    - If you need to edit any nested property within an object, you must provide values for all nested
    properties of that object. Any omitted nested properties will be overwritten with blanks. For
    example, if you want to update `phone_number.local_number`, you must also include the `country_code`
    property to avoid data loss for that property.

    Args:
        responsible_person_id (str):
        body (PartialEditResponsiblePersonRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartialEditResponsiblePersonResponse
     """


    return (await asyncio_detailed(
        responsible_person_id=responsible_person_id,
client=client,
body=body,

    )).parsed
