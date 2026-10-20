from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.shelf_life_attribute_info_handling_method_expired_goods import (
    ShelfLifeAttributeInfoHandlingMethodExpiredGoods,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShelfLifeAttributeInfo")


@_attrs_define
class ShelfLifeAttributeInfo:
    """
    Attributes:
        inbound_cutoff_days (int): The goods inbound cutoff days before expiration, represent the time period before the
            product's expiration when the warehouse will no longer accept inbound shipments.
        expiration_alert_days (int): The goods alert days before expired, represent the period of time before platform
            send expiration reminder alerts to the merchant.
        sales_cutoff_days (int): The goods sales cut off days before expired, represent the period of time before
            expiration in which the goods will no longer be available for sale.
        shelf_life (int | Unset): The goods shelf life (days)
        handling_method_expired_goods (ShelfLifeAttributeInfoHandlingMethodExpiredGoods | Unset): How expired inventory
            is handled.
            Possible values:
            - `STORE_UNITS`: Move the units to defective inventory.
            - `RETURN_TO_SELLER`: Return the units to the seller.
            - `DISPOSE`: Dispose of the units.
    """

    inbound_cutoff_days: int
    expiration_alert_days: int
    sales_cutoff_days: int
    shelf_life: int | Unset = UNSET
    handling_method_expired_goods: ShelfLifeAttributeInfoHandlingMethodExpiredGoods | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound_cutoff_days = self.inbound_cutoff_days

        expiration_alert_days = self.expiration_alert_days

        sales_cutoff_days = self.sales_cutoff_days

        shelf_life = self.shelf_life

        handling_method_expired_goods: str | Unset = UNSET
        if not isinstance(self.handling_method_expired_goods, Unset):
            handling_method_expired_goods = self.handling_method_expired_goods.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inbound_cutoff_days": inbound_cutoff_days,
                "expiration_alert_days": expiration_alert_days,
                "sales_cutoff_days": sales_cutoff_days,
            }
        )
        if shelf_life is not UNSET:
            field_dict["shelf_life"] = shelf_life
        if handling_method_expired_goods is not UNSET:
            field_dict["handling_method_expired_goods"] = handling_method_expired_goods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inbound_cutoff_days = d.pop("inbound_cutoff_days")

        expiration_alert_days = d.pop("expiration_alert_days")

        sales_cutoff_days = d.pop("sales_cutoff_days")

        shelf_life = d.pop("shelf_life", UNSET)

        _handling_method_expired_goods = d.pop("handling_method_expired_goods", UNSET)
        handling_method_expired_goods: ShelfLifeAttributeInfoHandlingMethodExpiredGoods | Unset
        if isinstance(_handling_method_expired_goods, Unset):
            handling_method_expired_goods = UNSET
        else:
            handling_method_expired_goods = ShelfLifeAttributeInfoHandlingMethodExpiredGoods(
                _handling_method_expired_goods
            )

        shelf_life_attribute_info = cls(
            inbound_cutoff_days=inbound_cutoff_days,
            expiration_alert_days=expiration_alert_days,
            sales_cutoff_days=sales_cutoff_days,
            shelf_life=shelf_life,
            handling_method_expired_goods=handling_method_expired_goods,
        )

        shelf_life_attribute_info.additional_properties = d
        return shelf_life_attribute_info

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
