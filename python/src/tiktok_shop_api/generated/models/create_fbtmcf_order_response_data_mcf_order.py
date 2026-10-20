from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFBTMCFOrderResponseDataMcfOrder")


@_attrs_define
class CreateFBTMCFOrderResponseDataMcfOrder:
    """
    Attributes:
        external_order_id (str | Unset): The corresponding order ID in your OMS.
        mcf_order_id (str | Unset): A unique ID that identifies different MCF orders
        create_time (int | Unset): The Unix timestamp, in seconds, when the MCF order was created.
    """

    external_order_id: str | Unset = UNSET
    mcf_order_id: str | Unset = UNSET
    create_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_order_id = self.external_order_id

        mcf_order_id = self.mcf_order_id

        create_time = self.create_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_order_id is not UNSET:
            field_dict["external_order_id"] = external_order_id
        if mcf_order_id is not UNSET:
            field_dict["mcf_order_id"] = mcf_order_id
        if create_time is not UNSET:
            field_dict["create_time"] = create_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_order_id = d.pop("external_order_id", UNSET)

        mcf_order_id = d.pop("mcf_order_id", UNSET)

        create_time = d.pop("create_time", UNSET)

        create_fbtmcf_order_response_data_mcf_order = cls(
            external_order_id=external_order_id,
            mcf_order_id=mcf_order_id,
            create_time=create_time,
        )

        create_fbtmcf_order_response_data_mcf_order.additional_properties = d
        return create_fbtmcf_order_response_data_mcf_order

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
