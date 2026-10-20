from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchSampleApplicationFulfillmentsResponseDataFulfillmentProduct")



@_attrs_define
class SearchSampleApplicationFulfillmentsResponseDataFulfillmentProduct:
    """ 
        Attributes:
            id (str | Unset): The product identifier.
            main_image_url (str | Unset): The cover image url of product.
     """

    id: str | Unset = UNSET
    main_image_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        main_image_url = self.main_image_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if main_image_url is not UNSET:
            field_dict["main_image_url"] = main_image_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        main_image_url = d.pop("main_image_url", UNSET)

        search_sample_application_fulfillments_response_data_fulfillment_product = cls(
            id=id,
            main_image_url=main_image_url,
        )


        search_sample_application_fulfillments_response_data_fulfillment_product.additional_properties = d
        return search_sample_application_fulfillments_response_data_fulfillment_product

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
