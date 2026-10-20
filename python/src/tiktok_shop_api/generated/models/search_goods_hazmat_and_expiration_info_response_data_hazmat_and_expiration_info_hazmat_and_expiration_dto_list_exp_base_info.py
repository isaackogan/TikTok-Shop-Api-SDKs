from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfoHazmatAndExpirationDtoListExpBaseInfo",
)


@_attrs_define
class SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfoHazmatAndExpirationDtoListExpBaseInfo:
    """
    Attributes:
        inbound_cutoff_days (int | Unset): The period before a product's expiration date when the warehouse will stop
            accepting inbound shipments.For example, if the product expiration date is December 1, 2024, and the inbound
            cutoff days are 20 days, then the warehouse will stop accepting inbound shipments for this product after
            November 11, 2024 (20 days before expiration)
        expiration_alert_days (int | Unset): The period of time before expiration in which the platform will send
            expiration alerts.
        sales_cutoff_days (int | Unset): The period before a product's expiration date when the inventory will no longer
            be available for sale. For example, if the product expiration date is December 1, 2024, and the sales cutoff
            days are 20 days, then the inventory will stop being available for sale after November 11, 2024 (20 days before
            expiration).
    """

    inbound_cutoff_days: int | Unset = UNSET
    expiration_alert_days: int | Unset = UNSET
    sales_cutoff_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound_cutoff_days = self.inbound_cutoff_days

        expiration_alert_days = self.expiration_alert_days

        sales_cutoff_days = self.sales_cutoff_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound_cutoff_days is not UNSET:
            field_dict["inbound_cutoff_days"] = inbound_cutoff_days
        if expiration_alert_days is not UNSET:
            field_dict["expiration_alert_days"] = expiration_alert_days
        if sales_cutoff_days is not UNSET:
            field_dict["sales_cutoff_days"] = sales_cutoff_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inbound_cutoff_days = d.pop("inbound_cutoff_days", UNSET)

        expiration_alert_days = d.pop("expiration_alert_days", UNSET)

        sales_cutoff_days = d.pop("sales_cutoff_days", UNSET)

        search_goods_hazmat_and_expiration_info_response_data_hazmat_and_expiration_info_hazmat_and_expiration_dto_list_exp_base_info = cls(
            inbound_cutoff_days=inbound_cutoff_days,
            expiration_alert_days=expiration_alert_days,
            sales_cutoff_days=sales_cutoff_days,
        )

        search_goods_hazmat_and_expiration_info_response_data_hazmat_and_expiration_info_hazmat_and_expiration_dto_list_exp_base_info.additional_properties = d
        return search_goods_hazmat_and_expiration_info_response_data_hazmat_and_expiration_info_hazmat_and_expiration_dto_list_exp_base_info

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
