from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.shipping_info_list import ShippingInfoList


T = TypeVar("T", bound="UpdatePackageShippingInfoRequest")


@_attrs_define
class UpdatePackageShippingInfoRequest:
    """
    Attributes:
        shipping_info_list (list[ShippingInfoList]): "Only supports uploading multiple tracking numbers for split-
            shipment in 3PL single item scenarios (non-virtual bundle) (This function is only support for whitelist sellers；
            If you are not on the allowlist, it is recommended to contact AM to apply)
            For other scenarios, only one tracking number can be uploaded at a time."
    """

    shipping_info_list: list[ShippingInfoList]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipping_info_list = []
        for shipping_info_list_item_data in self.shipping_info_list:
            shipping_info_list_item = shipping_info_list_item_data.to_dict()
            shipping_info_list.append(shipping_info_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipping_info_list": shipping_info_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shipping_info_list import ShippingInfoList  # noqa: PLC0415

        d = dict(src_dict)
        shipping_info_list = []
        _shipping_info_list = d.pop("shipping_info_list")
        for shipping_info_list_item_data in _shipping_info_list:
            shipping_info_list_item = ShippingInfoList.from_dict(shipping_info_list_item_data)

            shipping_info_list.append(shipping_info_list_item)

        update_package_shipping_info_request = cls(
            shipping_info_list=shipping_info_list,
        )

        update_package_shipping_info_request.additional_properties = d
        return update_package_shipping_info_request

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
