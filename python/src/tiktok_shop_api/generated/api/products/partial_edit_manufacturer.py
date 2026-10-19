from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.partial_edit_manufacturer_request import PartialEditManufacturerRequest
from ...models.partial_edit_manufacturer_response import PartialEditManufacturerResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    manufacturer_id: str,
    *,
    body: PartialEditManufacturerRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202409/compliance/manufacturers/{manufacturer_id}/partial_edit".format(
            manufacturer_id=quote(str(manufacturer_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PartialEditManufacturerResponse | None:
    if response.status_code == 200:
        response_200 = PartialEditManufacturerResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PartialEditManufacturerResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    manufacturer_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditManufacturerRequest | Unset = UNSET,
) -> Response[PartialEditManufacturerResponse]:
    """Partial Edit Manufacturer

     Edit the details of a manufacturer in the EU languages supported by TikTok Shop. Include the locale
    code to edit the manufacturer's information in a particular language.
    Target seller: Local sellers operating in EU countries
    **Note**:
    - The manufacturer name, registered trade name, email address, local phone number, and the address
    field must not contain Chinese characters.
    - Updates are handled per top-level property, so all non-empty fields within an updated object must
    be supplied to prevent overwriting with blanks.
    - For top-level properties (e.g. `name`, `email`) that are not nested in an object, you can update
    them individually. Omitting these properties in the request will leave them unchanged.
    - If you need to edit any nested property within an object, you must provide values for all nested
    properties of that object. Any omitted nested properties will be overwritten with blanks. For an
    available phone number, provide `availability=AVAILABLE`, `country_code`, and `local_number`
    together. If `availability=UNAVAILABLE` is supported for the seller, provide
    `availability=UNAVAILABLE` and omit `country_code` and `local_number`; otherwise, a valid phone
    number is still required.

    Args:
        manufacturer_id (str):
        body (PartialEditManufacturerRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartialEditManufacturerResponse]
    """

    kwargs = _get_kwargs(
        manufacturer_id=manufacturer_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    manufacturer_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditManufacturerRequest | Unset = UNSET,
) -> PartialEditManufacturerResponse | None:
    """Partial Edit Manufacturer

     Edit the details of a manufacturer in the EU languages supported by TikTok Shop. Include the locale
    code to edit the manufacturer's information in a particular language.
    Target seller: Local sellers operating in EU countries
    **Note**:
    - The manufacturer name, registered trade name, email address, local phone number, and the address
    field must not contain Chinese characters.
    - Updates are handled per top-level property, so all non-empty fields within an updated object must
    be supplied to prevent overwriting with blanks.
    - For top-level properties (e.g. `name`, `email`) that are not nested in an object, you can update
    them individually. Omitting these properties in the request will leave them unchanged.
    - If you need to edit any nested property within an object, you must provide values for all nested
    properties of that object. Any omitted nested properties will be overwritten with blanks. For an
    available phone number, provide `availability=AVAILABLE`, `country_code`, and `local_number`
    together. If `availability=UNAVAILABLE` is supported for the seller, provide
    `availability=UNAVAILABLE` and omit `country_code` and `local_number`; otherwise, a valid phone
    number is still required.

    Args:
        manufacturer_id (str):
        body (PartialEditManufacturerRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartialEditManufacturerResponse
    """

    return sync_detailed(
        manufacturer_id=manufacturer_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    manufacturer_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditManufacturerRequest | Unset = UNSET,
) -> Response[PartialEditManufacturerResponse]:
    """Partial Edit Manufacturer

     Edit the details of a manufacturer in the EU languages supported by TikTok Shop. Include the locale
    code to edit the manufacturer's information in a particular language.
    Target seller: Local sellers operating in EU countries
    **Note**:
    - The manufacturer name, registered trade name, email address, local phone number, and the address
    field must not contain Chinese characters.
    - Updates are handled per top-level property, so all non-empty fields within an updated object must
    be supplied to prevent overwriting with blanks.
    - For top-level properties (e.g. `name`, `email`) that are not nested in an object, you can update
    them individually. Omitting these properties in the request will leave them unchanged.
    - If you need to edit any nested property within an object, you must provide values for all nested
    properties of that object. Any omitted nested properties will be overwritten with blanks. For an
    available phone number, provide `availability=AVAILABLE`, `country_code`, and `local_number`
    together. If `availability=UNAVAILABLE` is supported for the seller, provide
    `availability=UNAVAILABLE` and omit `country_code` and `local_number`; otherwise, a valid phone
    number is still required.

    Args:
        manufacturer_id (str):
        body (PartialEditManufacturerRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartialEditManufacturerResponse]
    """

    kwargs = _get_kwargs(
        manufacturer_id=manufacturer_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    manufacturer_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditManufacturerRequest | Unset = UNSET,
) -> PartialEditManufacturerResponse | None:
    """Partial Edit Manufacturer

     Edit the details of a manufacturer in the EU languages supported by TikTok Shop. Include the locale
    code to edit the manufacturer's information in a particular language.
    Target seller: Local sellers operating in EU countries
    **Note**:
    - The manufacturer name, registered trade name, email address, local phone number, and the address
    field must not contain Chinese characters.
    - Updates are handled per top-level property, so all non-empty fields within an updated object must
    be supplied to prevent overwriting with blanks.
    - For top-level properties (e.g. `name`, `email`) that are not nested in an object, you can update
    them individually. Omitting these properties in the request will leave them unchanged.
    - If you need to edit any nested property within an object, you must provide values for all nested
    properties of that object. Any omitted nested properties will be overwritten with blanks. For an
    available phone number, provide `availability=AVAILABLE`, `country_code`, and `local_number`
    together. If `availability=UNAVAILABLE` is supported for the seller, provide
    `availability=UNAVAILABLE` and omit `country_code` and `local_number`; otherwise, a valid phone
    number is still required.

    Args:
        manufacturer_id (str):
        body (PartialEditManufacturerRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartialEditManufacturerResponse
    """

    return (
        await asyncio_detailed(
            manufacturer_id=manufacturer_id,
            client=client,
            body=body,
        )
    ).parsed
