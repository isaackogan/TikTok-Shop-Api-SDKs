from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_affiliate_orders_by_creator_request_time_type import SearchAffiliateOrdersByCreatorRequestTimeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchAffiliateOrdersByCreatorRequest")


@_attrs_define
class SearchAffiliateOrdersByCreatorRequest:
    """
    Attributes:
        time_ge (int): The inclusive start of the time range for the selected `time_type`, as a Unix timestamp in
            milliseconds. Orders with timestamps greater than or equal to `time_ge` and less than `time_lt` are included.
        time_lt (int): The exclusive end of the time range for the selected `time_type`, as a Unix timestamp in
            milliseconds. Orders with timestamps greater than or equal to `time_ge` and less than `time_lt` are included.
        time_type (SearchAffiliateOrdersByCreatorRequestTimeType | Unset): Specifies the type of timestamp to filter the
            orders by. The query time range (time_ge and time_lt) will be applied to the selected time type.
            Possible values:
            - PAY_TIME: Filter based on the order payment time.
            - DELIVERY_TIME: Filter based on the order delivery/shipment time.
            - SETTLE_TIME: Filter based on the order settlement time.
            - CREATE_TIME (default): Filter based on the order creation time.
    """

    time_ge: int
    time_lt: int
    time_type: SearchAffiliateOrdersByCreatorRequestTimeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_ge = self.time_ge

        time_lt = self.time_lt

        time_type: str | Unset = UNSET
        if not isinstance(self.time_type, Unset):
            time_type = self.time_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_ge": time_ge,
                "time_lt": time_lt,
            }
        )
        if time_type is not UNSET:
            field_dict["time_type"] = time_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_ge = d.pop("time_ge")

        time_lt = d.pop("time_lt")

        _time_type = d.pop("time_type", UNSET)
        time_type: SearchAffiliateOrdersByCreatorRequestTimeType | Unset
        if isinstance(_time_type, Unset):
            time_type = UNSET
        else:
            time_type = SearchAffiliateOrdersByCreatorRequestTimeType(_time_type)

        search_affiliate_orders_by_creator_request = cls(
            time_ge=time_ge,
            time_lt=time_lt,
            time_type=time_type,
        )

        search_affiliate_orders_by_creator_request.additional_properties = d
        return search_affiliate_orders_by_creator_request

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
