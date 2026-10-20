from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchSampleApplicationsResponseDataSampleApplicationProduct")



@_attrs_define
class SearchSampleApplicationsResponseDataSampleApplicationProduct:
    """ 
        Attributes:
            id (str | Unset): The product identifier.
            title (str | Unset): The product name of the product.
            sku_id (str | Unset): The unique id of product sku which creator apply for as sample.
            sku_image_url (str | Unset): The URL of SKU image.
            sku_name (str | Unset): The SKU property value names, joined by commas.
     """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    sku_image_url: str | Unset = UNSET
    sku_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        sku_id = self.sku_id

        sku_image_url = self.sku_image_url

        sku_name = self.sku_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if sku_image_url is not UNSET:
            field_dict["sku_image_url"] = sku_image_url
        if sku_name is not UNSET:
            field_dict["sku_name"] = sku_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        sku_image_url = d.pop("sku_image_url", UNSET)

        sku_name = d.pop("sku_name", UNSET)

        search_sample_applications_response_data_sample_application_product = cls(
            id=id,
            title=title,
            sku_id=sku_id,
            sku_image_url=sku_image_url,
            sku_name=sku_name,
        )


        search_sample_applications_response_data_sample_application_product.additional_properties = d
        return search_sample_applications_response_data_sample_application_product

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
