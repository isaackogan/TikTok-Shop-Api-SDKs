from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shipping_template_availability_response_data_template_service_unreachable_reason_filter_reason import GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReasonFilterReason





T = TypeVar("T", bound="GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReason")



@_attrs_define
class GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReason:
    """ 
        Attributes:
            service_id (str | Unset): Id of the service
            filter_reason (list[GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReasonFilterReason] |
                Unset): Reasons this shipping service is unavailable for the template.
     """

    service_id: str | Unset = UNSET
    filter_reason: list[GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReasonFilterReason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shipping_template_availability_response_data_template_service_unreachable_reason_filter_reason import GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReasonFilterReason # noqa: PLC0415
        service_id = self.service_id

        filter_reason: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_reason, Unset):
            filter_reason = []
            for filter_reason_item_data in self.filter_reason:
                filter_reason_item = filter_reason_item_data.to_dict()
                filter_reason.append(filter_reason_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if filter_reason is not UNSET:
            field_dict["filter_reason"] = filter_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shipping_template_availability_response_data_template_service_unreachable_reason_filter_reason import GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReasonFilterReason # noqa: PLC0415
        d = dict(src_dict)
        service_id = d.pop("service_id", UNSET)

        _filter_reason = d.pop("filter_reason", UNSET)
        filter_reason: list[GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReasonFilterReason] | Unset = UNSET
        if _filter_reason is not UNSET:
            filter_reason = []
            for filter_reason_item_data in _filter_reason:
                filter_reason_item = GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReasonFilterReason.from_dict(filter_reason_item_data)



                filter_reason.append(filter_reason_item)


        get_shipping_template_availability_response_data_template_service_unreachable_reason = cls(
            service_id=service_id,
            filter_reason=filter_reason,
        )


        get_shipping_template_availability_response_data_template_service_unreachable_reason.additional_properties = d
        return get_shipping_template_availability_response_data_template_service_unreachable_reason

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
