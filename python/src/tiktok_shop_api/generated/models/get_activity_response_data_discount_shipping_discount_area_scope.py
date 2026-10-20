from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetActivityResponseDataDiscountShippingDiscountAreaScope")


@_attrs_define
class GetActivityResponseDataDiscountShippingDiscountAreaScope:
    """
    Attributes:
        type_ (str | Unset): The (buyer's) geographical area to which the promotion activity applies.
            ​- `WHOLE`: Promotion activity applies to all areas to which the seller offers fulfillment.
            - `SPECIFIC_AREAS`: Only applies to specific fulfillment areas, as defined in `area_scope.specific_areas`.
        specific_areas (list[str] | Unset): The list of areas for which the promotion activity applies. The valid values
            that may be included in this list are dependent on the region of the shop. The list of valid values for each
            shop region are available here: [link](https://partner.tiktokshop.com/docv2/page/67e3b059e7dc4f04a4ff9e09)
    """

    type_: str | Unset = UNSET
    specific_areas: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        specific_areas: list[str] | Unset = UNSET
        if not isinstance(self.specific_areas, Unset):
            specific_areas = self.specific_areas

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if specific_areas is not UNSET:
            field_dict["specific_areas"] = specific_areas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        specific_areas = cast(list[str], d.pop("specific_areas", UNSET))

        get_activity_response_data_discount_shipping_discount_area_scope = cls(
            type_=type_,
            specific_areas=specific_areas,
        )

        get_activity_response_data_discount_shipping_discount_area_scope.additional_properties = d
        return get_activity_response_data_discount_shipping_discount_area_scope

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
