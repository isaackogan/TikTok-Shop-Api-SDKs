from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetPODCustomizationDetailsResponseDataPodDetail")



@_attrs_define
class GetPODCustomizationDetailsResponseDataPodDetail:
    """ 
        Attributes:
            pod_info_json (str | Unset): A JSON-encoded string containing the POD customization template for the order line.
            order_line_id (str | Unset): The unique identifier of the order line item.
     """

    pod_info_json: str | Unset = UNSET
    order_line_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        pod_info_json = self.pod_info_json

        order_line_id = self.order_line_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if pod_info_json is not UNSET:
            field_dict["pod_info_json"] = pod_info_json
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pod_info_json = d.pop("pod_info_json", UNSET)

        order_line_id = d.pop("order_line_id", UNSET)

        get_pod_customization_details_response_data_pod_detail = cls(
            pod_info_json=pod_info_json,
            order_line_id=order_line_id,
        )


        get_pod_customization_details_response_data_pod_detail.additional_properties = d
        return get_pod_customization_details_response_data_pod_detail

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
