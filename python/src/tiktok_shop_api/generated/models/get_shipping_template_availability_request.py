from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shipping_template_availability_request_product_attribute import (
        GetShippingTemplateAvailabilityRequestProductAttribute,
    )


T = TypeVar("T", bound="GetShippingTemplateAvailabilityRequest")


@_attrs_define
class GetShippingTemplateAvailabilityRequest:
    """
    Attributes:
        product_attribute (GetShippingTemplateAvailabilityRequestProductAttribute | Unset):
    """

    product_attribute: GetShippingTemplateAvailabilityRequestProductAttribute | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_attribute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_attribute, Unset):
            product_attribute = self.product_attribute.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_attribute is not UNSET:
            field_dict["product_attribute"] = product_attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shipping_template_availability_request_product_attribute import (
            GetShippingTemplateAvailabilityRequestProductAttribute,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _product_attribute = d.pop("product_attribute", UNSET)
        product_attribute: GetShippingTemplateAvailabilityRequestProductAttribute | Unset
        if isinstance(_product_attribute, Unset):
            product_attribute = UNSET
        else:
            product_attribute = GetShippingTemplateAvailabilityRequestProductAttribute.from_dict(_product_attribute)

        get_shipping_template_availability_request = cls(
            product_attribute=product_attribute,
        )

        get_shipping_template_availability_request.additional_properties = d
        return get_shipping_template_availability_request

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
