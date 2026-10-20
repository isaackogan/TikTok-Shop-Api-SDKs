from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_manufacturers_request_locales_item import SearchManufacturersRequestLocalesItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchManufacturersRequest")



@_attrs_define
class SearchManufacturersRequest:
    """ 
        Attributes:
            manufacturer_ids (list[str] | Unset): Filter results by these manufacturer IDs.
                Max IDs: The value of `page_size`
            keyword (str | Unset): Filter results to show those that contain this keyword.
                Search scope: name, registered trade name, local_number, email
                Max length: 200 characters

                **Note**: Provide either the `manufacturer_ids` or `keyword`; if both are provided, `manufacturer_ids` will take
                priority.
            locales (list[SearchManufacturersRequestLocalesItem] | Unset): The BCP-47 locale codes for displaying the
                manufacturer information.
                Default: The locale of the seller's registered business address.
                Possible values:
                - de-DE
                - en-IE
                - es-ES
                - fr-FR
                - it-IT
     """

    manufacturer_ids: list[str] | Unset = UNSET
    keyword: str | Unset = UNSET
    locales: list[SearchManufacturersRequestLocalesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        manufacturer_ids: list[str] | Unset = UNSET
        if not isinstance(self.manufacturer_ids, Unset):
            manufacturer_ids = self.manufacturer_ids



        keyword = self.keyword

        locales: list[str] | Unset = UNSET
        if not isinstance(self.locales, Unset):
            locales = []
            for locales_item_data in self.locales:
                locales_item = locales_item_data.value
                locales.append(locales_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if manufacturer_ids is not UNSET:
            field_dict["manufacturer_ids"] = manufacturer_ids
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if locales is not UNSET:
            field_dict["locales"] = locales

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        manufacturer_ids = cast(list[str], d.pop("manufacturer_ids", UNSET))


        keyword = d.pop("keyword", UNSET)

        _locales = d.pop("locales", UNSET)
        locales: list[SearchManufacturersRequestLocalesItem] | Unset = UNSET
        if _locales is not UNSET:
            locales = []
            for locales_item_data in _locales:
                locales_item = SearchManufacturersRequestLocalesItem(locales_item_data)



                locales.append(locales_item)


        search_manufacturers_request = cls(
            manufacturer_ids=manufacturer_ids,
            keyword=keyword,
            locales=locales,
        )


        search_manufacturers_request.additional_properties = d
        return search_manufacturers_request

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
