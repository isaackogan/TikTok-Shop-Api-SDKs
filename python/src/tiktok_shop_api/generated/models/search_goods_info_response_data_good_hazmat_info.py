from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_goods_info_response_data_good_hazmat_info_dg_class import (
    SearchGoodsInfoResponseDataGoodHazmatInfoDgClass,
)
from ..models.search_goods_info_response_data_good_hazmat_info_dg_uncode import (
    SearchGoodsInfoResponseDataGoodHazmatInfoDgUncode,
)
from ..models.search_goods_info_response_data_good_hazmat_info_hazmat_type import (
    SearchGoodsInfoResponseDataGoodHazmatInfoHazmatType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aerosol_extra_info import AerosolExtraInfo
    from ..models.search_goods_info_response_data_good_hazmat_info_battery_extra_info import (
        SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfo,
    )
    from ..models.search_goods_info_response_data_good_hazmat_info_flammable_liquids_extra_info import (
        SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfo,
    )


T = TypeVar("T", bound="SearchGoodsInfoResponseDataGoodHazmatInfo")


@_attrs_define
class SearchGoodsInfoResponseDataGoodHazmatInfo:
    """
    Attributes:
        hazmat_type (SearchGoodsInfoResponseDataGoodHazmatInfoHazmatType | Unset): hazardous goods type
            Possible values:
            -MAGNETIZED
            -BATTERY
            -FLAMMABLE_LIQUID
            -AEROSOLS
        battery_extra_info (SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfo | Unset):
        flammable_liquids_extra_info (SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfo | Unset):
        aerosol_extra_info (AerosolExtraInfo | Unset):
        dg_class (SearchGoodsInfoResponseDataGoodHazmatInfoDgClass | Unset): Hazmat class
            Possible values:
            -CLASS_2
            -CLASS_3
            -CLASS_9
        dg_uncode (SearchGoodsInfoResponseDataGoodHazmatInfoDgUncode | Unset): UN identifier for the hazardous
            substance. Standard UN values use the `UN` prefix followed by four digits; `OTHER` is also supported.
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
        msds_file_url (str | Unset): Material safety data sheet of the hazmat goods to support review the goods' safety
            compliance in FBT
    """

    hazmat_type: SearchGoodsInfoResponseDataGoodHazmatInfoHazmatType | Unset = UNSET
    battery_extra_info: SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfo | Unset = UNSET
    flammable_liquids_extra_info: SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfo | Unset = UNSET
    aerosol_extra_info: AerosolExtraInfo | Unset = UNSET
    dg_class: SearchGoodsInfoResponseDataGoodHazmatInfoDgClass | Unset = UNSET
    dg_uncode: SearchGoodsInfoResponseDataGoodHazmatInfoDgUncode | Unset = UNSET
    msds_file_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hazmat_type: str | Unset = UNSET
        if not isinstance(self.hazmat_type, Unset):
            hazmat_type = self.hazmat_type.value

        battery_extra_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.battery_extra_info, Unset):
            battery_extra_info = self.battery_extra_info.to_dict()

        flammable_liquids_extra_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flammable_liquids_extra_info, Unset):
            flammable_liquids_extra_info = self.flammable_liquids_extra_info.to_dict()

        aerosol_extra_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aerosol_extra_info, Unset):
            aerosol_extra_info = self.aerosol_extra_info.to_dict()

        dg_class: str | Unset = UNSET
        if not isinstance(self.dg_class, Unset):
            dg_class = self.dg_class.value

        dg_uncode: str | Unset = UNSET
        if not isinstance(self.dg_uncode, Unset):
            dg_uncode = self.dg_uncode.value

        msds_file_url = self.msds_file_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hazmat_type is not UNSET:
            field_dict["hazmat_type"] = hazmat_type
        if battery_extra_info is not UNSET:
            field_dict["battery_extra_info"] = battery_extra_info
        if flammable_liquids_extra_info is not UNSET:
            field_dict["flammable_liquids_extra_info"] = flammable_liquids_extra_info
        if aerosol_extra_info is not UNSET:
            field_dict["aerosol_extra_info"] = aerosol_extra_info
        if dg_class is not UNSET:
            field_dict["dg_class"] = dg_class
        if dg_uncode is not UNSET:
            field_dict["dg_uncode"] = dg_uncode
        if msds_file_url is not UNSET:
            field_dict["msds_file_url"] = msds_file_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aerosol_extra_info import AerosolExtraInfo  # noqa: PLC0415
        from ..models.search_goods_info_response_data_good_hazmat_info_battery_extra_info import (
            SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfo,  # noqa: PLC0415
        )
        from ..models.search_goods_info_response_data_good_hazmat_info_flammable_liquids_extra_info import (
            SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _hazmat_type = d.pop("hazmat_type", UNSET)
        hazmat_type: SearchGoodsInfoResponseDataGoodHazmatInfoHazmatType | Unset
        if isinstance(_hazmat_type, Unset):
            hazmat_type = UNSET
        else:
            hazmat_type = SearchGoodsInfoResponseDataGoodHazmatInfoHazmatType(_hazmat_type)

        _battery_extra_info = d.pop("battery_extra_info", UNSET)
        battery_extra_info: SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfo | Unset
        if isinstance(_battery_extra_info, Unset):
            battery_extra_info = UNSET
        else:
            battery_extra_info = SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfo.from_dict(
                _battery_extra_info
            )

        _flammable_liquids_extra_info = d.pop("flammable_liquids_extra_info", UNSET)
        flammable_liquids_extra_info: SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfo | Unset
        if isinstance(_flammable_liquids_extra_info, Unset):
            flammable_liquids_extra_info = UNSET
        else:
            flammable_liquids_extra_info = SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfo.from_dict(
                _flammable_liquids_extra_info
            )

        _aerosol_extra_info = d.pop("aerosol_extra_info", UNSET)
        aerosol_extra_info: AerosolExtraInfo | Unset
        if isinstance(_aerosol_extra_info, Unset):
            aerosol_extra_info = UNSET
        else:
            aerosol_extra_info = AerosolExtraInfo.from_dict(_aerosol_extra_info)

        _dg_class = d.pop("dg_class", UNSET)
        dg_class: SearchGoodsInfoResponseDataGoodHazmatInfoDgClass | Unset
        if isinstance(_dg_class, Unset):
            dg_class = UNSET
        else:
            dg_class = SearchGoodsInfoResponseDataGoodHazmatInfoDgClass(_dg_class)

        _dg_uncode = d.pop("dg_uncode", UNSET)
        dg_uncode: SearchGoodsInfoResponseDataGoodHazmatInfoDgUncode | Unset
        if isinstance(_dg_uncode, Unset):
            dg_uncode = UNSET
        else:
            dg_uncode = SearchGoodsInfoResponseDataGoodHazmatInfoDgUncode(_dg_uncode)

        msds_file_url = d.pop("msds_file_url", UNSET)

        search_goods_info_response_data_good_hazmat_info = cls(
            hazmat_type=hazmat_type,
            battery_extra_info=battery_extra_info,
            flammable_liquids_extra_info=flammable_liquids_extra_info,
            aerosol_extra_info=aerosol_extra_info,
            dg_class=dg_class,
            dg_uncode=dg_uncode,
            msds_file_url=msds_file_url,
        )

        search_goods_info_response_data_good_hazmat_info.additional_properties = d
        return search_goods_info_response_data_good_hazmat_info

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
