from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckProductListingResponseDataFailReason")


@_attrs_define
class CheckProductListingResponseDataFailReason:
    """
    Attributes:
        code (int | Unset): A machine-readable code that represents the failure reason. This is equivalent to the error
            codes shown when creating a product. For the full list of codes, refer to [Create Product > Error
            Code](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a?#Error_Code).
        message (str | Unset): A detailed reason for the failure.
    """

    code: int | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        check_product_listing_response_data_fail_reason = cls(
            code=code,
            message=message,
        )

        check_product_listing_response_data_fail_reason.additional_properties = d
        return check_product_listing_response_data_fail_reason

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
