from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hazmat_info_dg_class import HazmatInfoDgClass
from ..models.hazmat_info_dg_uncode import HazmatInfoDgUncode
from ..models.hazmat_info_hazmat_type import HazmatInfoHazmatType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aerosol_extra_info import AerosolExtraInfo
    from ..models.battery_extra_info import BatteryExtraInfo
    from ..models.flammable_liquids_extra_info import FlammableLiquidsExtraInfo


T = TypeVar("T", bound="HazmatInfo")


@_attrs_define
class HazmatInfo:
    """
    Attributes:
        hazmat_type (HazmatInfoHazmatType): hazardous goods type
            Possible values:
            -MAGNETIZED
            -BATTERY
            -FLAMMABLE_LIQUID
            -AEROSOLS
        dg_class (HazmatInfoDgClass): Hazmat class
            Possible values:
            -CLASS_2
            -CLASS_3
            -CLASS_9
        dg_uncode (HazmatInfoDgUncode): UN identifier for the hazardous substance. Standard UN values use the `UN`
            prefix followed by four digits; `OTHER` is also supported.
            Possible values:
            - UN2807
            - UN3480
            - UN3090
            - UN3481
            - UN3091
            - UN1263
            - UN1266
            - UN3065
            - OTHER
        msds_file_url (str): Material safety data sheet of the hazmat goods to support review the goods' safety
            compliance in FBT
        battery_extra_info (BatteryExtraInfo | Unset):
        flammable_liquids_extra_info (FlammableLiquidsExtraInfo | Unset):
        aerosol_extra_info (AerosolExtraInfo | Unset):
    """

    hazmat_type: HazmatInfoHazmatType
    dg_class: HazmatInfoDgClass
    dg_uncode: HazmatInfoDgUncode
    msds_file_url: str
    battery_extra_info: BatteryExtraInfo | Unset = UNSET
    flammable_liquids_extra_info: FlammableLiquidsExtraInfo | Unset = UNSET
    aerosol_extra_info: AerosolExtraInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hazmat_type = self.hazmat_type.value

        dg_class = self.dg_class.value

        dg_uncode = self.dg_uncode.value

        msds_file_url = self.msds_file_url

        battery_extra_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.battery_extra_info, Unset):
            battery_extra_info = self.battery_extra_info.to_dict()

        flammable_liquids_extra_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flammable_liquids_extra_info, Unset):
            flammable_liquids_extra_info = self.flammable_liquids_extra_info.to_dict()

        aerosol_extra_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aerosol_extra_info, Unset):
            aerosol_extra_info = self.aerosol_extra_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hazmat_type": hazmat_type,
                "dg_class": dg_class,
                "dg_uncode": dg_uncode,
                "msds_file_url": msds_file_url,
            }
        )
        if battery_extra_info is not UNSET:
            field_dict["battery_extra_info"] = battery_extra_info
        if flammable_liquids_extra_info is not UNSET:
            field_dict["flammable_liquids_extra_info"] = flammable_liquids_extra_info
        if aerosol_extra_info is not UNSET:
            field_dict["aerosol_extra_info"] = aerosol_extra_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aerosol_extra_info import AerosolExtraInfo  # noqa: PLC0415
        from ..models.battery_extra_info import BatteryExtraInfo  # noqa: PLC0415
        from ..models.flammable_liquids_extra_info import FlammableLiquidsExtraInfo  # noqa: PLC0415

        d = dict(src_dict)
        hazmat_type = HazmatInfoHazmatType(d.pop("hazmat_type"))

        dg_class = HazmatInfoDgClass(d.pop("dg_class"))

        dg_uncode = HazmatInfoDgUncode(d.pop("dg_uncode"))

        msds_file_url = d.pop("msds_file_url")

        _battery_extra_info = d.pop("battery_extra_info", UNSET)
        battery_extra_info: BatteryExtraInfo | Unset
        if isinstance(_battery_extra_info, Unset):
            battery_extra_info = UNSET
        else:
            battery_extra_info = BatteryExtraInfo.from_dict(_battery_extra_info)

        _flammable_liquids_extra_info = d.pop("flammable_liquids_extra_info", UNSET)
        flammable_liquids_extra_info: FlammableLiquidsExtraInfo | Unset
        if isinstance(_flammable_liquids_extra_info, Unset):
            flammable_liquids_extra_info = UNSET
        else:
            flammable_liquids_extra_info = FlammableLiquidsExtraInfo.from_dict(_flammable_liquids_extra_info)

        _aerosol_extra_info = d.pop("aerosol_extra_info", UNSET)
        aerosol_extra_info: AerosolExtraInfo | Unset
        if isinstance(_aerosol_extra_info, Unset):
            aerosol_extra_info = UNSET
        else:
            aerosol_extra_info = AerosolExtraInfo.from_dict(_aerosol_extra_info)

        hazmat_info = cls(
            hazmat_type=hazmat_type,
            dg_class=dg_class,
            dg_uncode=dg_uncode,
            msds_file_url=msds_file_url,
            battery_extra_info=battery_extra_info,
            flammable_liquids_extra_info=flammable_liquids_extra_info,
            aerosol_extra_info=aerosol_extra_info,
        )

        hazmat_info.additional_properties = d
        return hazmat_info

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
