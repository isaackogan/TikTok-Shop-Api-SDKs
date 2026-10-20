from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_activity_response_data_discount_bmsm_discount_detail import GetActivityResponseDataDiscountBmsmDiscountDetail





T = TypeVar("T", bound="GetActivityResponseDataDiscountBmsmDiscount")



@_attrs_define
class GetActivityResponseDataDiscountBmsmDiscount:
    """ 
        Attributes:
            details (list[GetActivityResponseDataDiscountBmsmDiscountDetail] | Unset): Configurations for BMSM promotions.
                A maximum of two `tier`s are permitted. `details.threshold_type` and `details.type` must be the same across all
                `tier`s.
     """

    details: list[GetActivityResponseDataDiscountBmsmDiscountDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_activity_response_data_discount_bmsm_discount_detail import GetActivityResponseDataDiscountBmsmDiscountDetail # noqa: PLC0415
        details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_activity_response_data_discount_bmsm_discount_detail import GetActivityResponseDataDiscountBmsmDiscountDetail # noqa: PLC0415
        d = dict(src_dict)
        _details = d.pop("details", UNSET)
        details: list[GetActivityResponseDataDiscountBmsmDiscountDetail] | Unset = UNSET
        if _details is not UNSET:
            details = []
            for details_item_data in _details:
                details_item = GetActivityResponseDataDiscountBmsmDiscountDetail.from_dict(details_item_data)



                details.append(details_item)


        get_activity_response_data_discount_bmsm_discount = cls(
            details=details,
        )


        get_activity_response_data_discount_bmsm_discount.additional_properties = d
        return get_activity_response_data_discount_bmsm_discount

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
