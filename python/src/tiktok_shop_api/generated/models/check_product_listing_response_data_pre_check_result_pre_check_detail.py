from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CheckProductListingResponseDataPreCheckResultPreCheckDetail")



@_attrs_define
class CheckProductListingResponseDataPreCheckResultPreCheckDetail:
    """ 
        Attributes:
            short_reason (str | Unset): Reason for streamlining: Simple problem description of product verification results
            long_reason (str | Unset): Detailed reason: Detailed problem description of product verification results
            related_fields (list[str] | Unset): Problem Module: From which module does the problem originate, e.g.,
                PRE_CHECK_FIELD_TITLE, PRE_CHECK_FIELD_IMAGES
     """

    short_reason: str | Unset = UNSET
    long_reason: str | Unset = UNSET
    related_fields: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        short_reason = self.short_reason

        long_reason = self.long_reason

        related_fields: list[str] | Unset = UNSET
        if not isinstance(self.related_fields, Unset):
            related_fields = self.related_fields




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if short_reason is not UNSET:
            field_dict["short_reason"] = short_reason
        if long_reason is not UNSET:
            field_dict["long_reason"] = long_reason
        if related_fields is not UNSET:
            field_dict["related_fields"] = related_fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        short_reason = d.pop("short_reason", UNSET)

        long_reason = d.pop("long_reason", UNSET)

        related_fields = cast(list[str], d.pop("related_fields", UNSET))


        check_product_listing_response_data_pre_check_result_pre_check_detail = cls(
            short_reason=short_reason,
            long_reason=long_reason,
            related_fields=related_fields,
        )


        check_product_listing_response_data_pre_check_result_pre_check_detail.additional_properties = d
        return check_product_listing_response_data_pre_check_result_pre_check_detail

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
