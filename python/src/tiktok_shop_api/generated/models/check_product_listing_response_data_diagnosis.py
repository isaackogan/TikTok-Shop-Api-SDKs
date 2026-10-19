from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_product_listing_response_data_diagnosis_field import CheckProductListingResponseDataDiagnosisField
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_product_listing_response_data_diagnosis_suggestion import (
        CheckProductListingResponseDataDiagnosisSuggestion,
    )
    from ..models.diagnosis_result import DiagnosisResult


T = TypeVar("T", bound="CheckProductListingResponseDataDiagnosis")


@_attrs_define
class CheckProductListingResponseDataDiagnosis:
    """
    Attributes:
        field (CheckProductListingResponseDataDiagnosisField | Unset): The product field being diagnosed.
            Possible values:
            - TITLE: Product title
            - DESCRIPTION: Product description
            - IMAGE: Product image displayed in the image gallery
            - ATTRIBUTE: Product attribute
            - SIZE_CHART: Product size chart
        diagnosis_results (list[DiagnosisResult] | Unset): The diagnosis results.
        suggestions (CheckProductListingResponseDataDiagnosisSuggestion | Unset):
    """

    field: CheckProductListingResponseDataDiagnosisField | Unset = UNSET
    diagnosis_results: list[DiagnosisResult] | Unset = UNSET
    suggestions: CheckProductListingResponseDataDiagnosisSuggestion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field: str | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.value

        diagnosis_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.diagnosis_results, Unset):
            diagnosis_results = []
            for diagnosis_results_item_data in self.diagnosis_results:
                diagnosis_results_item = diagnosis_results_item_data.to_dict()
                diagnosis_results.append(diagnosis_results_item)

        suggestions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = self.suggestions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if diagnosis_results is not UNSET:
            field_dict["diagnosis_results"] = diagnosis_results
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_product_listing_response_data_diagnosis_suggestion import (
            CheckProductListingResponseDataDiagnosisSuggestion,  # noqa: PLC0415
        )
        from ..models.diagnosis_result import DiagnosisResult  # noqa: PLC0415

        d = dict(src_dict)
        _field = d.pop("field", UNSET)
        field: CheckProductListingResponseDataDiagnosisField | Unset
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = CheckProductListingResponseDataDiagnosisField(_field)

        _diagnosis_results = d.pop("diagnosis_results", UNSET)
        diagnosis_results: list[DiagnosisResult] | Unset = UNSET
        if _diagnosis_results is not UNSET:
            diagnosis_results = []
            for diagnosis_results_item_data in _diagnosis_results:
                diagnosis_results_item = DiagnosisResult.from_dict(diagnosis_results_item_data)

                diagnosis_results.append(diagnosis_results_item)

        _suggestions = d.pop("suggestions", UNSET)
        suggestions: CheckProductListingResponseDataDiagnosisSuggestion | Unset
        if isinstance(_suggestions, Unset):
            suggestions = UNSET
        else:
            suggestions = CheckProductListingResponseDataDiagnosisSuggestion.from_dict(_suggestions)

        check_product_listing_response_data_diagnosis = cls(
            field=field,
            diagnosis_results=diagnosis_results,
            suggestions=suggestions,
        )

        check_product_listing_response_data_diagnosis.additional_properties = d
        return check_product_listing_response_data_diagnosis

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
