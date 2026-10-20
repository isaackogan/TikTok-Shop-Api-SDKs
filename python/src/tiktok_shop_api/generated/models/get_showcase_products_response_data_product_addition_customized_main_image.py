from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetShowcaseProductsResponseDataProductAdditionCustomizedMainImage")



@_attrs_define
class GetShowcaseProductsResponseDataProductAdditionCustomizedMainImage:
    """ 
        Attributes:
            width (int | Unset): The image width in pixels.
            heigth (int | Unset): The image height in pixels.
            url (str | Unset): The product's TikTok Shop image URL.
     """

    width: int | Unset = UNSET
    heigth: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        width = self.width

        heigth = self.heigth

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if width is not UNSET:
            field_dict["width"] = width
        if heigth is not UNSET:
            field_dict["heigth"] = heigth
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width", UNSET)

        heigth = d.pop("heigth", UNSET)

        url = d.pop("url", UNSET)

        get_showcase_products_response_data_product_addition_customized_main_image = cls(
            width=width,
            heigth=heigth,
            url=url,
        )


        get_showcase_products_response_data_product_addition_customized_main_image.additional_properties = d
        return get_showcase_products_response_data_product_addition_customized_main_image

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
