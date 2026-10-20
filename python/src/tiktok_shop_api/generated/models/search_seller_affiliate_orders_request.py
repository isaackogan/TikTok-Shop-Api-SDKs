from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSellerAffiliateOrdersRequest")


@_attrs_define
class SearchSellerAffiliateOrdersRequest:
    """
    Attributes:
        create_time_lt (int | Unset): Filter orders created before this time, specified as a Unix timestamp in seconds.
            Use it with `create_time_ge`; the interval in a single request must not exceed three months. See
            `create_time_ge` for omitted-bound behavior.
        create_time_ge (int | Unset): Filter orders to show only those that are created on or after the specified date
            and time. Unix timestamp.

            Note:
            `create_time_ge` and `create_time_lt` together constitute the creation time filter condition.
            - If `create_time_ge` is filled but `create_time_lt` is empty, `create_time_lt` will default to the current
            time.
            - If `create_time_lt` is filled but `create_time_ge` is empty, `create_time_ge` will default to the earliest
            shop time.
            If both are not specified, data from the last three months will be queried by default.
        program_id (str | Unset): Filter orders by the associated affiliate partner campaign ID.
    """

    create_time_lt: int | Unset = UNSET
    create_time_ge: int | Unset = UNSET
    program_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time_lt = self.create_time_lt

        create_time_ge = self.create_time_ge

        program_id = self.program_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time_lt is not UNSET:
            field_dict["create_time_lt"] = create_time_lt
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if program_id is not UNSET:
            field_dict["program_id"] = program_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_time_lt = d.pop("create_time_lt", UNSET)

        create_time_ge = d.pop("create_time_ge", UNSET)

        program_id = d.pop("program_id", UNSET)

        search_seller_affiliate_orders_request = cls(
            create_time_lt=create_time_lt,
            create_time_ge=create_time_ge,
            program_id=program_id,
        )

        search_seller_affiliate_orders_request.additional_properties = d
        return search_seller_affiliate_orders_request

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
