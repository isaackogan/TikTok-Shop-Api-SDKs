from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_package_delivery_status_request_package_delivery_type import UpdatePackageDeliveryStatusRequestPackageDeliveryType
from ..models.update_package_delivery_status_request_package_fail_delivery_reason import UpdatePackageDeliveryStatusRequestPackageFailDeliveryReason
from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdatePackageDeliveryStatusRequestPackage")



@_attrs_define
class UpdatePackageDeliveryStatusRequestPackage:
    """ 
        Attributes:
            id (str): The package ID.
            delivery_type (UpdatePackageDeliveryStatusRequestPackageDeliveryType): Delivery status of the package.
                Possible values for in-store pick up:
                - `DELIVERY_SUCCESS`: The package has been successfully delivered.
                Possible values for SOF (Seller Own Fleet):
                 - `DELIVERY_SUCCESS`: The package has been successfully delivered.
                 - `DELIVERY_FAILED`: The package could not be delivered successfully.
                 - `UPDATE_POD`: Updates the attachment for a package that has already been delivered.
            fail_delivery_reason (UpdatePackageDeliveryStatusRequestPackageFailDeliveryReason | Unset): Delivery failure
                reasons.

                When `delivery_type = DELIVERY_FAILED`, this field is required. For other delivery types, this field is not
                required.

                Possible values:
                - `INVALID_ADDRESS`: The buyer shipping address is invalid.
                - `UNABLE_RECEIVE`: The buyer is currently unable to receive the delivery.
                - `UNABLE_CONTACT_BUYER`: Unable to contact the buyer.
                - `BUYER_REFUSED`: The buyer has refused to receive the product.
                - `DELAY_DELIVERY`: Delay in delivery.
                - `PACKAGE_LOST`: The package is lost.
                - `PACKAGE_DAMAGE`: The package is damaged.
                - `FORCE_MAJEURE`: An unforeseeable event of force majeure has occurred.
                - `OTHER`: Other reason.
            file_type (str | Unset): Attachment type:
                - `IMG`
                - `PDF`
            file_url (str | Unset): Attachment URL.
                The seller can use the [Upload Delivery File](https://partner.tiktokshop.com/docv2/page/650aa6e04a0bb702c06dcd34
                ?external_id=650aa6e04a0bb702c06dcd34#Back%20To%20Top) and [Upload Delivery
                Image](https://partner.tiktokshop.com/docv2/page/650aa70d0fcef602bf32772f?external_id=650aa70d0fcef602bf32772f)
                APIs to generate the URL. The attachment will be used by TikTok Shop to verify the package delivery.
            verification_code (str | Unset): The verification code required for order pickup.
     """

    id: str
    delivery_type: UpdatePackageDeliveryStatusRequestPackageDeliveryType
    fail_delivery_reason: UpdatePackageDeliveryStatusRequestPackageFailDeliveryReason | Unset = UNSET
    file_type: str | Unset = UNSET
    file_url: str | Unset = UNSET
    verification_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        delivery_type = self.delivery_type.value

        fail_delivery_reason: str | Unset = UNSET
        if not isinstance(self.fail_delivery_reason, Unset):
            fail_delivery_reason = self.fail_delivery_reason.value


        file_type = self.file_type

        file_url = self.file_url

        verification_code = self.verification_code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "delivery_type": delivery_type,
        })
        if fail_delivery_reason is not UNSET:
            field_dict["fail_delivery_reason"] = fail_delivery_reason
        if file_type is not UNSET:
            field_dict["file_type"] = file_type
        if file_url is not UNSET:
            field_dict["file_url"] = file_url
        if verification_code is not UNSET:
            field_dict["verification_code"] = verification_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        delivery_type = UpdatePackageDeliveryStatusRequestPackageDeliveryType(d.pop("delivery_type"))




        _fail_delivery_reason = d.pop("fail_delivery_reason", UNSET)
        fail_delivery_reason: UpdatePackageDeliveryStatusRequestPackageFailDeliveryReason | Unset
        if isinstance(_fail_delivery_reason,  Unset):
            fail_delivery_reason = UNSET
        else:
            fail_delivery_reason = UpdatePackageDeliveryStatusRequestPackageFailDeliveryReason(_fail_delivery_reason)




        file_type = d.pop("file_type", UNSET)

        file_url = d.pop("file_url", UNSET)

        verification_code = d.pop("verification_code", UNSET)

        update_package_delivery_status_request_package = cls(
            id=id,
            delivery_type=delivery_type,
            fail_delivery_reason=fail_delivery_reason,
            file_type=file_type,
            file_url=file_url,
            verification_code=verification_code,
        )


        update_package_delivery_status_request_package.additional_properties = d
        return update_package_delivery_status_request_package

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
