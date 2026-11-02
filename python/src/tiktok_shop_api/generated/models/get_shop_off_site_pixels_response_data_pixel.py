from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetShopOffSitePixelsResponseDataPixel")



@_attrs_define
class GetShopOffSitePixelsResponseDataPixel:
    """ 
        Attributes:
            pixel_id (str | Unset): Pixel ID available for off-site analysis in the report-data window. Pass this value as
                pixel_id when requesting off-site reports for the same authorized shop.
            pixel_name (str | Unset): Display name of the Pixel as returned by the report data source.
     """

    pixel_id: str | Unset = UNSET
    pixel_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        pixel_id = self.pixel_id

        pixel_name = self.pixel_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if pixel_id is not UNSET:
            field_dict["pixel_id"] = pixel_id
        if pixel_name is not UNSET:
            field_dict["pixel_name"] = pixel_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pixel_id = d.pop("pixel_id", UNSET)

        pixel_name = d.pop("pixel_name", UNSET)

        get_shop_off_site_pixels_response_data_pixel = cls(
            pixel_id=pixel_id,
            pixel_name=pixel_name,
        )


        get_shop_off_site_pixels_response_data_pixel.additional_properties = d
        return get_shop_off_site_pixels_response_data_pixel

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
