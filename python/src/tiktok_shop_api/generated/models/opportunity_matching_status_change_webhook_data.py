from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpportunityMatchingStatusChangeWebhookData")


@_attrs_define
class OpportunityMatchingStatusChangeWebhookData:
    """
    Attributes:
        external_product_id (str | Unset): An external product identifier used in the external ecommerce platform.
        opportunity_matching_status (str | Unset): The status of opportunity matching.
             Possible values:
             - `PENDING`: Waiting for opportunity matching.
             - `MATCHED`: There are one or more matched opportunities.
             - `NOT_MATCHED`: There are no matches.
        opportunity_ids (list[str] | Unset): A list of IDs for the matched opportunities.
        opportunity_matching_end_time (int | Unset): The time by which the system will stop matching opportunities for
            this candidate product. Unix timestamp.
             - Default: 60 days from the upload time.
             - Latest allowable time: 60 days from the upload time.
        update_time (int | Unset): The time when the opportunity matching status is last updated. Unix timestamp.
    """

    external_product_id: str | Unset = UNSET
    opportunity_matching_status: str | Unset = UNSET
    opportunity_ids: list[str] | Unset = UNSET
    opportunity_matching_end_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_product_id = self.external_product_id

        opportunity_matching_status = self.opportunity_matching_status

        opportunity_ids: list[str] | Unset = UNSET
        if not isinstance(self.opportunity_ids, Unset):
            opportunity_ids = self.opportunity_ids

        opportunity_matching_end_time = self.opportunity_matching_end_time

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_product_id is not UNSET:
            field_dict["external_product_id"] = external_product_id
        if opportunity_matching_status is not UNSET:
            field_dict["opportunity_matching_status"] = opportunity_matching_status
        if opportunity_ids is not UNSET:
            field_dict["opportunity_ids"] = opportunity_ids
        if opportunity_matching_end_time is not UNSET:
            field_dict["opportunity_matching_end_time"] = opportunity_matching_end_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_product_id = d.pop("external_product_id", UNSET)

        opportunity_matching_status = d.pop("opportunity_matching_status", UNSET)

        opportunity_ids = cast(list[str], d.pop("opportunity_ids", UNSET))

        opportunity_matching_end_time = d.pop("opportunity_matching_end_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        opportunity_matching_status_change_webhook_data = cls(
            external_product_id=external_product_id,
            opportunity_matching_status=opportunity_matching_status,
            opportunity_ids=opportunity_ids,
            opportunity_matching_end_time=opportunity_matching_end_time,
            update_time=update_time,
        )

        opportunity_matching_status_change_webhook_data.additional_properties = d
        return opportunity_matching_status_change_webhook_data

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
