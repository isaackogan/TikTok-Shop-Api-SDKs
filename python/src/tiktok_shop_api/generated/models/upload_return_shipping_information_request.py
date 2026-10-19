from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="UploadReturnShippingInformationRequest")


@_attrs_define
class UploadReturnShippingInformationRequest:
    """
    Attributes:
        tracking_number (str): The return shipping tracking number provided by the seller to the buyer.
        return_provider_id (str): The return shipping provider ID provided by the seller to the buyer.
        return_shipping_label (File | Unset): Return shipping label.
        return_qr_code (File | Unset): Return QR code.
    """

    tracking_number: str
    return_provider_id: str
    return_shipping_label: File | Unset = UNSET
    return_qr_code: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracking_number = self.tracking_number

        return_provider_id = self.return_provider_id

        return_shipping_label: FileTypes | Unset = UNSET
        if not isinstance(self.return_shipping_label, Unset):
            return_shipping_label = self.return_shipping_label.to_tuple()

        return_qr_code: FileTypes | Unset = UNSET
        if not isinstance(self.return_qr_code, Unset):
            return_qr_code = self.return_qr_code.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tracking_number": tracking_number,
                "return_provider_id": return_provider_id,
            }
        )
        if return_shipping_label is not UNSET:
            field_dict["return_shipping_label"] = return_shipping_label
        if return_qr_code is not UNSET:
            field_dict["return_qr_code"] = return_qr_code

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("tracking_number", (None, str(self.tracking_number).encode(), "text/plain")))

        files.append(("return_provider_id", (None, str(self.return_provider_id).encode(), "text/plain")))

        if not isinstance(self.return_shipping_label, Unset):
            files.append(("return_shipping_label", self.return_shipping_label.to_tuple()))

        if not isinstance(self.return_qr_code, Unset):
            files.append(("return_qr_code", self.return_qr_code.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tracking_number = d.pop("tracking_number")

        return_provider_id = d.pop("return_provider_id")

        _return_shipping_label = d.pop("return_shipping_label", UNSET)
        return_shipping_label: File | Unset
        if isinstance(_return_shipping_label, Unset):
            return_shipping_label = UNSET
        else:
            return_shipping_label = File(payload=BytesIO(_return_shipping_label))

        _return_qr_code = d.pop("return_qr_code", UNSET)
        return_qr_code: File | Unset
        if isinstance(_return_qr_code, Unset):
            return_qr_code = UNSET
        else:
            return_qr_code = File(payload=BytesIO(_return_qr_code))

        upload_return_shipping_information_request = cls(
            tracking_number=tracking_number,
            return_provider_id=return_provider_id,
            return_shipping_label=return_shipping_label,
            return_qr_code=return_qr_code,
        )

        upload_return_shipping_information_request.additional_properties = d
        return upload_return_shipping_information_request

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
