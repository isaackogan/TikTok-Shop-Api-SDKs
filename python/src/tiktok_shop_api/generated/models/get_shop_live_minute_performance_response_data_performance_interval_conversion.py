from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avg_price import AvgPrice
    from ..models.click_to_order_rate import ClickToOrderRate
    from ..models.get_shop_live_minute_performance_response_data_performance_interval_conversion_gpm import (
        GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversionGpm,
    )


T = TypeVar("T", bound="GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversion")


@_attrs_define
class GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversion:
    """
    Attributes:
        avg_price (AvgPrice | Unset):
        click_to_order_rate (ClickToOrderRate | Unset):
        gpm (GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversionGpm | Unset):
        created_sku_orders (int | Unset): The number of SKU orders created by users from the LIVE
        sku_order_rate (str | Unset): Number of SKU orders from the LIVE divided by the impressions of the LIVE
    """

    avg_price: AvgPrice | Unset = UNSET
    click_to_order_rate: ClickToOrderRate | Unset = UNSET
    gpm: GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversionGpm | Unset = UNSET
    created_sku_orders: int | Unset = UNSET
    sku_order_rate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_price, Unset):
            avg_price = self.avg_price.to_dict()

        click_to_order_rate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.click_to_order_rate, Unset):
            click_to_order_rate = self.click_to_order_rate.to_dict()

        gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpm, Unset):
            gpm = self.gpm.to_dict()

        created_sku_orders = self.created_sku_orders

        sku_order_rate = self.sku_order_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_price is not UNSET:
            field_dict["avg_price"] = avg_price
        if click_to_order_rate is not UNSET:
            field_dict["click_to_order_rate"] = click_to_order_rate
        if gpm is not UNSET:
            field_dict["gpm"] = gpm
        if created_sku_orders is not UNSET:
            field_dict["created_sku_orders"] = created_sku_orders
        if sku_order_rate is not UNSET:
            field_dict["sku_order_rate"] = sku_order_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avg_price import AvgPrice  # noqa: PLC0415
        from ..models.click_to_order_rate import ClickToOrderRate  # noqa: PLC0415
        from ..models.get_shop_live_minute_performance_response_data_performance_interval_conversion_gpm import (
            GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversionGpm,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _avg_price = d.pop("avg_price", UNSET)
        avg_price: AvgPrice | Unset
        if isinstance(_avg_price, Unset):
            avg_price = UNSET
        else:
            avg_price = AvgPrice.from_dict(_avg_price)

        _click_to_order_rate = d.pop("click_to_order_rate", UNSET)
        click_to_order_rate: ClickToOrderRate | Unset
        if isinstance(_click_to_order_rate, Unset):
            click_to_order_rate = UNSET
        else:
            click_to_order_rate = ClickToOrderRate.from_dict(_click_to_order_rate)

        _gpm = d.pop("gpm", UNSET)
        gpm: GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversionGpm | Unset
        if isinstance(_gpm, Unset):
            gpm = UNSET
        else:
            gpm = GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversionGpm.from_dict(_gpm)

        created_sku_orders = d.pop("created_sku_orders", UNSET)

        sku_order_rate = d.pop("sku_order_rate", UNSET)

        get_shop_live_minute_performance_response_data_performance_interval_conversion = cls(
            avg_price=avg_price,
            click_to_order_rate=click_to_order_rate,
            gpm=gpm,
            created_sku_orders=created_sku_orders,
            sku_order_rate=sku_order_rate,
        )

        get_shop_live_minute_performance_response_data_performance_interval_conversion.additional_properties = d
        return get_shop_live_minute_performance_response_data_performance_interval_conversion

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
