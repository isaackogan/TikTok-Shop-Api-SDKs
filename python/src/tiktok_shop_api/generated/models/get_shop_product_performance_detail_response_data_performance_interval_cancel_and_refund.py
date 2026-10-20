from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceIntervalCancelAndRefund")


@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceIntervalCancelAndRefund:
    """
    Attributes:
        returned (int | Unset): Returned refers to units that were returned and refunded.
        canceled (int | Unset): Canceled refers to units included in orders that were either "Unpaid" or "Awaiting
            Shipment."
        refunded (int | Unset): Refunded refers to units that were refunded but not returned.
        replacements (int | Unset): Replacements refers to units that were returned and replaced.
    """

    returned: int | Unset = UNSET
    canceled: int | Unset = UNSET
    refunded: int | Unset = UNSET
    replacements: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        returned = self.returned

        canceled = self.canceled

        refunded = self.refunded

        replacements = self.replacements

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if returned is not UNSET:
            field_dict["returned"] = returned
        if canceled is not UNSET:
            field_dict["canceled"] = canceled
        if refunded is not UNSET:
            field_dict["refunded"] = refunded
        if replacements is not UNSET:
            field_dict["replacements"] = replacements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        returned = d.pop("returned", UNSET)

        canceled = d.pop("canceled", UNSET)

        refunded = d.pop("refunded", UNSET)

        replacements = d.pop("replacements", UNSET)

        get_shop_product_performance_detail_response_data_performance_interval_cancel_and_refund = cls(
            returned=returned,
            canceled=canceled,
            refunded=refunded,
            replacements=replacements,
        )

        get_shop_product_performance_detail_response_data_performance_interval_cancel_and_refund.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_interval_cancel_and_refund

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
