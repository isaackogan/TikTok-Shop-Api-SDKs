from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchOpenCollaborationProductsRequestCommissionRateRange")


@_attrs_define
class SearchOpenCollaborationProductsRequestCommissionRateRange:
    """
    Attributes:
        rate_ge (int | Unset): The minimum commission rate. Products with a commission rate greater than or equal to
            this value are included in the results. Express the rate in hundredths of a percent; for example, `3587` means
            `35.87%`. The value must be from `100` to `8000`, inclusive.
        rate_lt (int | Unset): The commission rate must be less than this value in order to be included in the search
            results. The commission rate is expressed in hundredths of a percent. For example, `3587` is a commission rate
            of `35.87%`. This value must a minimum of `1000`.
    """

    rate_ge: int | Unset = UNSET
    rate_lt: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate_ge = self.rate_ge

        rate_lt = self.rate_lt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate_ge is not UNSET:
            field_dict["rate_ge"] = rate_ge
        if rate_lt is not UNSET:
            field_dict["rate_lt"] = rate_lt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate_ge = d.pop("rate_ge", UNSET)

        rate_lt = d.pop("rate_lt", UNSET)

        search_open_collaboration_products_request_commission_rate_range = cls(
            rate_ge=rate_ge,
            rate_lt=rate_lt,
        )

        search_open_collaboration_products_request_commission_rate_range.additional_properties = d
        return search_open_collaboration_products_request_commission_rate_range

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
