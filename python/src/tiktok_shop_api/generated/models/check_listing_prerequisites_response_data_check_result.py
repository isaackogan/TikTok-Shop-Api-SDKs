from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_listing_prerequisites_response_data_check_result_check_item import (
    CheckListingPrerequisitesResponseDataCheckResultCheckItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckListingPrerequisitesResponseDataCheckResult")


@_attrs_define
class CheckListingPrerequisitesResponseDataCheckResult:
    """
    Attributes:
        check_item (CheckListingPrerequisitesResponseDataCheckResultCheckItem | Unset): A requirement that the shop
            needs to satisfy.
            Possible values:
            - SHOP_STATUS
            - SHOP_TAX
            - PICKUP_WAREHOUSE
            - RETURN_WAREHOUSE
            - DELIVERY_OPTION
            - SHIPPING_TEMPLATE
            - PRODUCT_QUANTITY_LIMIT
            - EXTENDED_PRODUCER_RESPONSIBILITY
            - BANk_ACCOUNT
            - CONTACT_INFO
        is_failed (bool | Unset): A flag indicating whether the shop has failed a `check_item`.
        fail_reasons (list[str] | Unset): The specific reasons for failing a certain `check_item`.
    """

    check_item: CheckListingPrerequisitesResponseDataCheckResultCheckItem | Unset = UNSET
    is_failed: bool | Unset = UNSET
    fail_reasons: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_item: str | Unset = UNSET
        if not isinstance(self.check_item, Unset):
            check_item = self.check_item.value

        is_failed = self.is_failed

        fail_reasons: list[str] | Unset = UNSET
        if not isinstance(self.fail_reasons, Unset):
            fail_reasons = self.fail_reasons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_item is not UNSET:
            field_dict["check_item"] = check_item
        if is_failed is not UNSET:
            field_dict["is_failed"] = is_failed
        if fail_reasons is not UNSET:
            field_dict["fail_reasons"] = fail_reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _check_item = d.pop("check_item", UNSET)
        check_item: CheckListingPrerequisitesResponseDataCheckResultCheckItem | Unset
        if isinstance(_check_item, Unset):
            check_item = UNSET
        else:
            check_item = CheckListingPrerequisitesResponseDataCheckResultCheckItem(_check_item)

        is_failed = d.pop("is_failed", UNSET)

        fail_reasons = cast(list[str], d.pop("fail_reasons", UNSET))

        check_listing_prerequisites_response_data_check_result = cls(
            check_item=check_item,
            is_failed=is_failed,
            fail_reasons=fail_reasons,
        )

        check_listing_prerequisites_response_data_check_result.additional_properties = d
        return check_listing_prerequisites_response_data_check_result

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
