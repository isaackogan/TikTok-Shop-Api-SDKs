from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_live_room_user_portraits_response_data_all_ads_age_indicator import (
        GetLiveRoomUserPortraitsResponseDataAllAdsAgeIndicator,
    )
    from ..models.get_live_room_user_portraits_response_data_all_ads_gender_indicator import (
        GetLiveRoomUserPortraitsResponseDataAllAdsGenderIndicator,
    )
    from ..models.get_live_room_user_portraits_response_data_all_fan_indicator import (
        GetLiveRoomUserPortraitsResponseDataAllFanIndicator,
    )
    from ..models.get_live_room_user_portraits_response_data_paid_ads_age_indicator import (
        GetLiveRoomUserPortraitsResponseDataPaidAdsAgeIndicator,
    )
    from ..models.get_live_room_user_portraits_response_data_paid_ads_gender_indicator import (
        GetLiveRoomUserPortraitsResponseDataPaidAdsGenderIndicator,
    )
    from ..models.get_live_room_user_portraits_response_data_paid_fan_indicator import (
        GetLiveRoomUserPortraitsResponseDataPaidFanIndicator,
    )
    from ..models.get_live_room_user_portraits_response_data_region_indicator import (
        GetLiveRoomUserPortraitsResponseDataRegionIndicator,
    )


T = TypeVar("T", bound="GetLiveRoomUserPortraitsResponseData")


