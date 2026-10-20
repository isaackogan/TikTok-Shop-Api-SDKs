from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.suggest_brands_response_data_brand import SuggestBrandsResponseDataBrand





T = TypeVar("T", bound="SuggestBrandsResponseData")



@_attrs_define
class SuggestBrandsResponseData:
    """ 
        Attributes:
            brands (list[SuggestBrandsResponseDataBrand] | Unset): Recommended brands in recommendation order. Empty when no
                recommendations are available.
     """

    brands: list[SuggestBrandsResponseDataBrand] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.suggest_brands_response_data_brand import SuggestBrandsResponseDataBrand # noqa: PLC0415
        brands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.brands, Unset):
            brands = []
            for brands_item_data in self.brands:
                brands_item = brands_item_data.to_dict()
                brands.append(brands_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if brands is not UNSET:
            field_dict["brands"] = brands

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.suggest_brands_response_data_brand import SuggestBrandsResponseDataBrand # noqa: PLC0415
        d = dict(src_dict)
        _brands = d.pop("brands", UNSET)
        brands: list[SuggestBrandsResponseDataBrand] | Unset = UNSET
        if _brands is not UNSET:
            brands = []
            for brands_item_data in _brands:
                brands_item = SuggestBrandsResponseDataBrand.from_dict(brands_item_data)



                brands.append(brands_item)


        suggest_brands_response_data = cls(
            brands=brands,
        )


        suggest_brands_response_data.additional_properties = d
        return suggest_brands_response_data

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
