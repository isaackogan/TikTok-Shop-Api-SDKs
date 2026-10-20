from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gift_info import GiftInfo


T = TypeVar("T", bound="GiftDiscount")


@_attrs_define
class GiftDiscount:
    """
    Attributes:
        gift_receiving_type (str): The receiving type of gift. Currently only one type is supported:
            - `ALL_RECEIVE`: All gifts configured in the promotion can be collected.
        gift_infos (list[GiftInfo]): Gift With Purchase tier configurations. Provide at least one tier. A maximum of two
            tiers is permitted in SEA and the UK, while only one tier is permitted in the US. `threshold_type` must be the
            same across all tiers.
    """

    gift_receiving_type: str
    gift_infos: list[GiftInfo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gift_receiving_type = self.gift_receiving_type

        gift_infos = []
        for gift_infos_item_data in self.gift_infos:
            gift_infos_item = gift_infos_item_data.to_dict()
            gift_infos.append(gift_infos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gift_receiving_type": gift_receiving_type,
                "gift_infos": gift_infos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift_info import GiftInfo  # noqa: PLC0415

        d = dict(src_dict)
        gift_receiving_type = d.pop("gift_receiving_type")

        gift_infos = []
        _gift_infos = d.pop("gift_infos")
        for gift_infos_item_data in _gift_infos:
            gift_infos_item = GiftInfo.from_dict(gift_infos_item_data)

            gift_infos.append(gift_infos_item)

        gift_discount = cls(
            gift_receiving_type=gift_receiving_type,
            gift_infos=gift_infos,
        )

        gift_discount.additional_properties = d
        return gift_discount

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
