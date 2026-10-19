from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_goods_info_response_data_good_lot_expiration_info_handling_method import (
    SearchGoodsInfoResponseDataGoodLotExpirationInfoHandlingMethod,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchGoodsInfoResponseDataGoodLotExpirationInfo")


@_attrs_define
class SearchGoodsInfoResponseDataGoodLotExpirationInfo:
    """
    Attributes:
        is_lot_control (bool | Unset): A flag indicating whether the goods is under lot control.
            True: Under lot control.
            False: Not under lot control.
            Note: Lot code and expiration date management information is mandatory for these [product
            categories](https://bytedance.us.larkoffice.com/sheets/OoT2sKH7jhykXCtHEseuzkGYsod) according to Fulfilled by
            TikTok guidelines.
        is_expiration_management (bool | Unset): A flag indicating whether the goods is under expiration managment.
            True: Under expiration managment.
            False: Not under expiration managment.
        shelf_life_days (int | Unset): The goods shelf life days input by merchant, represent the total number of days
            the product remains usable or sellable from the time it is manufactured until its expiration.
        inbound_cutoff_days (int | Unset): The goods inbound cutoff days before expiration, represent the time period
            before the product's expiration when the warehouse will no longer accept inbound shipments.
        expiration_alert_days (int | Unset): The goods alert days before expired, represent the period of time before
            platform send expiration reminder alerts to the merchant.
        sales_cutoff_days (int | Unset): The goods sales cut off days before expired, represent the period of time
            before expiration in which the goods will no longer be available for sale.
        handling_method (SearchGoodsInfoResponseDataGoodLotExpirationInfoHandlingMethod | Unset): The handling method
            for expired inventory.
            Possible values:
            - `STORE_UNITS`: Move the units to defective inventory.
            - `RETURN_TO_SELLER`: Return the units to the seller.
            - `DISPOSE`: Dispose of the units.
    """

    is_lot_control: bool | Unset = UNSET
    is_expiration_management: bool | Unset = UNSET
    shelf_life_days: int | Unset = UNSET
    inbound_cutoff_days: int | Unset = UNSET
    expiration_alert_days: int | Unset = UNSET
    sales_cutoff_days: int | Unset = UNSET
    handling_method: SearchGoodsInfoResponseDataGoodLotExpirationInfoHandlingMethod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_lot_control = self.is_lot_control

        is_expiration_management = self.is_expiration_management

        shelf_life_days = self.shelf_life_days

        inbound_cutoff_days = self.inbound_cutoff_days

        expiration_alert_days = self.expiration_alert_days

        sales_cutoff_days = self.sales_cutoff_days

        handling_method: str | Unset = UNSET
        if not isinstance(self.handling_method, Unset):
            handling_method = self.handling_method.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_lot_control is not UNSET:
            field_dict["is_lot_control"] = is_lot_control
        if is_expiration_management is not UNSET:
            field_dict["is_expiration_management"] = is_expiration_management
        if shelf_life_days is not UNSET:
            field_dict["shelf_life_days"] = shelf_life_days
        if inbound_cutoff_days is not UNSET:
            field_dict["inbound_cutoff_days"] = inbound_cutoff_days
        if expiration_alert_days is not UNSET:
            field_dict["expiration_alert_days"] = expiration_alert_days
        if sales_cutoff_days is not UNSET:
            field_dict["sales_cutoff_days"] = sales_cutoff_days
        if handling_method is not UNSET:
            field_dict["handling_method"] = handling_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_lot_control = d.pop("is_lot_control", UNSET)

        is_expiration_management = d.pop("is_expiration_management", UNSET)

        shelf_life_days = d.pop("shelf_life_days", UNSET)

        inbound_cutoff_days = d.pop("inbound_cutoff_days", UNSET)

        expiration_alert_days = d.pop("expiration_alert_days", UNSET)

        sales_cutoff_days = d.pop("sales_cutoff_days", UNSET)

        _handling_method = d.pop("handling_method", UNSET)
        handling_method: SearchGoodsInfoResponseDataGoodLotExpirationInfoHandlingMethod | Unset
        if isinstance(_handling_method, Unset):
            handling_method = UNSET
        else:
            handling_method = SearchGoodsInfoResponseDataGoodLotExpirationInfoHandlingMethod(_handling_method)

        search_goods_info_response_data_good_lot_expiration_info = cls(
            is_lot_control=is_lot_control,
            is_expiration_management=is_expiration_management,
            shelf_life_days=shelf_life_days,
            inbound_cutoff_days=inbound_cutoff_days,
            expiration_alert_days=expiration_alert_days,
            sales_cutoff_days=sales_cutoff_days,
            handling_method=handling_method,
        )

        search_goods_info_response_data_good_lot_expiration_info.additional_properties = d
        return search_goods_info_response_data_good_lot_expiration_info

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
