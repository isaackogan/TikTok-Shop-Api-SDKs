from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creator_search_sample_application_fulfillments_response_data_fulfillment import (
        CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillment,
    )


T = TypeVar("T", bound="CreatorSearchSampleApplicationFulfillmentsResponseData")


@_attrs_define
class CreatorSearchSampleApplicationFulfillmentsResponseData:
    """
    Attributes:
        fulfillments (list[CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillment] | Unset): Creator
            fulfillment contents.
    """

    fulfillments: list[CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillment] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fulfillments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fulfillments, Unset):
            fulfillments = []
            for fulfillments_item_data in self.fulfillments:
                fulfillments_item = fulfillments_item_data.to_dict()
                fulfillments.append(fulfillments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fulfillments is not UNSET:
            field_dict["fulfillments"] = fulfillments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator_search_sample_application_fulfillments_response_data_fulfillment import (
            CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillment,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _fulfillments = d.pop("fulfillments", UNSET)
        fulfillments: list[CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillment] | Unset = UNSET
        if _fulfillments is not UNSET:
            fulfillments = []
            for fulfillments_item_data in _fulfillments:
                fulfillments_item = CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillment.from_dict(
                    fulfillments_item_data
                )

                fulfillments.append(fulfillments_item)

        creator_search_sample_application_fulfillments_response_data = cls(
            fulfillments=fulfillments,
        )

        creator_search_sample_application_fulfillments_response_data.additional_properties = d
        return creator_search_sample_application_fulfillments_response_data

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
