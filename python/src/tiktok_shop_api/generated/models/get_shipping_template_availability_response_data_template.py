from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shipping_template_availability_response_data_template_service_unreachable_reason import GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReason
  from ..models.get_shipping_template_availability_response_data_template_template import GetShippingTemplateAvailabilityResponseDataTemplateTemplate





T = TypeVar("T", bound="GetShippingTemplateAvailabilityResponseDataTemplate")



@_attrs_define
class GetShippingTemplateAvailabilityResponseDataTemplate:
    """ 
        Attributes:
            template_is_available (bool | Unset): Whether the template is available
            template (GetShippingTemplateAvailabilityResponseDataTemplateTemplate | Unset):
            service_unreachable_reason (list[GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReason] |
                Unset): Reasons the shipping template is unavailable, grouped by shipping service. This field is omitted when
                the template is available.
     """

    template_is_available: bool | Unset = UNSET
    template: GetShippingTemplateAvailabilityResponseDataTemplateTemplate | Unset = UNSET
    service_unreachable_reason: list[GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shipping_template_availability_response_data_template_service_unreachable_reason import GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReason # noqa: PLC0415
        from ..models.get_shipping_template_availability_response_data_template_template import GetShippingTemplateAvailabilityResponseDataTemplateTemplate # noqa: PLC0415
        template_is_available = self.template_is_available

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        service_unreachable_reason: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_unreachable_reason, Unset):
            service_unreachable_reason = []
            for service_unreachable_reason_item_data in self.service_unreachable_reason:
                service_unreachable_reason_item = service_unreachable_reason_item_data.to_dict()
                service_unreachable_reason.append(service_unreachable_reason_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if template_is_available is not UNSET:
            field_dict["template_is_available"] = template_is_available
        if template is not UNSET:
            field_dict["template"] = template
        if service_unreachable_reason is not UNSET:
            field_dict["service_unreachable_reason"] = service_unreachable_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shipping_template_availability_response_data_template_service_unreachable_reason import GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReason # noqa: PLC0415
        from ..models.get_shipping_template_availability_response_data_template_template import GetShippingTemplateAvailabilityResponseDataTemplateTemplate # noqa: PLC0415
        d = dict(src_dict)
        template_is_available = d.pop("template_is_available", UNSET)

        _template = d.pop("template", UNSET)
        template: GetShippingTemplateAvailabilityResponseDataTemplateTemplate | Unset
        if isinstance(_template,  Unset):
            template = UNSET
        else:
            template = GetShippingTemplateAvailabilityResponseDataTemplateTemplate.from_dict(_template)




        _service_unreachable_reason = d.pop("service_unreachable_reason", UNSET)
        service_unreachable_reason: list[GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReason] | Unset = UNSET
        if _service_unreachable_reason is not UNSET:
            service_unreachable_reason = []
            for service_unreachable_reason_item_data in _service_unreachable_reason:
                service_unreachable_reason_item = GetShippingTemplateAvailabilityResponseDataTemplateServiceUnreachableReason.from_dict(service_unreachable_reason_item_data)



                service_unreachable_reason.append(service_unreachable_reason_item)


        get_shipping_template_availability_response_data_template = cls(
            template_is_available=template_is_available,
            template=template,
            service_unreachable_reason=service_unreachable_reason,
        )


        get_shipping_template_availability_response_data_template.additional_properties = d
        return get_shipping_template_availability_response_data_template

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
