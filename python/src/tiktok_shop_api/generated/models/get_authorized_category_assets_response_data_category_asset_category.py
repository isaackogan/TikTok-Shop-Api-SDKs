from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetAuthorizedCategoryAssetsResponseDataCategoryAssetCategory")



@_attrs_define
class GetAuthorizedCategoryAssetsResponseDataCategoryAssetCategory:
    """ 
        Attributes:
            id (int | Unset): The ID of the business category. Use this field to verify if the partner has authorized the
                correct category. Otherwise, request re-authorization from the partner by referring to the [Partner
                authorization guide](https://partner.tiktokshop.com/docv2/page/669a301bd92cd602fd403ff9).
            name (str | Unset): The name of the business category. This name may change.
     """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        get_authorized_category_assets_response_data_category_asset_category = cls(
            id=id,
            name=name,
        )


        get_authorized_category_assets_response_data_category_asset_category.additional_properties = d
        return get_authorized_category_assets_response_data_category_asset_category

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
