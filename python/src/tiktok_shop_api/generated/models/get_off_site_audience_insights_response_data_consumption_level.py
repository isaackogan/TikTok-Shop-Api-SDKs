from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetOffSiteAudienceInsightsResponseDataConsumptionLevel")



@_attrs_define
class GetOffSiteAudienceInsightsResponseDataConsumptionLevel:
    """ 
        Attributes:
            name (str | Unset): Consumption-level name returned by the report; labels are source values and are not
                guaranteed to follow a fixed display dictionary.
            off_site_customers_value (None | str | Unset): Percentage of the report's off-site attributed purchasers in this
                consumption level, calculated against the report's total off-site customer count. Returned as a percentage
                string with a % suffix, such as 32.15%; do not multiply by 100 again. Unavailable values may be null and must
                not be replaced with 0%.
            tts_customers_value (None | str | Unset): Percentage of the report's TikTok Shop purchasers in this consumption
                level, calculated against the report's total TikTok Shop customer count. Returned as a percentage string with a
                % suffix, such as 32.15%; do not multiply by 100 again. Unavailable values may be null and must not be replaced
                with 0%.
     """

    name: str | Unset = UNSET
    off_site_customers_value: None | str | Unset = UNSET
    tts_customers_value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        off_site_customers_value: None | str | Unset
        if isinstance(self.off_site_customers_value, Unset):
            off_site_customers_value = UNSET
        else:
            off_site_customers_value = self.off_site_customers_value

        tts_customers_value: None | str | Unset
        if isinstance(self.tts_customers_value, Unset):
            tts_customers_value = UNSET
        else:
            tts_customers_value = self.tts_customers_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if off_site_customers_value is not UNSET:
            field_dict["off_site_customers_value"] = off_site_customers_value
        if tts_customers_value is not UNSET:
            field_dict["tts_customers_value"] = tts_customers_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_off_site_customers_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        off_site_customers_value = _parse_off_site_customers_value(d.pop("off_site_customers_value", UNSET))


        def _parse_tts_customers_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tts_customers_value = _parse_tts_customers_value(d.pop("tts_customers_value", UNSET))


        get_off_site_audience_insights_response_data_consumption_level = cls(
            name=name,
            off_site_customers_value=off_site_customers_value,
            tts_customers_value=tts_customers_value,
        )


        get_off_site_audience_insights_response_data_consumption_level.additional_properties = d
        return get_off_site_audience_insights_response_data_consumption_level

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
