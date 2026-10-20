from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_manufacturers_response_data_manufacturer import SearchManufacturersResponseDataManufacturer





T = TypeVar("T", bound="SearchManufacturersResponseData")



@_attrs_define
class SearchManufacturersResponseData:
    """ 
        Attributes:
            manufacturers (list[SearchManufacturersResponseDataManufacturer] | Unset): The list of manufacturers that meet
                the query conditions.
            total_count (int | Unset): The number of manufacturers that meet the query conditions.
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. Provide
                this value in the `page_token` parameter of your request if the current response does not return all the
                results.
     """

    manufacturers: list[SearchManufacturersResponseDataManufacturer] | Unset = UNSET
    total_count: int | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_manufacturers_response_data_manufacturer import SearchManufacturersResponseDataManufacturer # noqa: PLC0415
        manufacturers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.manufacturers, Unset):
            manufacturers = []
            for manufacturers_item_data in self.manufacturers:
                manufacturers_item = manufacturers_item_data.to_dict()
                manufacturers.append(manufacturers_item)



        total_count = self.total_count

        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if manufacturers is not UNSET:
            field_dict["manufacturers"] = manufacturers
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_manufacturers_response_data_manufacturer import SearchManufacturersResponseDataManufacturer # noqa: PLC0415
        d = dict(src_dict)
        _manufacturers = d.pop("manufacturers", UNSET)
        manufacturers: list[SearchManufacturersResponseDataManufacturer] | Unset = UNSET
        if _manufacturers is not UNSET:
            manufacturers = []
            for manufacturers_item_data in _manufacturers:
                manufacturers_item = SearchManufacturersResponseDataManufacturer.from_dict(manufacturers_item_data)



                manufacturers.append(manufacturers_item)


        total_count = d.pop("total_count", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        search_manufacturers_response_data = cls(
            manufacturers=manufacturers,
            total_count=total_count,
            next_page_token=next_page_token,
        )


        search_manufacturers_response_data.additional_properties = d
        return search_manufacturers_response_data

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
