from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_logistics_tracking_response_data_logistics_detail import (
        GetLogisticsTrackingResponseDataLogisticsDetail,
    )


T = TypeVar("T", bound="GetLogisticsTrackingResponseData")


@_attrs_define
class GetLogisticsTrackingResponseData:
    """
    Attributes:
        order_id (str | Unset): TikTok Shop order ID.
        logistics_details (list[GetLogisticsTrackingResponseDataLogisticsDetail] | Unset): A list of parcels in the
            order. Each item describes one parcel and can include its carrier, latest tracking number, and tracking-event
            history.
    """

    order_id: str | Unset = UNSET
    logistics_details: list[GetLogisticsTrackingResponseDataLogisticsDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        logistics_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.logistics_details, Unset):
            logistics_details = []
            for logistics_details_item_data in self.logistics_details:
                logistics_details_item = logistics_details_item_data.to_dict()
                logistics_details.append(logistics_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if logistics_details is not UNSET:
            field_dict["logistics_details"] = logistics_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_logistics_tracking_response_data_logistics_detail import (
            GetLogisticsTrackingResponseDataLogisticsDetail,  # noqa: PLC0415
        )

        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        _logistics_details = d.pop("logistics_details", UNSET)
        logistics_details: list[GetLogisticsTrackingResponseDataLogisticsDetail] | Unset = UNSET
        if _logistics_details is not UNSET:
            logistics_details = []
            for logistics_details_item_data in _logistics_details:
                logistics_details_item = GetLogisticsTrackingResponseDataLogisticsDetail.from_dict(
                    logistics_details_item_data
                )

                logistics_details.append(logistics_details_item)

        get_logistics_tracking_response_data = cls(
            order_id=order_id,
            logistics_details=logistics_details,
        )

        get_logistics_tracking_response_data.additional_properties = d
        return get_logistics_tracking_response_data

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
