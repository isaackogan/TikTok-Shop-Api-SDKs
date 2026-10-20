from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_brands_response_data_brand import GetBrandsResponseDataBrand





T = TypeVar("T", bound="GetBrandsResponseData")



@_attrs_define
class GetBrandsResponseData:
    """ 
        Attributes:
            brands (list[GetBrandsResponseDataBrand] | Unset): The list of brands that meet the query conditions.
            total_count (int | Unset): The total count of brands that meet the query conditions.
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. If this
                value is non-empty, pass it in the `page_token` parameter of the next request. An empty value means there are no
                more results.
     """

    brands: list[GetBrandsResponseDataBrand] | Unset = UNSET
    total_count: int | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_brands_response_data_brand import GetBrandsResponseDataBrand # noqa: PLC0415
        brands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.brands, Unset):
            brands = []
            for brands_item_data in self.brands:
                brands_item = brands_item_data.to_dict()
                brands.append(brands_item)



        total_count = self.total_count

        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if brands is not UNSET:
            field_dict["brands"] = brands
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_brands_response_data_brand import GetBrandsResponseDataBrand # noqa: PLC0415
        d = dict(src_dict)
        _brands = d.pop("brands", UNSET)
        brands: list[GetBrandsResponseDataBrand] | Unset = UNSET
        if _brands is not UNSET:
            brands = []
            for brands_item_data in _brands:
                brands_item = GetBrandsResponseDataBrand.from_dict(brands_item_data)



                brands.append(brands_item)


        total_count = d.pop("total_count", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        get_brands_response_data = cls(
            brands=brands,
            total_count=total_count,
            next_page_token=next_page_token,
        )


        get_brands_response_data.additional_properties = d
        return get_brands_response_data

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
