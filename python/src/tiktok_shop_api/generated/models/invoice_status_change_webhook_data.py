from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="InvoiceStatusChangeWebhookData")



@_attrs_define
class InvoiceStatusChangeWebhookData:
    """ 
        Attributes:
            package_id (str | Unset): The ID of the package.
            order_ids (list[str] | Unset): List of order IDs in the corresponding `package_id`.
            invoice_status (str | Unset): The status of the invoice upload. Possible values:

                 * `SUCCESS`
                 * `PROCESSING`
                 * `FAILED`
                 * `INVALID`
            invalid_reason (str | Unset): The reason why `invoice_status = INVALID`. Possible values:

                 * `UNKNOWN`: Internal system error. Please try again later.
                 * `FAILED`: The NFe file or access key is invalid. Please check the XML file for correctness.
                 * `NOT_FOUND`: The NFe was not found. This may be due to data delay. Please try again later.
                 * `NOT_AUTHORIZED`: The NFe is not legally authorized. It may not have been issued or has been canceled.
                 * `ACCESS_KEY_DUPLICATE`: The access key already exists. You cannot upload an invoice with duplicate access
                key.
                 * `CNPJ_NOT_MATCH`：Ensure the NF-e has the same 8-digit prefix as the CNPJ you provided during onboarding.
                 * `UF_Inconsistent_Required`: NF-e validation failed: The CNPJ used to issue the NF-e is registered in a
                different state from your warehouse.
                 * `UF_Inconsistent_Dismisse_Retirada_missing`: NF-e validation failed: The CNPJ used to issue the NF-e is
                registered in a different state from your warehouse. To issue a valid NF-e with this CNPJ, include warehouse
                information (Pickup Location Identification) in your NF-e.
                 * `UF_Inconsistent_Dismissed_Retirada_Inconsistent`: The CNPJ used to issue the NF-e is registered in a
                different state from your warehouse. To issue a valid NF-e with this CNPJ, include warehouse information (Pickup
                Location Identification) in your NF-e.
     """

    package_id: str | Unset = UNSET
    order_ids: list[str] | Unset = UNSET
    invoice_status: str | Unset = UNSET
    invalid_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        package_id = self.package_id

        order_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_ids, Unset):
            order_ids = self.order_ids



        invoice_status = self.invoice_status

        invalid_reason = self.invalid_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if order_ids is not UNSET:
            field_dict["order_ids"] = order_ids
        if invoice_status is not UNSET:
            field_dict["invoice_status"] = invoice_status
        if invalid_reason is not UNSET:
            field_dict["invalid_reason"] = invalid_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_id = d.pop("package_id", UNSET)

        order_ids = cast(list[str], d.pop("order_ids", UNSET))


        invoice_status = d.pop("invoice_status", UNSET)

        invalid_reason = d.pop("invalid_reason", UNSET)

        invoice_status_change_webhook_data = cls(
            package_id=package_id,
            order_ids=order_ids,
            invoice_status=invoice_status,
            invalid_reason=invalid_reason,
        )


        invoice_status_change_webhook_data.additional_properties = d
        return invoice_status_change_webhook_data

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
