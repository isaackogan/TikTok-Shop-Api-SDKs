from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.upload_invoice_request_invoice_file_type import UploadInvoiceRequestInvoiceFileType
from typing import cast






T = TypeVar("T", bound="UploadInvoiceRequestInvoice")



@_attrs_define
class UploadInvoiceRequestInvoice:
    """ 
        Attributes:
            package_id (str): The TikTok Shop package ID, retrieved from [Search Package](650aa592bace3e02b75db748).
            order_ids (list[str]): The list of TikTok Shop order IDs, retrieved from [Get Order
                List](650aa8094a0bb702c06df242).
            file_type (UploadInvoiceRequestInvoiceFileType): The invoice file format.
                Possible values:
                - `XML`
            file (str): Base64 encoding of the invoice file to upload.
                Max file size: 1MB
     """

    package_id: str
    order_ids: list[str]
    file_type: UploadInvoiceRequestInvoiceFileType
    file: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        package_id = self.package_id

        order_ids = self.order_ids



        file_type = self.file_type.value

        file = self.file


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "package_id": package_id,
            "order_ids": order_ids,
            "file_type": file_type,
            "file": file,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_id = d.pop("package_id")

        order_ids = cast(list[str], d.pop("order_ids"))


        file_type = UploadInvoiceRequestInvoiceFileType(d.pop("file_type"))




        file = d.pop("file")

        upload_invoice_request_invoice = cls(
            package_id=package_id,
            order_ids=order_ids,
            file_type=file_type,
            file=file,
        )


        upload_invoice_request_invoice.additional_properties = d
        return upload_invoice_request_invoice

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
