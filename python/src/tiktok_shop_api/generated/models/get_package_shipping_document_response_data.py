from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPackageShippingDocumentResponseData")


@_attrs_define
class GetPackageShippingDocumentResponseData:
    """
    Attributes:
        doc_url (str | Unset): The URL of the shipping document generated for the specified package according to the
            requested `document_type`. The URL is valid for 24 hours.
        tracking_number (str | Unset): The package tracking number from the shipping carrier.
    """

    doc_url: str | Unset = UNSET
    tracking_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        doc_url = self.doc_url

        tracking_number = self.tracking_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_url is not UNSET:
            field_dict["doc_url"] = doc_url
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        doc_url = d.pop("doc_url", UNSET)

        tracking_number = d.pop("tracking_number", UNSET)

        get_package_shipping_document_response_data = cls(
            doc_url=doc_url,
            tracking_number=tracking_number,
        )

        get_package_shipping_document_response_data.additional_properties = d
        return get_package_shipping_document_response_data

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
