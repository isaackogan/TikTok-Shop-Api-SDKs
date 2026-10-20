from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_authorized_category_assets_response_data_category_asset import GetAuthorizedCategoryAssetsResponseDataCategoryAsset





T = TypeVar("T", bound="GetAuthorizedCategoryAssetsResponseData")



@_attrs_define
class GetAuthorizedCategoryAssetsResponseData:
    """ 
        Attributes:
            category_assets (list[GetAuthorizedCategoryAssetsResponseDataCategoryAsset] | Unset): The list of business
                category assets that a partner has authorized for the app.
     """

    category_assets: list[GetAuthorizedCategoryAssetsResponseDataCategoryAsset] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_authorized_category_assets_response_data_category_asset import GetAuthorizedCategoryAssetsResponseDataCategoryAsset # noqa: PLC0415
        category_assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category_assets, Unset):
            category_assets = []
            for category_assets_item_data in self.category_assets:
                category_assets_item = category_assets_item_data.to_dict()
                category_assets.append(category_assets_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if category_assets is not UNSET:
            field_dict["category_assets"] = category_assets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_authorized_category_assets_response_data_category_asset import GetAuthorizedCategoryAssetsResponseDataCategoryAsset # noqa: PLC0415
        d = dict(src_dict)
        _category_assets = d.pop("category_assets", UNSET)
        category_assets: list[GetAuthorizedCategoryAssetsResponseDataCategoryAsset] | Unset = UNSET
        if _category_assets is not UNSET:
            category_assets = []
            for category_assets_item_data in _category_assets:
                category_assets_item = GetAuthorizedCategoryAssetsResponseDataCategoryAsset.from_dict(category_assets_item_data)



                category_assets.append(category_assets_item)


        get_authorized_category_assets_response_data = cls(
            category_assets=category_assets,
        )


        get_authorized_category_assets_response_data.additional_properties = d
        return get_authorized_category_assets_response_data

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
