from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_submission_records_response_data_data_submission import GetSubmissionRecordsResponseDataDataSubmission





T = TypeVar("T", bound="GetSubmissionRecordsResponseDataData")



@_attrs_define
class GetSubmissionRecordsResponseDataData:
    """ 
        Attributes:
            submissions (list[GetSubmissionRecordsResponseDataDataSubmission] | Unset): List of submission records.
            next_page_token (str | Unset): Token for fetching next page. Empty if no more pages.
            total_count (int | Unset): Total number of matching submissions (approximate).
     """

    submissions: list[GetSubmissionRecordsResponseDataDataSubmission] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_submission_records_response_data_data_submission import GetSubmissionRecordsResponseDataDataSubmission # noqa: PLC0415
        submissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.submissions, Unset):
            submissions = []
            for submissions_item_data in self.submissions:
                submissions_item = submissions_item_data.to_dict()
                submissions.append(submissions_item)



        next_page_token = self.next_page_token

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if submissions is not UNSET:
            field_dict["submissions"] = submissions
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_submission_records_response_data_data_submission import GetSubmissionRecordsResponseDataDataSubmission # noqa: PLC0415
        d = dict(src_dict)
        _submissions = d.pop("submissions", UNSET)
        submissions: list[GetSubmissionRecordsResponseDataDataSubmission] | Unset = UNSET
        if _submissions is not UNSET:
            submissions = []
            for submissions_item_data in _submissions:
                submissions_item = GetSubmissionRecordsResponseDataDataSubmission.from_dict(submissions_item_data)



                submissions.append(submissions_item)


        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        get_submission_records_response_data_data = cls(
            submissions=submissions,
            next_page_token=next_page_token,
            total_count=total_count,
        )


        get_submission_records_response_data_data.additional_properties = d
        return get_submission_records_response_data_data

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
