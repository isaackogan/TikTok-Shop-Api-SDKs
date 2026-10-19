from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gmv import Gmv


T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdownSale")


@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdownSale:
    """
    Attributes:
        gmv (Gmv | Unset):
        items_sold (int | Unset): Number of items sold in the corresponding content type.
        avg_customers (int | Unset): Daily average count of customers.
    """

    gmv: Gmv | Unset = UNSET
    items_sold: int | Unset = UNSET
    avg_customers: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        items_sold = self.items_sold

        avg_customers = self.avg_customers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if avg_customers is not UNSET:
            field_dict["avg_customers"] = avg_customers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv  # noqa: PLC0415

        d = dict(src_dict)
        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv, Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)

        items_sold = d.pop("items_sold", UNSET)

        avg_customers = d.pop("avg_customers", UNSET)

        get_shop_product_performance_detail_response_data_performance_interval_sale_breakdown_sale = cls(
            gmv=gmv,
            items_sold=items_sold,
            avg_customers=avg_customers,
        )

        get_shop_product_performance_detail_response_data_performance_interval_sale_breakdown_sale.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_interval_sale_breakdown_sale

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
