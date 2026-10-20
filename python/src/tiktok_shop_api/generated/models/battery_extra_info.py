from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.battery_extra_info_battery_packaging_type import BatteryExtraInfoBatteryPackagingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatteryExtraInfo")


@_attrs_define
class BatteryExtraInfo:
    """
    Attributes:
        battery_type (str): Battery type
            Possible values:
            LITHIUM_ION
            LITHIUM_METAL
            OTHER
        battery_packaging_type (BatteryExtraInfoBatteryPackagingType): Battery packaging type.
            Possible values:
            - STANDALONE
            - IN_EQUIPMENT
            - WITH_EQUIPMENT
            - OTHER
        total_battery_weight (str): Total battery weight in the unit specified by total_battery_weight_unit.
        total_battery_weight_unit (str): Unit for total_battery_weight. Possible value: GRAM.
        total_battery_capacity (str): Total battery capacity in the unit specified by total_battery_capacity_unit.
        total_battery_capacity_unit (str): Unit for total_battery_capacity, such as WATTHOUR.
        is_need_un_38_3_test (bool): UN38.3 testing ensures that batteries meet specific safety criteria. Please send
            the report in the field if it's not included in the MSDS.
        un_38_3_test_file_url (str | Unset): UN38.3 testing file URL
        battery_count_per_package (str | Unset): per package battery count
    """

    battery_type: str
    battery_packaging_type: BatteryExtraInfoBatteryPackagingType
    total_battery_weight: str
    total_battery_weight_unit: str
    total_battery_capacity: str
    total_battery_capacity_unit: str
    is_need_un_38_3_test: bool
    un_38_3_test_file_url: str | Unset = UNSET
    battery_count_per_package: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        battery_type = self.battery_type

        battery_packaging_type = self.battery_packaging_type.value

        total_battery_weight = self.total_battery_weight

        total_battery_weight_unit = self.total_battery_weight_unit

        total_battery_capacity = self.total_battery_capacity

        total_battery_capacity_unit = self.total_battery_capacity_unit

        is_need_un_38_3_test = self.is_need_un_38_3_test

        un_38_3_test_file_url = self.un_38_3_test_file_url

        battery_count_per_package = self.battery_count_per_package

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "battery_type": battery_type,
                "battery_packaging_type": battery_packaging_type,
                "total_battery_weight": total_battery_weight,
                "total_battery_weight_unit": total_battery_weight_unit,
                "total_battery_capacity": total_battery_capacity,
                "total_battery_capacity_unit": total_battery_capacity_unit,
                "is_need_un_38_3_test": is_need_un_38_3_test,
            }
        )
        if un_38_3_test_file_url is not UNSET:
            field_dict["un_38_3_test_file_url"] = un_38_3_test_file_url
        if battery_count_per_package is not UNSET:
            field_dict["battery_count_per_package"] = battery_count_per_package

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        battery_type = d.pop("battery_type")

        battery_packaging_type = BatteryExtraInfoBatteryPackagingType(d.pop("battery_packaging_type"))

        total_battery_weight = d.pop("total_battery_weight")

        total_battery_weight_unit = d.pop("total_battery_weight_unit")

        total_battery_capacity = d.pop("total_battery_capacity")

        total_battery_capacity_unit = d.pop("total_battery_capacity_unit")

        is_need_un_38_3_test = d.pop("is_need_un_38_3_test")

        un_38_3_test_file_url = d.pop("un_38_3_test_file_url", UNSET)

        battery_count_per_package = d.pop("battery_count_per_package", UNSET)

        battery_extra_info = cls(
            battery_type=battery_type,
            battery_packaging_type=battery_packaging_type,
            total_battery_weight=total_battery_weight,
            total_battery_weight_unit=total_battery_weight_unit,
            total_battery_capacity=total_battery_capacity,
            total_battery_capacity_unit=total_battery_capacity_unit,
            is_need_un_38_3_test=is_need_un_38_3_test,
            un_38_3_test_file_url=un_38_3_test_file_url,
            battery_count_per_package=battery_count_per_package,
        )

        battery_extra_info.additional_properties = d
        return battery_extra_info

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
