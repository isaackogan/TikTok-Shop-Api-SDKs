from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.gift_info_threshold_type import GiftInfoThresholdType
from typing import cast

if TYPE_CHECKING:
  from ..models.gift_detail import GiftDetail





T = TypeVar("T", bound="GiftInfo")



@_attrs_define
class GiftInfo:
    """ 
        Attributes:
            tier (int): `tier` uses 1-based indexing, i.e. the first and second tiers are counted "1, 2", not "0, 1".
                `threshold_value` for a given tier must be greater than that of the previous tier.
                E.g. If `tier`==1 has `threshold_value`==`2`, `tier`==2 must have `threshold_value` > `2`.
            threshold_type (GiftInfoThresholdType): The purchase threshold type of discount. Possible enumerations are:
                - `MINIMAL_ITEM_QUANTITY`: Buyer must meet or exceed the minimum spend criteria with eligible products.
                - `MINIMAL_ORDER_AMOUNT`: Buyer must meet or exceed the minimum spend criteria with eligible order.
            threshold_value (str): The purchase threshold for the gift, determined by `threshold_type`.
                - When `threshold_type==MINIMAL_ITEM_QUANTITY`, enter a positive integer number of eligible products.
                - When `threshold_type==MINIMAL_ORDER_AMOUNT`, enter a positive eligible-product subtotal in local currency,
                with at most two decimal places.
            gift_details (list[GiftDetail]): The gift SKUs for this tier. Across all tiers, provide at least one gift SKU in
                total, and do not repeat the same sku_id anywhere in the activity. For a MINIMAL_ITEM_QUANTITY tier, this list
                must not be empty.
     """

    tier: int
    threshold_type: GiftInfoThresholdType
    threshold_value: str
    gift_details: list[GiftDetail]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gift_detail import GiftDetail # noqa: PLC0415
        tier = self.tier

        threshold_type = self.threshold_type.value

        threshold_value = self.threshold_value

        gift_details = []
        for gift_details_item_data in self.gift_details:
            gift_details_item = gift_details_item_data.to_dict()
            gift_details.append(gift_details_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tier": tier,
            "threshold_type": threshold_type,
            "threshold_value": threshold_value,
            "gift_details": gift_details,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift_detail import GiftDetail # noqa: PLC0415
        d = dict(src_dict)
        tier = d.pop("tier")

        threshold_type = GiftInfoThresholdType(d.pop("threshold_type"))




        threshold_value = d.pop("threshold_value")

        gift_details = []
        _gift_details = d.pop("gift_details")
        for gift_details_item_data in (_gift_details):
            gift_details_item = GiftDetail.from_dict(gift_details_item_data)



            gift_details.append(gift_details_item)


        gift_info = cls(
            tier=tier,
            threshold_type=threshold_type,
            threshold_value=threshold_value,
            gift_details=gift_details,
        )


        gift_info.additional_properties = d
        return gift_info

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
