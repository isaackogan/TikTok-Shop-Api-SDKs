from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchPODCustomizationDetailsResponseDataPodDetail")



@_attrs_define
class SearchPODCustomizationDetailsResponseDataPodDetail:
    """ 
        Attributes:
            order_line_id (str | Unset): The unique identifier of the order line associated with the POD customization
                details.
            pod_detail (str | Unset): The unique identifier of the order line item.
     """

    order_line_id: str | Unset = UNSET
    pod_detail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_line_id = self.order_line_id

        pod_detail = self.pod_detail


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if pod_detail is not UNSET:
            field_dict["pod_detail"] = pod_detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_line_id = d.pop("order_line_id", UNSET)

        pod_detail = d.pop("pod_detail", UNSET)

        search_pod_customization_details_response_data_pod_detail = cls(
            order_line_id=order_line_id,
            pod_detail=pod_detail,
        )


        search_pod_customization_details_response_data_pod_detail.additional_properties = d
        return search_pod_customization_details_response_data_pod_detail

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
