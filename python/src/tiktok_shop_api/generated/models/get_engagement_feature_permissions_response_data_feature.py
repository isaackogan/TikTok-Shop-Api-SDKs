from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_engagement_feature_permissions_response_data_feature_name import (
    GetEngagementFeaturePermissionsResponseDataFeatureName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetEngagementFeaturePermissionsResponseDataFeature")


@_attrs_define
class GetEngagementFeaturePermissionsResponseDataFeature:
    """
    Attributes:
        name (GetEngagementFeaturePermissionsResponseDataFeatureName | Unset): The feature name.
            Possible values:
            - `FUNDAMENTAL`: The ability to use any customer engagement APIs or features. This is the prerequisite for all
            other customer engagement features.
            - `CUSTOM_MSG`: The ability to define and send custom messages.
        is_authorized (bool | Unset): A flag to indicate whether the shop has permission to use this feature.
            Possible values:
            - `true`: Authorized to use this feature.
            - `false`: Not authorized to use this feature.
    """

    name: GetEngagementFeaturePermissionsResponseDataFeatureName | Unset = UNSET
    is_authorized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        is_authorized = self.is_authorized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if is_authorized is not UNSET:
            field_dict["is_authorized"] = is_authorized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: GetEngagementFeaturePermissionsResponseDataFeatureName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = GetEngagementFeaturePermissionsResponseDataFeatureName(_name)

        is_authorized = d.pop("is_authorized", UNSET)

        get_engagement_feature_permissions_response_data_feature = cls(
            name=name,
            is_authorized=is_authorized,
        )

        get_engagement_feature_permissions_response_data_feature.additional_properties = d
        return get_engagement_feature_permissions_response_data_feature

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