@_attrs_define
class GetLiveRoomUserPortraitsResponseData:
    """
    Attributes:
        all_ads_gender_indicators (list[GetLiveRoomUserPortraitsResponseDataAllAdsGenderIndicator] | Unset): Gender
            indicators for advertisement
        all_fan_indicators (list[GetLiveRoomUserPortraitsResponseDataAllFanIndicator] | Unset): Fans indicators
        all_ads_age_indicators (list[GetLiveRoomUserPortraitsResponseDataAllAdsAgeIndicator] | Unset): Age indicators
            for advertisement
        region_indicators (list[GetLiveRoomUserPortraitsResponseDataRegionIndicator] | Unset): Country-level user
            portrait indicators for the live room.
        paid_ads_age_indicators (list[GetLiveRoomUserPortraitsResponseDataPaidAdsAgeIndicator] | Unset): Paid
            advertisement age indicators for advertisement
        paid_ads_gender_indicators (list[GetLiveRoomUserPortraitsResponseDataPaidAdsGenderIndicator] | Unset): Paid
            advertisement gender indicators for advertisement
        paid_fan_indicators (list[GetLiveRoomUserPortraitsResponseDataPaidFanIndicator] | Unset): Paid fans indicators
    """

    all_ads_gender_indicators: list[GetLiveRoomUserPortraitsResponseDataAllAdsGenderIndicator] | Unset = UNSET
    all_fan_indicators: list[GetLiveRoomUserPortraitsResponseDataAllFanIndicator] | Unset = UNSET
    all_ads_age_indicators: list[GetLiveRoomUserPortraitsResponseDataAllAdsAgeIndicator] | Unset = UNSET
    region_indicators: list[GetLiveRoomUserPortraitsResponseDataRegionIndicator] | Unset = UNSET
    paid_ads_age_indicators: list[GetLiveRoomUserPortraitsResponseDataPaidAdsAgeIndicator] | Unset = UNSET
    paid_ads_gender_indicators: list[GetLiveRoomUserPortraitsResponseDataPaidAdsGenderIndicator] | Unset = UNSET
    paid_fan_indicators: list[GetLiveRoomUserPortraitsResponseDataPaidFanIndicator] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_ads_gender_indicators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_ads_gender_indicators, Unset):
            all_ads_gender_indicators = []
            for all_ads_gender_indicators_item_data in self.all_ads_gender_indicators:
                all_ads_gender_indicators_item = all_ads_gender_indicators_item_data.to_dict()
                all_ads_gender_indicators.append(all_ads_gender_indicators_item)

        all_fan_indicators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_fan_indicators, Unset):
            all_fan_indicators = []
            for all_fan_indicators_item_data in self.all_fan_indicators:
                all_fan_indicators_item = all_fan_indicators_item_data.to_dict()
                all_fan_indicators.append(all_fan_indicators_item)

        all_ads_age_indicators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_ads_age_indicators, Unset):
            all_ads_age_indicators = []
            for all_ads_age_indicators_item_data in self.all_ads_age_indicators:
                all_ads_age_indicators_item = all_ads_age_indicators_item_data.to_dict()
                all_ads_age_indicators.append(all_ads_age_indicators_item)

        region_indicators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.region_indicators, Unset):
            region_indicators = []
            for region_indicators_item_data in self.region_indicators:
                region_indicators_item = region_indicators_item_data.to_dict()
                region_indicators.append(region_indicators_item)

        paid_ads_age_indicators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.paid_ads_age_indicators, Unset):
            paid_ads_age_indicators = []
            for paid_ads_age_indicators_item_data in self.paid_ads_age_indicators:
                paid_ads_age_indicators_item = paid_ads_age_indicators_item_data.to_dict()
                paid_ads_age_indicators.append(paid_ads_age_indicators_item)

        paid_ads_gender_indicators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.paid_ads_gender_indicators, Unset):
            paid_ads_gender_indicators = []
            for paid_ads_gender_indicators_item_data in self.paid_ads_gender_indicators:
                paid_ads_gender_indicators_item = paid_ads_gender_indicators_item_data.to_dict()
                paid_ads_gender_indicators.append(paid_ads_gender_indicators_item)

        paid_fan_indicators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.paid_fan_indicators, Unset):
            paid_fan_indicators = []
            for paid_fan_indicators_item_data in self.paid_fan_indicators:
                paid_fan_indicators_item = paid_fan_indicators_item_data.to_dict()
                paid_fan_indicators.append(paid_fan_indicators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ads_gender_indicators is not UNSET:
            field_dict["all_ads_gender_indicators"] = all_ads_gender_indicators
        if all_fan_indicators is not UNSET:
            field_dict["all_fan_indicators"] = all_fan_indicators
        if all_ads_age_indicators is not UNSET:
            field_dict["all_ads_age_indicators"] = all_ads_age_indicators
        if region_indicators is not UNSET:
            field_dict["region_indicators"] = region_indicators
        if paid_ads_age_indicators is not UNSET:
            field_dict["paid_ads_age_indicators"] = paid_ads_age_indicators
        if paid_ads_gender_indicators is not UNSET:
            field_dict["paid_ads_gender_indicators"] = paid_ads_gender_indicators
        if paid_fan_indicators is not UNSET:
            field_dict["paid_fan_indicators"] = paid_fan_indicators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_live_room_user_portraits_response_data_all_ads_age_indicator import (
            GetLiveRoomUserPortraitsResponseDataAllAdsAgeIndicator,  # noqa: PLC0415
        )
        from ..models.get_live_room_user_portraits_response_data_all_ads_gender_indicator import (
            GetLiveRoomUserPortraitsResponseDataAllAdsGenderIndicator,  # noqa: PLC0415
        )
        from ..models.get_live_room_user_portraits_response_data_all_fan_indicator import (
            GetLiveRoomUserPortraitsResponseDataAllFanIndicator,  # noqa: PLC0415
        )
        from ..models.get_live_room_user_portraits_response_data_paid_ads_age_indicator import (
            GetLiveRoomUserPortraitsResponseDataPaidAdsAgeIndicator,  # noqa: PLC0415
        )
        from ..models.get_live_room_user_portraits_response_data_paid_ads_gender_indicator import (
            GetLiveRoomUserPortraitsResponseDataPaidAdsGenderIndicator,  # noqa: PLC0415
        )
        from ..models.get_live_room_user_portraits_response_data_paid_fan_indicator import (
            GetLiveRoomUserPortraitsResponseDataPaidFanIndicator,  # noqa: PLC0415
        )
        from ..models.get_live_room_user_portraits_response_data_region_indicator import (
            GetLiveRoomUserPortraitsResponseDataRegionIndicator,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _all_ads_gender_indicators = d.pop("all_ads_gender_indicators", UNSET)
        all_ads_gender_indicators: list[GetLiveRoomUserPortraitsResponseDataAllAdsGenderIndicator] | Unset = UNSET
        if _all_ads_gender_indicators is not UNSET:
            all_ads_gender_indicators = []
            for all_ads_gender_indicators_item_data in _all_ads_gender_indicators:
                all_ads_gender_indicators_item = GetLiveRoomUserPortraitsResponseDataAllAdsGenderIndicator.from_dict(
                    all_ads_gender_indicators_item_data
                )

                all_ads_gender_indicators.append(all_ads_gender_indicators_item)

        _all_fan_indicators = d.pop("all_fan_indicators", UNSET)
        all_fan_indicators: list[GetLiveRoomUserPortraitsResponseDataAllFanIndicator] | Unset = UNSET
        if _all_fan_indicators is not UNSET:
            all_fan_indicators = []
            for all_fan_indicators_item_data in _all_fan_indicators:
                all_fan_indicators_item = GetLiveRoomUserPortraitsResponseDataAllFanIndicator.from_dict(
                    all_fan_indicators_item_data
                )

                all_fan_indicators.append(all_fan_indicators_item)

        _all_ads_age_indicators = d.pop("all_ads_age_indicators", UNSET)
        all_ads_age_indicators: list[GetLiveRoomUserPortraitsResponseDataAllAdsAgeIndicator] | Unset = UNSET
        if _all_ads_age_indicators is not UNSET:
            all_ads_age_indicators = []
            for all_ads_age_indicators_item_data in _all_ads_age_indicators:
                all_ads_age_indicators_item = GetLiveRoomUserPortraitsResponseDataAllAdsAgeIndicator.from_dict(
                    all_ads_age_indicators_item_data
                )

                all_ads_age_indicators.append(all_ads_age_indicators_item)

        _region_indicators = d.pop("region_indicators", UNSET)
        region_indicators: list[GetLiveRoomUserPortraitsResponseDataRegionIndicator] | Unset = UNSET
        if _region_indicators is not UNSET:
            region_indicators = []
            for region_indicators_item_data in _region_indicators:
                region_indicators_item = GetLiveRoomUserPortraitsResponseDataRegionIndicator.from_dict(
                    region_indicators_item_data
                )

                region_indicators.append(region_indicators_item)

        _paid_ads_age_indicators = d.pop("paid_ads_age_indicators", UNSET)
        paid_ads_age_indicators: list[GetLiveRoomUserPortraitsResponseDataPaidAdsAgeIndicator] | Unset = UNSET
        if _paid_ads_age_indicators is not UNSET:
            paid_ads_age_indicators = []
            for paid_ads_age_indicators_item_data in _paid_ads_age_indicators:
                paid_ads_age_indicators_item = GetLiveRoomUserPortraitsResponseDataPaidAdsAgeIndicator.from_dict(
                    paid_ads_age_indicators_item_data
                )

                paid_ads_age_indicators.append(paid_ads_age_indicators_item)

        _paid_ads_gender_indicators = d.pop("paid_ads_gender_indicators", UNSET)
        paid_ads_gender_indicators: list[GetLiveRoomUserPortraitsResponseDataPaidAdsGenderIndicator] | Unset = UNSET
        if _paid_ads_gender_indicators is not UNSET:
            paid_ads_gender_indicators = []
            for paid_ads_gender_indicators_item_data in _paid_ads_gender_indicators:
                paid_ads_gender_indicators_item = GetLiveRoomUserPortraitsResponseDataPaidAdsGenderIndicator.from_dict(
                    paid_ads_gender_indicators_item_data
                )

                paid_ads_gender_indicators.append(paid_ads_gender_indicators_item)

        _paid_fan_indicators = d.pop("paid_fan_indicators", UNSET)
        paid_fan_indicators: list[GetLiveRoomUserPortraitsResponseDataPaidFanIndicator] | Unset = UNSET
        if _paid_fan_indicators is not UNSET:
            paid_fan_indicators = []
            for paid_fan_indicators_item_data in _paid_fan_indicators:
                paid_fan_indicators_item = GetLiveRoomUserPortraitsResponseDataPaidFanIndicator.from_dict(
                    paid_fan_indicators_item_data
                )

                paid_fan_indicators.append(paid_fan_indicators_item)

        get_live_room_user_portraits_response_data = cls(
            all_ads_gender_indicators=all_ads_gender_indicators,
            all_fan_indicators=all_fan_indicators,
            all_ads_age_indicators=all_ads_age_indicators,
            region_indicators=region_indicators,
            paid_ads_age_indicators=paid_ads_age_indicators,
            paid_ads_gender_indicators=paid_ads_gender_indicators,
            paid_fan_indicators=paid_fan_indicators,
        )

        get_live_room_user_portraits_response_data.additional_properties = d
        return get_live_room_user_portraits_response_data

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
