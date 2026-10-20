from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_active_shops_response_data_shop import GetActiveShopsResponseDataShop


T = TypeVar("T", bound="GetActiveShopsResponseData")


@_attrs_define
class GetActiveShopsResponseData:
    """
    Attributes:
        shops (list[GetActiveShopsResponseDataShop] | Unset): The list of active shops that belong to the seller.
            Note: Local sellers only have 1 shop.
    """

    shops: list[GetActiveShopsResponseDataShop] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shops, Unset):
            shops = []
            for shops_item_data in self.shops:
                shops_item = shops_item_data.to_dict()
                shops.append(shops_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shops is not UNSET:
            field_dict["shops"] = shops

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_active_shops_response_data_shop import GetActiveShopsResponseDataShop  # noqa: PLC0415

        d = dict(src_dict)
        _shops = d.pop("shops", UNSET)
        shops: list[GetActiveShopsResponseDataShop] | Unset = UNSET
        if _shops is not UNSET:
            shops = []
            for shops_item_data in _shops:
                shops_item = GetActiveShopsResponseDataShop.from_dict(shops_item_data)

                shops.append(shops_item)

        get_active_shops_response_data = cls(
            shops=shops,
        )

        get_active_shops_response_data.additional_properties = d
        return get_active_shops_response_data

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
