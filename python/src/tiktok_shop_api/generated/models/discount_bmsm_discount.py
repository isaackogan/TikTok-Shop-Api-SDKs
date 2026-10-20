from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_promotion_activity_request_discount_bmsm_discount_detail import CreatePromotionActivityRequestDiscountBmsmDiscountDetail





T = TypeVar("T", bound="DiscountBmsmDiscount")



@_attrs_define
class DiscountBmsmDiscount:
    """ 
        Attributes:
            details (list[CreatePromotionActivityRequestDiscountBmsmDiscountDetail] | Unset): Configurations for Buy More
                Save More tiers. Provide one or two tiers. `threshold_type` and `type` must be the same across all tiers.
     """

    details: list[CreatePromotionActivityRequestDiscountBmsmDiscountDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_promotion_activity_request_discount_bmsm_discount_detail import CreatePromotionActivityRequestDiscountBmsmDiscountDetail # noqa: PLC0415
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
        from ..models.create_promotion_activity_request_discount_bmsm_discount_detail import CreatePromotionActivityRequestDiscountBmsmDiscountDetail # noqa: PLC0415
        d = dict(src_dict)
        _details = d.pop("details", UNSET)
        details: list[CreatePromotionActivityRequestDiscountBmsmDiscountDetail] | Unset = UNSET
        if _details is not UNSET:
            details = []
            for details_item_data in _details:
                details_item = CreatePromotionActivityRequestDiscountBmsmDiscountDetail.from_dict(details_item_data)



                details.append(details_item)


        discount_bmsm_discount = cls(
            details=details,
        )


        discount_bmsm_discount.additional_properties = d
        return discount_bmsm_discount

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
