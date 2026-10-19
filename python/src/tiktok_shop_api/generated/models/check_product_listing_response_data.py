from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_product_listing_response_data_diagnosis import CheckProductListingResponseDataDiagnosis
    from ..models.check_product_listing_response_data_fail_reason import CheckProductListingResponseDataFailReason
    from ..models.check_product_listing_response_data_listing_quality import (
        CheckProductListingResponseDataListingQuality,
    )
    from ..models.check_product_listing_response_data_pre_check_result import (
        CheckProductListingResponseDataPreCheckResult,
    )
    from ..models.warning import Warning_


T = TypeVar("T", bound="CheckProductListingResponseData")


@_attrs_define
class CheckProductListingResponseData:
    """
    Attributes:
        check_result (str | Unset): The result of the product diagnosis (PASS, FAILED).
        fail_reasons (list[CheckProductListingResponseDataFailReason] | Unset): A list of failure reasons if
            `check_result` is FAILED.
        warnings (Warning_ | Unset):
        listing_quality (CheckProductListingResponseDataListingQuality | Unset):
        diagnoses (list[CheckProductListingResponseDataDiagnosis] | Unset): (**Deprecated**: This field is deprecated
            and will be removed in a future API version. Use [Diagnose and Optimize Product](677c9523f7765c0308b3d68d) API
            instead to get product diagnosis related information.)
            Product optimization diagnosis information.
        pre_check_results (list[CheckProductListingResponseDataPreCheckResult] | Unset): Contains any completed product
            information verification findings available for the supplied `gne_async_check_session_id`. The response does not
            expose a separate pending or completed status. If this field is missing or empty, you cannot determine from the
            response whether the asynchronous checks have completed or passed.
    """

    check_result: str | Unset = UNSET
    fail_reasons: list[CheckProductListingResponseDataFailReason] | Unset = UNSET
    warnings: Warning_ | Unset = UNSET
    listing_quality: CheckProductListingResponseDataListingQuality | Unset = UNSET
    diagnoses: list[CheckProductListingResponseDataDiagnosis] | Unset = UNSET
    pre_check_results: list[CheckProductListingResponseDataPreCheckResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_result = self.check_result

        fail_reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fail_reasons, Unset):
            fail_reasons = []
            for fail_reasons_item_data in self.fail_reasons:
                fail_reasons_item = fail_reasons_item_data.to_dict()
                fail_reasons.append(fail_reasons_item)

        warnings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings.to_dict()

        listing_quality: dict[str, Any] | Unset = UNSET
        if not isinstance(self.listing_quality, Unset):
            listing_quality = self.listing_quality.to_dict()

        diagnoses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.diagnoses, Unset):
            diagnoses = []
            for diagnoses_item_data in self.diagnoses:
                diagnoses_item = diagnoses_item_data.to_dict()
                diagnoses.append(diagnoses_item)

        pre_check_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pre_check_results, Unset):
            pre_check_results = []
            for pre_check_results_item_data in self.pre_check_results:
                pre_check_results_item = pre_check_results_item_data.to_dict()
                pre_check_results.append(pre_check_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_result is not UNSET:
            field_dict["check_result"] = check_result
        if fail_reasons is not UNSET:
            field_dict["fail_reasons"] = fail_reasons
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if listing_quality is not UNSET:
            field_dict["listing_quality"] = listing_quality
        if diagnoses is not UNSET:
            field_dict["diagnoses"] = diagnoses
        if pre_check_results is not UNSET:
            field_dict["pre_check_results"] = pre_check_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_product_listing_response_data_diagnosis import (
            CheckProductListingResponseDataDiagnosis,  # noqa: PLC0415
        )
        from ..models.check_product_listing_response_data_fail_reason import (
            CheckProductListingResponseDataFailReason,  # noqa: PLC0415
        )
        from ..models.check_product_listing_response_data_listing_quality import (
            CheckProductListingResponseDataListingQuality,  # noqa: PLC0415
        )
        from ..models.check_product_listing_response_data_pre_check_result import (
            CheckProductListingResponseDataPreCheckResult,  # noqa: PLC0415
        )
        from ..models.warning import Warning_  # noqa: PLC0415

        d = dict(src_dict)
        check_result = d.pop("check_result", UNSET)

        _fail_reasons = d.pop("fail_reasons", UNSET)
        fail_reasons: list[CheckProductListingResponseDataFailReason] | Unset = UNSET
        if _fail_reasons is not UNSET:
            fail_reasons = []
            for fail_reasons_item_data in _fail_reasons:
                fail_reasons_item = CheckProductListingResponseDataFailReason.from_dict(fail_reasons_item_data)

                fail_reasons.append(fail_reasons_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: Warning_ | Unset
        if isinstance(_warnings, Unset):
            warnings = UNSET
        else:
            warnings = Warning_.from_dict(_warnings)

        _listing_quality = d.pop("listing_quality", UNSET)
        listing_quality: CheckProductListingResponseDataListingQuality | Unset
        if isinstance(_listing_quality, Unset):
            listing_quality = UNSET
        else:
            listing_quality = CheckProductListingResponseDataListingQuality.from_dict(_listing_quality)

        _diagnoses = d.pop("diagnoses", UNSET)
        diagnoses: list[CheckProductListingResponseDataDiagnosis] | Unset = UNSET
        if _diagnoses is not UNSET:
            diagnoses = []
            for diagnoses_item_data in _diagnoses:
                diagnoses_item = CheckProductListingResponseDataDiagnosis.from_dict(diagnoses_item_data)

                diagnoses.append(diagnoses_item)

        _pre_check_results = d.pop("pre_check_results", UNSET)
        pre_check_results: list[CheckProductListingResponseDataPreCheckResult] | Unset = UNSET
        if _pre_check_results is not UNSET:
            pre_check_results = []
            for pre_check_results_item_data in _pre_check_results:
                pre_check_results_item = CheckProductListingResponseDataPreCheckResult.from_dict(
                    pre_check_results_item_data
                )

                pre_check_results.append(pre_check_results_item)

        check_product_listing_response_data = cls(
            check_result=check_result,
            fail_reasons=fail_reasons,
            warnings=warnings,
            listing_quality=listing_quality,
            diagnoses=diagnoses,
            pre_check_results=pre_check_results,
        )

        check_product_listing_response_data.additional_properties = d
        return check_product_listing_response_data

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
