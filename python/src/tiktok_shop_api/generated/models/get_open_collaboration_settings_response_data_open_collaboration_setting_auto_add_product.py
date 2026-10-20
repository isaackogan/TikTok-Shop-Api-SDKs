from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetOpenCollaborationSettingsResponseDataOpenCollaborationSettingAutoAddProduct")



@_attrs_define
class GetOpenCollaborationSettingsResponseDataOpenCollaborationSettingAutoAddProduct:
    """ 
        Attributes:
            enable (bool | Unset): - true: The seller can add existing non-affiliate products to open collaboration at one
                time, and future products will also be added automatically.
                - false: Future products will not be added to open collaboration automatically, but existing products' open
                collaboration will not be reverted.
            commission_rate (int | Unset): The default commission rate of open collaboration created for the auto-added
                products.
                The unit is 0.01%. For example, to set the default commission rate to 10%, set the value to `1000`. If so, if
                the price of a product is $50 USD, the creator would receive $5 USD for every piece of product sold.
                The range is `[100, 8000]`.
                When enable=false, this field will not be returned.
     """

    enable: bool | Unset = UNSET
    commission_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        commission_rate = self.commission_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if enable is not UNSET:
            field_dict["enable"] = enable
        if commission_rate is not UNSET:
            field_dict["commission_rate"] = commission_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        commission_rate = d.pop("commission_rate", UNSET)

        get_open_collaboration_settings_response_data_open_collaboration_setting_auto_add_product = cls(
            enable=enable,
            commission_rate=commission_rate,
        )


        get_open_collaboration_settings_response_data_open_collaboration_setting_auto_add_product.additional_properties = d
        return get_open_collaboration_settings_response_data_open_collaboration_setting_auto_add_product

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
