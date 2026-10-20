from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shipping_template_availability_request_product_attribute_dimension import GetShippingTemplateAvailabilityRequestProductAttributeDimension
  from ..models.get_shipping_template_availability_request_product_attribute_weight import GetShippingTemplateAvailabilityRequestProductAttributeWeight





T = TypeVar("T", bound="GetShippingTemplateAvailabilityRequestProductAttribute")



@_attrs_define
class GetShippingTemplateAvailabilityRequestProductAttribute:
    """ 
        Attributes:
            weight (GetShippingTemplateAvailabilityRequestProductAttributeWeight | Unset):
            dimension (GetShippingTemplateAvailabilityRequestProductAttributeDimension | Unset):
     """

    weight: GetShippingTemplateAvailabilityRequestProductAttributeWeight | Unset = UNSET
    dimension: GetShippingTemplateAvailabilityRequestProductAttributeDimension | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shipping_template_availability_request_product_attribute_dimension import GetShippingTemplateAvailabilityRequestProductAttributeDimension # noqa: PLC0415
        from ..models.get_shipping_template_availability_request_product_attribute_weight import GetShippingTemplateAvailabilityRequestProductAttributeWeight # noqa: PLC0415
        weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimension, Unset):
            dimension = self.dimension.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if weight is not UNSET:
            field_dict["weight"] = weight
        if dimension is not UNSET:
            field_dict["dimension"] = dimension

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shipping_template_availability_request_product_attribute_dimension import GetShippingTemplateAvailabilityRequestProductAttributeDimension # noqa: PLC0415
        from ..models.get_shipping_template_availability_request_product_attribute_weight import GetShippingTemplateAvailabilityRequestProductAttributeWeight # noqa: PLC0415
        d = dict(src_dict)
        _weight = d.pop("weight", UNSET)
        weight: GetShippingTemplateAvailabilityRequestProductAttributeWeight | Unset
        if isinstance(_weight,  Unset):
            weight = UNSET
        else:
            weight = GetShippingTemplateAvailabilityRequestProductAttributeWeight.from_dict(_weight)




        _dimension = d.pop("dimension", UNSET)
        dimension: GetShippingTemplateAvailabilityRequestProductAttributeDimension | Unset
        if isinstance(_dimension,  Unset):
            dimension = UNSET
        else:
            dimension = GetShippingTemplateAvailabilityRequestProductAttributeDimension.from_dict(_dimension)




        get_shipping_template_availability_request_product_attribute = cls(
            weight=weight,
            dimension=dimension,
        )


        get_shipping_template_availability_request_product_attribute.additional_properties = d
        return get_shipping_template_availability_request_product_attribute

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
