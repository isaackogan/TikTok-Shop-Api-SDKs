from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_fbtmcf_order_request_consignee_address import CreateFBTMCFOrderRequestConsigneeAddress


T = TypeVar("T", bound="CreateFBTMCFOrderRequestConsignee")


@_attrs_define
class CreateFBTMCFOrderRequestConsignee:
    """
    Attributes:
        name (str): The consignee name. Must not exceed 128 UTF-8 bytes.
        phone_number (str): The phone number of consignee
        email (str): The email of consignee
        address (CreateFBTMCFOrderRequestConsigneeAddress):
    """

    name: str
    phone_number: str
    email: str
    address: CreateFBTMCFOrderRequestConsigneeAddress
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        phone_number = self.phone_number

        email = self.email

        address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "phone_number": phone_number,
                "email": email,
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_fbtmcf_order_request_consignee_address import (
            CreateFBTMCFOrderRequestConsigneeAddress,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        phone_number = d.pop("phone_number")

        email = d.pop("email")

        address = CreateFBTMCFOrderRequestConsigneeAddress.from_dict(d.pop("address"))

        create_fbtmcf_order_request_consignee = cls(
            name=name,
            phone_number=phone_number,
            email=email,
            address=address,
        )

        create_fbtmcf_order_request_consignee.additional_properties = d
        return create_fbtmcf_order_request_consignee

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
