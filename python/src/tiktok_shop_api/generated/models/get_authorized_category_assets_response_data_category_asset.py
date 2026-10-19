from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_authorized_category_assets_response_data_category_asset_category import (
        GetAuthorizedCategoryAssetsResponseDataCategoryAssetCategory,
    )


T = TypeVar("T", bound="GetAuthorizedCategoryAssetsResponseDataCategoryAsset")


@_attrs_define
class GetAuthorizedCategoryAssetsResponseDataCategoryAsset:
    """
    Attributes:
        cipher (str | Unset): The encrypted category asset cipher for this authorized business category and target
            market. Use it as an input parameter in affiliate partner related APIs; you do not need to decrypt it.
        target_market (str | Unset): The target market associated with this authorized business category and its
            category asset cipher.
        category (GetAuthorizedCategoryAssetsResponseDataCategoryAssetCategory | Unset):
    """

    cipher: str | Unset = UNSET
    target_market: str | Unset = UNSET
    category: GetAuthorizedCategoryAssetsResponseDataCategoryAssetCategory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cipher = self.cipher

        target_market = self.target_market

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cipher is not UNSET:
            field_dict["cipher"] = cipher
        if target_market is not UNSET:
            field_dict["target_market"] = target_market
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_authorized_category_assets_response_data_category_asset_category import (
            GetAuthorizedCategoryAssetsResponseDataCategoryAssetCategory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        cipher = d.pop("cipher", UNSET)

        target_market = d.pop("target_market", UNSET)

        _category = d.pop("category", UNSET)
        category: GetAuthorizedCategoryAssetsResponseDataCategoryAssetCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = GetAuthorizedCategoryAssetsResponseDataCategoryAssetCategory.from_dict(_category)

        get_authorized_category_assets_response_data_category_asset = cls(
            cipher=cipher,
            target_market=target_market,
            category=category,
        )

        get_authorized_category_assets_response_data_category_asset.additional_properties = d
        return get_authorized_category_assets_response_data_category_asset

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
