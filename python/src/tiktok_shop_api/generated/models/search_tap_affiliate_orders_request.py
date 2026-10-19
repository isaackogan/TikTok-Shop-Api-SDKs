from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchTAPAffiliateOrdersRequest")


@_attrs_define
class SearchTAPAffiliateOrdersRequest:
    """
    Attributes:
        create_time_ge (int | Unset): Filter orders created at or after this time, specified as a Unix timestamp in
            seconds (UTC).

            `create_time_ge` and `create_time_lt` must be provided together, and the interval must not exceed three months.
            If both fields are omitted, the API queries orders from the last three months.
        create_time_lt (int | Unset): Filter orders created before this time, specified as a Unix timestamp in seconds
            (UTC). See `create_time_ge` for the pairing, interval, and default behavior.
        campaign_id (str | Unset): Filter orders by a TAP campaign using its identifier.
    """

    create_time_ge: int | Unset = UNSET
    create_time_lt: int | Unset = UNSET
    campaign_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time_ge = self.create_time_ge

        create_time_lt = self.create_time_lt

        campaign_id = self.campaign_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if create_time_lt is not UNSET:
            field_dict["create_time_lt"] = create_time_lt
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_time_ge = d.pop("create_time_ge", UNSET)

        create_time_lt = d.pop("create_time_lt", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

        search_tap_affiliate_orders_request = cls(
            create_time_ge=create_time_ge,
            create_time_lt=create_time_lt,
            campaign_id=campaign_id,
        )

        search_tap_affiliate_orders_request.additional_properties = d
        return search_tap_affiliate_orders_request

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
