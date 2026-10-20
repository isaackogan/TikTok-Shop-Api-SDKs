from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReasonFilterReason")



@_attrs_define
class GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReasonFilterReason:
    """ 
        Attributes:
            filter_type (str | Unset): 1 for length filter
                2 for width filter
                3 for height filter
                4 for weight filter
                9 for service mode filter
                11 for service filter
            reason (str | Unset): Detailed reason for unreachable
     """

    filter_type: str | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        filter_type = self.filter_type

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if filter_type is not UNSET:
            field_dict["filter_type"] = filter_type
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_type = d.pop("filter_type", UNSET)

        reason = d.pop("reason", UNSET)

        get_shipping_template_availability_response_data_template_service_unreachable_reason_filter_reason = cls(
            filter_type=filter_type,
            reason=reason,
        )


        get_shipping_template_availability_response_data_template_service_unreachable_reason_filter_reason.additional_properties = d
        return get_shipping_template_availability_response_data_template_service_unreachable_reason_filter_reason

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
