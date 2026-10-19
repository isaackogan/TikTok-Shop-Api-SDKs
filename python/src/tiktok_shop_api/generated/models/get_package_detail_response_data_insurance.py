from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_package_detail_response_data_insurance_claim_status import (
    GetPackageDetailResponseDataInsuranceClaimStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPackageDetailResponseDataInsurance")


@_attrs_define
class GetPackageDetailResponseDataInsurance:
    """
    Attributes:
        is_purchased (bool | Unset): Whether insurance has been purchased for the package.
        coverage_amount (str | Unset): The insurance coverage amount for the package. Units: USD.
        is_claim_eligible (bool | Unset): Whether the package is eligible for an insurance claim, based on eligible
            refund reasons.
        claim_status (GetPackageDetailResponseDataInsuranceClaimStatus | Unset): The insurance claim status.
            Available values:
            - `NOT_STARTED`: Claim has not been initiated for this package.
            - `CLAIM_PENDING`: Claim is currently under review.
            - `APPROVED`: Claim has been approved.
            - `DECLINED`: Claim has been declined.
    """

    is_purchased: bool | Unset = UNSET
    coverage_amount: str | Unset = UNSET
    is_claim_eligible: bool | Unset = UNSET
    claim_status: GetPackageDetailResponseDataInsuranceClaimStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_purchased = self.is_purchased

        coverage_amount = self.coverage_amount

        is_claim_eligible = self.is_claim_eligible

        claim_status: str | Unset = UNSET
        if not isinstance(self.claim_status, Unset):
            claim_status = self.claim_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_purchased is not UNSET:
            field_dict["is_purchased"] = is_purchased
        if coverage_amount is not UNSET:
            field_dict["coverage_amount"] = coverage_amount
        if is_claim_eligible is not UNSET:
            field_dict["is_claim_eligible"] = is_claim_eligible
        if claim_status is not UNSET:
            field_dict["claim_status"] = claim_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_purchased = d.pop("is_purchased", UNSET)

        coverage_amount = d.pop("coverage_amount", UNSET)

        is_claim_eligible = d.pop("is_claim_eligible", UNSET)

        _claim_status = d.pop("claim_status", UNSET)
        claim_status: GetPackageDetailResponseDataInsuranceClaimStatus | Unset
        if isinstance(_claim_status, Unset):
            claim_status = UNSET
        else:
            claim_status = GetPackageDetailResponseDataInsuranceClaimStatus(_claim_status)

        get_package_detail_response_data_insurance = cls(
            is_purchased=is_purchased,
            coverage_amount=coverage_amount,
            is_claim_eligible=is_claim_eligible,
            claim_status=claim_status,
        )

        get_package_detail_response_data_insurance.additional_properties = d
        return get_package_detail_response_data_insurance

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
