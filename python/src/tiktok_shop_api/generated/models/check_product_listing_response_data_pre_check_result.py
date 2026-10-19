from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_product_listing_response_data_pre_check_result_pre_check_detail import (
        CheckProductListingResponseDataPreCheckResultPreCheckDetail,
    )


T = TypeVar("T", bound="CheckProductListingResponseDataPreCheckResult")


@_attrs_define
class CheckProductListingResponseDataPreCheckResult:
    """
    Attributes:
        pre_check_item (str | Unset): Product information verification type: The types of issues returned by product
            information verification.
        pre_check_details (list[CheckProductListingResponseDataPreCheckResultPreCheckDetail] | Unset): Information
            Verification Details.
    """

    pre_check_item: str | Unset = UNSET
    pre_check_details: list[CheckProductListingResponseDataPreCheckResultPreCheckDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pre_check_item = self.pre_check_item

        pre_check_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pre_check_details, Unset):
            pre_check_details = []
            for pre_check_details_item_data in self.pre_check_details:
                pre_check_details_item = pre_check_details_item_data.to_dict()
                pre_check_details.append(pre_check_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pre_check_item is not UNSET:
            field_dict["pre_check_item"] = pre_check_item
        if pre_check_details is not UNSET:
            field_dict["pre_check_details"] = pre_check_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_product_listing_response_data_pre_check_result_pre_check_detail import (
            CheckProductListingResponseDataPreCheckResultPreCheckDetail,  # noqa: PLC0415
        )

        d = dict(src_dict)
        pre_check_item = d.pop("pre_check_item", UNSET)

        _pre_check_details = d.pop("pre_check_details", UNSET)
        pre_check_details: list[CheckProductListingResponseDataPreCheckResultPreCheckDetail] | Unset = UNSET
        if _pre_check_details is not UNSET:
            pre_check_details = []
            for pre_check_details_item_data in _pre_check_details:
                pre_check_details_item = CheckProductListingResponseDataPreCheckResultPreCheckDetail.from_dict(
                    pre_check_details_item_data
                )

                pre_check_details.append(pre_check_details_item)

        check_product_listing_response_data_pre_check_result = cls(
            pre_check_item=pre_check_item,
            pre_check_details=pre_check_details,
        )

        check_product_listing_response_data_pre_check_result.additional_properties = d
        return check_product_listing_response_data_pre_check_result

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
