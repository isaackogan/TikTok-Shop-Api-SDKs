from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_goods_info_response_data_good_hazmat_info_battery_extra_info_battery_packaging_type import (
    SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfoBatteryPackagingType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfo")


@_attrs_define
class SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfo:
    """
    Attributes:
        battery_type (str | Unset): Battery type
            Possible values:
            LITHIUM_ION
            LITHIUM_METAL
            OTHER
        battery_packaging_type (SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfoBatteryPackagingType | Unset):
            Battery packaging type.
            Possible values:
            - STANDALONE
            - IN_EQUIPMENT
            - WITH_EQUIPMENT
            - OTHER
        total_battery_weight (str | Unset): Total battery weight in the unit specified by total_battery_weight_unit.
        total_battery_weight_unit (str | Unset): Unit for total_battery_weight. Possible value: GRAM.
        total_battery_capacity (str | Unset): Total battery capacity in the unit specified by
            total_battery_capacity_unit.
        battery_count_per_package (str | Unset): per package battery count
        is_need_un_38_3_test (bool | Unset): UN38.3 testing ensures that batteries meet specific safety criteria. Please
            send the report in the field if it's not included in the MSDS.
        un_38_3_test_file_url (str | Unset): UN38.3 testing file URL
        total_battery_capacity_unit (str | Unset): Unit for `total_battery_capacity`, such as `WATT_HOURS`.
    """

    battery_type: str | Unset = UNSET
    battery_packaging_type: SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfoBatteryPackagingType | Unset = (
        UNSET
    )
    total_battery_weight: str | Unset = UNSET
    total_battery_weight_unit: str | Unset = UNSET
    total_battery_capacity: str | Unset = UNSET
    battery_count_per_package: str | Unset = UNSET
    is_need_un_38_3_test: bool | Unset = UNSET
    un_38_3_test_file_url: str | Unset = UNSET
    total_battery_capacity_unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        battery_type = self.battery_type

        battery_packaging_type: str | Unset = UNSET
        if not isinstance(self.battery_packaging_type, Unset):
            battery_packaging_type = self.battery_packaging_type.value

        total_battery_weight = self.total_battery_weight

        total_battery_weight_unit = self.total_battery_weight_unit

        total_battery_capacity = self.total_battery_capacity

        battery_count_per_package = self.battery_count_per_package

        is_need_un_38_3_test = self.is_need_un_38_3_test

        un_38_3_test_file_url = self.un_38_3_test_file_url

        total_battery_capacity_unit = self.total_battery_capacity_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if battery_type is not UNSET:
            field_dict["battery_type"] = battery_type
        if battery_packaging_type is not UNSET:
            field_dict["battery_packaging_type"] = battery_packaging_type
        if total_battery_weight is not UNSET:
            field_dict["total_battery_weight"] = total_battery_weight
        if total_battery_weight_unit is not UNSET:
            field_dict["total_battery_weight_unit"] = total_battery_weight_unit
        if total_battery_capacity is not UNSET:
            field_dict["total_battery_capacity"] = total_battery_capacity
        if battery_count_per_package is not UNSET:
            field_dict["battery_count_per_package"] = battery_count_per_package
        if is_need_un_38_3_test is not UNSET:
            field_dict["is_need_un_38_3_test"] = is_need_un_38_3_test
        if un_38_3_test_file_url is not UNSET:
            field_dict["un_38_3_test_file_url"] = un_38_3_test_file_url
        if total_battery_capacity_unit is not UNSET:
            field_dict["total_battery_capacity_unit"] = total_battery_capacity_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        battery_type = d.pop("battery_type", UNSET)

        _battery_packaging_type = d.pop("battery_packaging_type", UNSET)
        battery_packaging_type: SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfoBatteryPackagingType | Unset
        if isinstance(_battery_packaging_type, Unset):
            battery_packaging_type = UNSET
        else:
            battery_packaging_type = SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfoBatteryPackagingType(
                _battery_packaging_type
            )

        total_battery_weight = d.pop("total_battery_weight", UNSET)

        total_battery_weight_unit = d.pop("total_battery_weight_unit", UNSET)

        total_battery_capacity = d.pop("total_battery_capacity", UNSET)

        battery_count_per_package = d.pop("battery_count_per_package", UNSET)

        is_need_un_38_3_test = d.pop("is_need_un_38_3_test", UNSET)

        un_38_3_test_file_url = d.pop("un_38_3_test_file_url", UNSET)

        total_battery_capacity_unit = d.pop("total_battery_capacity_unit", UNSET)

        search_goods_info_response_data_good_hazmat_info_battery_extra_info = cls(
            battery_type=battery_type,
            battery_packaging_type=battery_packaging_type,
            total_battery_weight=total_battery_weight,
            total_battery_weight_unit=total_battery_weight_unit,
            total_battery_capacity=total_battery_capacity,
            battery_count_per_package=battery_count_per_package,
            is_need_un_38_3_test=is_need_un_38_3_test,
            un_38_3_test_file_url=un_38_3_test_file_url,
            total_battery_capacity_unit=total_battery_capacity_unit,
        )

        search_goods_info_response_data_good_hazmat_info_battery_extra_info.additional_properties = d
        return search_goods_info_response_data_good_hazmat_info_battery_extra_info

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
