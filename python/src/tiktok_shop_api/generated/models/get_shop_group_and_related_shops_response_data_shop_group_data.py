from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_group_and_related_shops_response_data_shop_group_data_shop import (
        GetShopGroupAndRelatedShopsResponseDataShopGroupDataShop,
    )
    from ..models.get_shop_group_and_related_shops_response_data_shop_group_data_shop_group import (
        GetShopGroupAndRelatedShopsResponseDataShopGroupDataShopGroup,
    )


T = TypeVar("T", bound="GetShopGroupAndRelatedShopsResponseDataShopGroupData")


@_attrs_define
class GetShopGroupAndRelatedShopsResponseDataShopGroupData:
    """
    Attributes:
        shop_group (GetShopGroupAndRelatedShopsResponseDataShopGroupDataShopGroup | Unset):
        shops (list[GetShopGroupAndRelatedShopsResponseDataShopGroupDataShop] | Unset): The shops in the product
            interoperability group. If `shop_group` is omitted, this lists the shops associated with the same global seller
            as the authenticated shop.
    """

    shop_group: GetShopGroupAndRelatedShopsResponseDataShopGroupDataShopGroup | Unset = UNSET
    shops: list[GetShopGroupAndRelatedShopsResponseDataShopGroupDataShop] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shop_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop_group, Unset):
            shop_group = self.shop_group.to_dict()

        shops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shops, Unset):
            shops = []
            for shops_item_data in self.shops:
                shops_item = shops_item_data.to_dict()
                shops.append(shops_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shop_group is not UNSET:
            field_dict["shop_group"] = shop_group
        if shops is not UNSET:
            field_dict["shops"] = shops

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_group_and_related_shops_response_data_shop_group_data_shop import (
            GetShopGroupAndRelatedShopsResponseDataShopGroupDataShop,  # noqa: PLC0415
        )
        from ..models.get_shop_group_and_related_shops_response_data_shop_group_data_shop_group import (
            GetShopGroupAndRelatedShopsResponseDataShopGroupDataShopGroup,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _shop_group = d.pop("shop_group", UNSET)
        shop_group: GetShopGroupAndRelatedShopsResponseDataShopGroupDataShopGroup | Unset
        if isinstance(_shop_group, Unset):
            shop_group = UNSET
        else:
            shop_group = GetShopGroupAndRelatedShopsResponseDataShopGroupDataShopGroup.from_dict(_shop_group)

        _shops = d.pop("shops", UNSET)
        shops: list[GetShopGroupAndRelatedShopsResponseDataShopGroupDataShop] | Unset = UNSET
        if _shops is not UNSET:
            shops = []
            for shops_item_data in _shops:
                shops_item = GetShopGroupAndRelatedShopsResponseDataShopGroupDataShop.from_dict(shops_item_data)

                shops.append(shops_item)

        get_shop_group_and_related_shops_response_data_shop_group_data = cls(
            shop_group=shop_group,
            shops=shops,
        )

        get_shop_group_and_related_shops_response_data_shop_group_data.additional_properties = d
        return get_shop_group_and_related_shops_response_data_shop_group_data

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
