from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publish_result_region import PublishResultRegion
from ..models.publish_result_status import PublishResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fail_reason import FailReason


T = TypeVar("T", bound="PublishResult")


@_attrs_define
class PublishResult:
    """
    Attributes:
        region (PublishResultRegion | Unset): The market associated with this synchronization result.
            Possible values:
            - AT: Austria
            - BE: Belgium
            - CZ: Czech Republic
            - DE: Germany
            - ES: Spain
            - FR: France
            - GB: United Kingdom
            - GR: Greece
            - HU: Hungary
            - ID: Indonesia
            - IE: Ireland
            - IT: Italy
            - JP: Japan
            - MY: Malaysia
            - NL: Netherlands (NL)
            - PH: Philippines
            - PO: Poland
            - PT: Portugal
            - SG: Singapore
            - TH: Thailand
            - US: United States
            - VN: Vietnam
            - MX: Mexico
        status (PublishResultStatus | Unset): The status of syncing the product to the market.
            Possible values:
            - SUCCESS: The global product was successfully synchronized to the local shop, submitted for listing, and is now
            under review. Use the [Product Status Change
            webhook](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) to track the final audit status.
            - DRAFT: Synchronization did not complete, and the local product remains in draft.
            - FAILED: Synchronization of the global product to the local shop was unsuccessful.
        fail_reasons (list[FailReason] | Unset): The list of errors that occurred.
    """

    region: PublishResultRegion | Unset = UNSET
    status: PublishResultStatus | Unset = UNSET
    fail_reasons: list[FailReason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        _region = d.pop("region", UNSET)
        region: PublishResultRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = PublishResultRegion(_region)

        _status = d.pop("status", UNSET)
        status: PublishResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PublishResultStatus(_status)

        _fail_reasons = d.pop("fail_reasons", UNSET)
        fail_reasons: list[FailReason] | Unset = UNSET
        if _fail_reasons is not UNSET:
            fail_reasons = []
            for fail_reasons_item_data in _fail_reasons:
                fail_reasons_item = FailReason.from_dict(fail_reasons_item_data)

                fail_reasons.append(fail_reasons_item)

        publish_result = cls(
            region=region,
            status=status,
            fail_reasons=fail_reasons,
        )

        publish_result.additional_properties = d
        return publish_result

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
