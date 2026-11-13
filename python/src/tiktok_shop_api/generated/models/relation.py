from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Relation")



@_attrs_define
class Relation:
    """ 
        Attributes:
            method (str | Unset): Always returned. Participation method for the current campaign, not a conflict record for
                another campaign.
                How the shop participates in this campaign.
                - DIRECT: The shop registers directly for this campaign. Related records for other campaigns are not treated as
                registration for this campaign.
                - BUNDLE: The shop participates in this campaign through a bundle registration.
            related_campaign_id (str | Unset): For BUNDLE, returned only if the bundle entry campaign is visible to the
                shop. Omitted for DIRECT. A decimal string from 1 to 9223372036854775807.
            related_campaign_type (str | Unset): Type of the bundle entry campaign, used to select its detail endpoint.
                Returned together with related_campaign_id. Both fields are omitted if the type cannot be confirmed, without
                affecting the confirmed participation method.
                Unified campaign type with the same semantics in lists and all four detail models. Distinct from campaign group
                type.
                - PRODUCT: Product campaign.
                - SHOP: Shop campaign.
                - LIVESTREAM: Livestream campaign.
                - SHORT_VIDEO: Short video campaign.
     """

    method: str | Unset = UNSET
    related_campaign_id: str | Unset = UNSET
    related_campaign_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method

        related_campaign_id = self.related_campaign_id

        related_campaign_type = self.related_campaign_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if method is not UNSET:
            field_dict["method"] = method
        if related_campaign_id is not UNSET:
            field_dict["related_campaign_id"] = related_campaign_id
        if related_campaign_type is not UNSET:
            field_dict["related_campaign_type"] = related_campaign_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = d.pop("method", UNSET)

        related_campaign_id = d.pop("related_campaign_id", UNSET)

        related_campaign_type = d.pop("related_campaign_type", UNSET)

        relation = cls(
            method=method,
            related_campaign_id=related_campaign_id,
            related_campaign_type=related_campaign_type,
        )


        relation.additional_properties = d
        return relation

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
