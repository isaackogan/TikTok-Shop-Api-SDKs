from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClickToOrderRate")


@_attrs_define
class ClickToOrderRate:
    """
    Attributes:
        sku_order_ctor (str | Unset): The percentage of times viewers clicked product links in LIVE streams and placed a
            direct order.
        main_order_ctor (str | Unset): Percentage of times viewers who clicked LIVE product links also placed a main
            order.
    """

    sku_order_ctor: str | Unset = UNSET
    main_order_ctor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sku_order_ctor = self.sku_order_ctor

        main_order_ctor = self.main_order_ctor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_order_ctor is not UNSET:
            field_dict["sku_order_ctor"] = sku_order_ctor
        if main_order_ctor is not UNSET:
            field_dict["main_order_ctor"] = main_order_ctor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sku_order_ctor = d.pop("sku_order_ctor", UNSET)

        main_order_ctor = d.pop("main_order_ctor", UNSET)

        click_to_order_rate = cls(
            sku_order_ctor=sku_order_ctor,
            main_order_ctor=main_order_ctor,
        )

        click_to_order_rate.additional_properties = d
        return click_to_order_rate

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
