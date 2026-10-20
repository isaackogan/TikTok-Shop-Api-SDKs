from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fail_reason import FailReason


T = TypeVar("T", bound="PartialEditGlobalProductResponseDataPublishResult")


@_attrs_define
class PartialEditGlobalProductResponseDataPublishResult:
    """
    Attributes:
        region (str | Unset): The market where the product is published
            Possible values:
            - DE: Germany
            - ES: Spain
            - FR: France
            - GB: United Kingdom
            - ID: Indonesia
            - IE: Ireland
            - IT: Italy
            - JP: Japan
            - MX: Mexico
            - MY: Malaysia
            - PH: Philippines
            - SG: Singapore
            - TH: Thailand
            - US: United States
            - VN: Vietnam
        status (str | Unset): The status of syncing the product to the market.
            Possible values:
            - SUCCESS: The global product was successfully synchronized to the local shop, submitted for listing, and is now
            under review. Use the [Product status change](650956aff1fd3102b90b6261) webhook to track subsequent audit status
            changes and completion.
            - FAILED: Synchronization of the global product to the local shop was unsuccessful.
        fail_reasons (list[FailReason] | Unset): The list of errors that occurred.
    """

    region: str | Unset = UNSET
    status: str | Unset = UNSET
    fail_reasons: list[FailReason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region

        status = self.status

        fail_reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fail_reasons, Unset):
            fail_reasons = []
            for fail_reasons_item_data in self.fail_reasons:
                fail_reasons_item = fail_reasons_item_data.to_dict()
                fail_reasons.append(fail_reasons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status
        if fail_reasons is not UNSET:
            field_dict["fail_reasons"] = fail_reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fail_reason import FailReason  # noqa: PLC0415

        d = dict(src_dict)
        region = d.pop("region", UNSET)

        status = d.pop("status", UNSET)

        _fail_reasons = d.pop("fail_reasons", UNSET)
        fail_reasons: list[FailReason] | Unset = UNSET
        if _fail_reasons is not UNSET:
            fail_reasons = []
            for fail_reasons_item_data in _fail_reasons:
                fail_reasons_item = FailReason.from_dict(fail_reasons_item_data)

                fail_reasons.append(fail_reasons_item)

        partial_edit_global_product_response_data_publish_result = cls(
            region=region,
            status=status,
            fail_reasons=fail_reasons,
        )

        partial_edit_global_product_response_data_publish_result.additional_properties = d
        return partial_edit_global_product_response_data_publish_result

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
