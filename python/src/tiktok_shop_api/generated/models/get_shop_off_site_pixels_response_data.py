from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shop_off_site_pixels_response_data_pixel import GetShopOffSitePixelsResponseDataPixel





T = TypeVar("T", bound="GetShopOffSitePixelsResponseData")



@_attrs_define
class GetShopOffSitePixelsResponseData:
    """ 
        Attributes:
            pixels (list[GetShopOffSitePixelsResponseDataPixel] | Unset): Pixels available for off-site analysis for the
                authorized shop within the latest 56-day report-data window. This is not a list of every Pixel ever linked to
                the shop; newly linked Pixels without report data and Pixels with no recent data may be absent. Entries with a
                missing or blank Pixel ID or name, or a Pixel ID of 0, are excluded. An empty list means no analyzable Pixels
                were found in this window.
     """

    pixels: list[GetShopOffSitePixelsResponseDataPixel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_off_site_pixels_response_data_pixel import GetShopOffSitePixelsResponseDataPixel # noqa: PLC0415
        pixels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pixels, Unset):
            pixels = []
            for pixels_item_data in self.pixels:
                pixels_item = pixels_item_data.to_dict()
                pixels.append(pixels_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if pixels is not UNSET:
            field_dict["pixels"] = pixels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_off_site_pixels_response_data_pixel import GetShopOffSitePixelsResponseDataPixel # noqa: PLC0415
        d = dict(src_dict)
        _pixels = d.pop("pixels", UNSET)
        pixels: list[GetShopOffSitePixelsResponseDataPixel] | Unset = UNSET
        if _pixels is not UNSET:
            pixels = []
            for pixels_item_data in _pixels:
                pixels_item = GetShopOffSitePixelsResponseDataPixel.from_dict(pixels_item_data)



                pixels.append(pixels_item)


        get_shop_off_site_pixels_response_data = cls(
            pixels=pixels,
        )


        get_shop_off_site_pixels_response_data.additional_properties = d
        return get_shop_off_site_pixels_response_data

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
