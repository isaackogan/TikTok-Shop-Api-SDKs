from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.diagnosis_result import DiagnosisResult
  from ..models.suggestion import Suggestion





T = TypeVar("T", bound="Diagnosis")



@_attrs_define
class Diagnosis:
    """ 
        Attributes:
            field (str | Unset): The product field being diagnosed.
                Possible values:
                - TITLE: Product title
                - DESCRIPTION: Product description
                - IMAGE: Product image displayed in the image gallery
                - ATTRIBUTE: Product attribute
                - SIZE_CHART: Product size chart
            diagnosis_results (list[DiagnosisResult] | Unset): The results of diagnosing the specified field.
            suggestion (Suggestion | Unset):
     """

    field: str | Unset = UNSET
    diagnosis_results: list[DiagnosisResult] | Unset = UNSET
    suggestion: Suggestion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.diagnosis_result import DiagnosisResult # noqa: PLC0415
        from ..models.suggestion import Suggestion # noqa: PLC0415
        field = self.field

        diagnosis_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.diagnosis_results, Unset):
            diagnosis_results = []
            for diagnosis_results_item_data in self.diagnosis_results:
                diagnosis_results_item = diagnosis_results_item_data.to_dict()
                diagnosis_results.append(diagnosis_results_item)



        suggestion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggestion, Unset):
            suggestion = self.suggestion.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if field is not UNSET:
            field_dict["field"] = field
        if diagnosis_results is not UNSET:
            field_dict["diagnosis_results"] = diagnosis_results
        if suggestion is not UNSET:
            field_dict["suggestion"] = suggestion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnosis_result import DiagnosisResult # noqa: PLC0415
        from ..models.suggestion import Suggestion # noqa: PLC0415
        d = dict(src_dict)
        field = d.pop("field", UNSET)

        _diagnosis_results = d.pop("diagnosis_results", UNSET)
        diagnosis_results: list[DiagnosisResult] | Unset = UNSET
        if _diagnosis_results is not UNSET:
            diagnosis_results = []
            for diagnosis_results_item_data in _diagnosis_results:
                diagnosis_results_item = DiagnosisResult.from_dict(diagnosis_results_item_data)



                diagnosis_results.append(diagnosis_results_item)


        _suggestion = d.pop("suggestion", UNSET)
        suggestion: Suggestion | Unset
        if isinstance(_suggestion,  Unset):
            suggestion = UNSET
        else:
            suggestion = Suggestion.from_dict(_suggestion)




        diagnosis = cls(
            field=field,
            diagnosis_results=diagnosis_results,
            suggestion=suggestion,
        )


        diagnosis.additional_properties = d
        return diagnosis

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
