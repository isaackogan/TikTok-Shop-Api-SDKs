from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_engagement_feature_permissions_response_data_feature import (
        GetEngagementFeaturePermissionsResponseDataFeature,
    )


T = TypeVar("T", bound="GetEngagementFeaturePermissionsResponseData")


@_attrs_define
class GetEngagementFeaturePermissionsResponseData:
    """
    Attributes:
        features (list[GetEngagementFeaturePermissionsResponseDataFeature] | Unset): The list of customer engagement
            features that has access control.
    """

    features: list[GetEngagementFeaturePermissionsResponseDataFeature] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_engagement_feature_permissions_response_data_feature import (
            GetEngagementFeaturePermissionsResponseDataFeature,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _features = d.pop("features", UNSET)
        features: list[GetEngagementFeaturePermissionsResponseDataFeature] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = GetEngagementFeaturePermissionsResponseDataFeature.from_dict(features_item_data)

                features.append(features_item)

        get_engagement_feature_permissions_response_data = cls(
            features=features,
        )

        get_engagement_feature_permissions_response_data.additional_properties = d
        return get_engagement_feature_permissions_response_data

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
