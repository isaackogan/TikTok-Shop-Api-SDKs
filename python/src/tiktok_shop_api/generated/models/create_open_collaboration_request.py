from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateOpenCollaborationRequest")


@_attrs_define
class CreateOpenCollaborationRequest:
    """
    Attributes:
        product_id (str): The product ID to add to the affiliate open collaboration. Submit one product per request.
        commission_rate (int): The commission rate for the open collaboration, expressed in hundredths of a percent. For
            example, `3587` represents `35.87%`. The value must be from `100` to `8000`, inclusive.
    """

    product_id: str
    commission_rate: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        commission_rate = self.commission_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "commission_rate": commission_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id")

        commission_rate = d.pop("commission_rate")

        create_open_collaboration_request = cls(
            product_id=product_id,
            commission_rate=commission_rate,
        )

        create_open_collaboration_request.additional_properties = d
        return create_open_collaboration_request

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
