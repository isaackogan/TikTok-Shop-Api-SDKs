from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_acc_brands_response_data_brand import GetACCBrandsResponseDataBrand





T = TypeVar("T", bound="GetACCBrandsResponseData")



@_attrs_define
class GetACCBrandsResponseData:
    """ 
        Attributes:
            brands (list[GetACCBrandsResponseDataBrand] | Unset): Authorized brand and industry records for the current
                shop. Returns all records without pagination and in no guaranteed order; an empty array means no authorized
                records. Records are deduplicated by brand ID and do not enumerate every possible brand-industry relationship.
                Use brand_id and industry_id from the same record in the other ACC data APIs.
     """

    brands: list[GetACCBrandsResponseDataBrand] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_brands_response_data_brand import GetACCBrandsResponseDataBrand # noqa: PLC0415
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
        from ..models.get_acc_brands_response_data_brand import GetACCBrandsResponseDataBrand # noqa: PLC0415
        d = dict(src_dict)
        _brands = d.pop("brands", UNSET)
        brands: list[GetACCBrandsResponseDataBrand] | Unset = UNSET
        if _brands is not UNSET:
            brands = []
            for brands_item_data in _brands:
                brands_item = GetACCBrandsResponseDataBrand.from_dict(brands_item_data)



                brands.append(brands_item)


        get_acc_brands_response_data = cls(
            brands=brands,
        )


        get_acc_brands_response_data.additional_properties = d
        return get_acc_brands_response_data

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
