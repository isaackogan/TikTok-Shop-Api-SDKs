from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetOrderCustomsRequirementsRequest")


@_attrs_define
class GetOrderCustomsRequirementsRequest:
    """
    Attributes:
        order_ids (list[str]): TikTok Shop order IDs to query. When providing a request body, include 1 to 50 order IDs.
    """

    order_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_ids = self.order_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_ids": order_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_ids = cast(list[str], d.pop("order_ids"))

        get_order_customs_requirements_request = cls(
            order_ids=order_ids,
        )

        get_order_customs_requirements_request.additional_properties = d
        return get_order_customs_requirements_request

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
