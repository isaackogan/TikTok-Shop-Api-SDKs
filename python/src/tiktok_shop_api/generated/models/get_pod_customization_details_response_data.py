from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_pod_customization_details_response_data_pod_detail import (
        GetPODCustomizationDetailsResponseDataPodDetail,
    )


T = TypeVar("T", bound="GetPODCustomizationDetailsResponseData")


@_attrs_define
class GetPODCustomizationDetailsResponseData:
    """
    Attributes:
        pod_details (list[GetPODCustomizationDetailsResponseDataPodDetail] | Unset): The POD customization details
            returned for the requested order lines.
        status_code (int | Unset): response status
    """

    pod_details: list[GetPODCustomizationDetailsResponseDataPodDetail] | Unset = UNSET
    status_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pod_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pod_details, Unset):
            pod_details = []
            for pod_details_item_data in self.pod_details:
                pod_details_item = pod_details_item_data.to_dict()
                pod_details.append(pod_details_item)

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pod_details is not UNSET:
            field_dict["pod_details"] = pod_details
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_pod_customization_details_response_data_pod_detail import (
            GetPODCustomizationDetailsResponseDataPodDetail,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _pod_details = d.pop("pod_details", UNSET)
        pod_details: list[GetPODCustomizationDetailsResponseDataPodDetail] | Unset = UNSET
        if _pod_details is not UNSET:
            pod_details = []
            for pod_details_item_data in _pod_details:
                pod_details_item = GetPODCustomizationDetailsResponseDataPodDetail.from_dict(pod_details_item_data)

                pod_details.append(pod_details_item)

        status_code = d.pop("status_code", UNSET)

        get_pod_customization_details_response_data = cls(
            pod_details=pod_details,
            status_code=status_code,
        )

        get_pod_customization_details_response_data.additional_properties = d
        return get_pod_customization_details_response_data

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
