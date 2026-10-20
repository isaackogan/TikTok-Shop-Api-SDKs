from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductResponseDataSkuStatusInfo")



@_attrs_define
class GetProductResponseDataSkuStatusInfo:
    """ 
        Attributes:
            deactivation_source (str | Unset): The deactivation source of the SKU with `DEACTIVATED` status.
                Possible values:
                - SELLER: Indicates that the seller deactivated the SKU
                - PLATFORM: Indicates that the platform de-activated the SKU due to violation reasons
                - COMBO_RELATION: Indicates that the platform de-activated the bundle-SKU due to the deactivation of sub-SKU.
            status (str | Unset): The SKU status in TikTok Shop.
                Possible values:
                - NORMAL
                - DEACTIVATED
     """

    deactivation_source: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        deactivation_source = self.deactivation_source

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if deactivation_source is not UNSET:
            field_dict["deactivation_source"] = deactivation_source
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deactivation_source = d.pop("deactivation_source", UNSET)

        status = d.pop("status", UNSET)

        get_product_response_data_sku_status_info = cls(
            deactivation_source=deactivation_source,
            status=status,
        )


        get_product_response_data_sku_status_info.additional_properties = d
        return get_product_response_data_sku_status_info

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
